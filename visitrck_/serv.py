import sys
import os
from time import ctime
from uuid import uuid4
from tornado.options import define, options
from tornado.web import Application,RequestHandler
from tornado.ioloop import IOLoop
from tornado import locks
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from models.models import Visiter, Pageview

from utils.utils import genera_uuid
from utils.utils import ua_paser_str
from utils.utils import ip_to_isp_loc
from utils.utils import generate_random_str

#from tornado import options

#define("port", default=8888, help="run on the given port", type=int)
# define("db_host", default="va.fyping.cn", help="blog database host")
# define("db_port", default=5444, help="blog database port")
# define("db_database", default="blog_db", help="blog database name")
# define("db_user", default="fingeruser", help="blog database user")
# define("db_password", default="fingerechoroot123", help="blog database password")
DB_HOST="va.fyping.cn"
DB_PORT="5444"
DB_DATABASE="trackingsite"
DB_USER="fingeruser"
DB_PASSWORD="fingerechoroot123"



#######
##code from https://github.com/tornadoweb/tornado/issues/1675
######
class DataBase(object):
    def __init__(self):
        self.engine = create_engine("postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}".format(username=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            dbname=DB_DATABASE,
            port=DB_PORT))

class Application(Application):
    def __init__(self):
        self.database = DataBase()
        self.session = scoped_session(sessionmaker(bind=self.database.engine))
        handlers = [
            (r"/", MainHandler),
            (r'/uv', VisiterHandler),
        ]
        settings = dict(
            #template_path=os.path.join(os.path.dirname(__file__), "templates"),
            #static_path=os.path.join(os.path.dirname(__file__), "static"),
            #ui_modules={"Entry": EntryModule},
            #xsrf_cookies=True,
            cookie_secret=r'bhubyoifcwft7j3sarqbjcae',#"__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            #login_url="/auth/login",
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)
        #Application.__init__(self, handlers, **settings)

class BaseHandler(RequestHandler):
    ##session = self.application.session
    # def initialize(self):
    #     self.session = self.application.session
    def prepare(self):
        #self.xsrf_token=
        self.session = self.application.session
        self.set_header("Access-Control-Allow-Origin","*") 
        self.set_header("X-XSRFToken","helloworld")
    def on_finish(self):
        self.session.remove()

class VisiterHandler(BaseHandler):

    def init_avisiter(self,
        friend_status,
        visit_times,
        tokens,
        casual_user):
        ua = self.request.headers['User-Agent']
        device, os, browser = ua_paser_str(ua)
        uuid_ = uuid4()
        ip = self.request.remote_ip
        isp, location = ip_to_isp_loc(ip)
        first_time_visit=ctime()
        return Visiter(
        first_time_visit=first_time_visit,
        friend_status=friend_status,
        visit_times=visit_times,
        tokens=tokens,
        location=location,
        device=device,
        os=os,
        browser=browser,
        casual_user=casual_user,
        ip=ip,
        isp=isp,
        uuid=uuid_)
    async def insert_avisiter(self,visiter):
        self.application.session.add(visiter)
        self.application.session.commit()

    def query_exists(self,tokens):
        return False if 0==self.application.session.query(Visiter).filter(Visiter.tokens==tokens).count() else True

    async def update_times(self):
        tokens = self.get_argument("tokens",None)
        if tokens:
            if self.query_exists(tokens):
                tar = self.application.session.query(Visiter).filter(tokens==tokens).first()
                tar.visit_times = tar.visit_times + 1
            else:
                visiter = self.init_avisiter(friend_status=0,
                    visit_times=1,
                    casual_user=True,
                    tokens=tokens)
                self.application.session.add(visiter)

        else:
            for tar in self.application.session.query(Visiter).filter_by(ip=self.request.remote_ip).all():
                tar.casual_user = False                
        self.application.session.commit()
    async def post(self):
        await self.update_times()

class MainHandler(BaseHandler):
    async def get(self):
        if not self.get_cookie("mybaby"):
            self.set_cookie("mybaby",generate_random_str())
            self.set_status(status_code=204,reason="NOTHINGERROR")
        else:
            self.set_status(status_code=204,reason='200ok')
        self.finish()

async def main():
    global port

    app = Application()
    app.listen(port)

    shutdown_event = locks.Event()
    await shutdown_event.wait()


if __name__ == "__main__":
    port = sys.argv[1]
    if port:
        IOLoop.current().run_sync(main)
