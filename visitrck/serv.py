import sys
import os
from time import ctime
from datetime import datetime
from uuid import uuid4
from tornado.options import define, options
from tornado.web import Application,RequestHandler
from tornado.websocket import WebSocketHandler
from tornado.ioloop import IOLoop
from tornado import locks

from utils.utils import genera_uuid
from utils.utils import ua_paser_str
from utils.utils import ip_to_isp_loc
from utils.utils import generate_random_str

from database.rdf import insert 
from rdflib import Graph, Literal, URIRef, term
DEBUG_MODE = True

class Application(Application):
    def __init__(self):
        global DEBUG_MODE
        handlers = [
            (r"/", MainHandler),
            (r'/uv', VisiterHandler),
            (r'/pv', VisiterHandler),
            (r'/ht', VisiterHandler),
            # (r'/pv', PageviewHandler),
            # (r'/ht', PageviewHeartHandler),
        ]
        settings = dict(
            #template_path=os.path.join(os.path.dirname(__file__), "templates"),
            #static_path=os.path.join(os.path.dirname(__file__), "static"),
            #ui_modules={"Entry": EntryModule},
            #xsrf_cookies=True,
            cookie_secret=r'bhubyoifcwft7j3sarqbjcae',#"__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            #login_url="/auth/login",
            debug=DEBUG_MODE,
        )
        super(Application, self).__init__(handlers, **settings)
        
class BaseHandler(RequestHandler):
    # def initialize(self):
    #     self.session = self.application.session
    def prepare(self):
        #self.xsrf_token=
        self.set_header("Access-Control-Allow-Origin","*") 
        self.set_header("X-XSRFToken","helloworld")
    def on_finish(self):
        #self.session.remove()
        pass

class VisiterHandler(BaseHandler):

    def init_avisiter(self,tokens):
        ua = self.request.headers['User-Agent']
        device, os, browser = ua_paser_str(ua)
        ip = self.request.headers['X-Real-Ip']
        #isp, location = ip_to_isp_loc(ip)
        g = Graph()
        tokens = "https://fangself.com.cn/trackingsite/" + tokens
        g.add((URIRef(tokens),URIRef(u"urn:recordtime"),Literal(datetime.now())))
        g.add((URIRef(tokens),URIRef(u"urn:useragent"),Literal(ua)))
        g.add((URIRef(tokens),URIRef(u"urn:ip"),Literal(ip)))
        g.add((URIRef(tokens),URIRef(u"urn:device"),Literal(device)))
        g.add((URIRef(tokens),URIRef(u"urn:os"),Literal(os)))
        g.add((URIRef (tokens),URIRef(u"urn:browser"),Literal(browser)))
        insert(g)
        return False
    async def post(self):
        res =  self.init_avisiter(self.get_argument("tokens",None))
        if self.get_argument("tokens"):
            #if not res:
            self.set_status(status_code=204,reason="200ok")
            #else:
            #    self.write('{"status":"100","message":"error."}')
        else:
            self.write('{"status":"200","message":"ok."}')
        self.finish()


class MainHandler(BaseHandler):
    async def get(self):
        if not self.get_cookie("mybaby"):
            self.set_cookie("mybaby",generate_random_str())
            #self.set_status(status_code=204,reason="NOTHINGERROR")
            self.write("cookie helloworld")
        else:
            #self.set_status(status_code=204,reason='200ok')
            self.write("helloworld")
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

