#!/usr/bin/python3
from tornado.ioloop import IOLoop
from tornado import gen,web
from tornado_mysql import pools
from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPClientError as tornadoHTTPClientError
from tornado.simple_httpclient import HTTPTimeoutError as tornadoHTTPTimeoutError
from tornado.escape import xhtml_escape
from sys import argv
from logging import basicConfig as BasicConfig__
from logging import warning as Warning__
from logging import info as Info__
from time import localtime 
from ua_parser import user_agent_parser

from json import loads as Jsonloads__
from utils import para_contains
from utils import ua_paser_str
from utils import genera_uuid


connParam = { 'host': 'localhost', 'port': 3309, 'user': 'root','passwd': 'fy911phutys', 'db': 'trackingsite','charset':"utf8"}
class SortHandler(web.RequestHandler):
	POOL = pools.Pool(
		connParam,
		max_idle_connections = 1,
		max_recycle_sec=3
		)

	@gen.coroutine
	def post(self):
		if not self.request.headers.get('Welcome'):
			ua_str = self.request.headers['User-Agent']
			device , os , browser = ua_paser_str(ua_str)
			device = xhtml_escape(device)
			os = xhtml_escape(os)
			browser = xhtml_escape(browser)
			params = self.get_argument('params')
			para = params.split("$$");
			uuid = str(genera_uuid(ua_str))
			tokens = xhtml_escape("$$".join(para[:-1]))
			t_tm = localtime()
			friend_status='2' if para_contains(para,'m3') else '0'
			is_first = True
			sql = ""
			now = "%s-%s-%s@%s:%s:%s"%(t_tm.tm_year,\
				t_tm.tm_mon,t_tm.tm_mday,t_tm.tm_hour,t_tm.tm_min,t_tm.tm_sec)
			first_time_visit = '1001-01-01@01:01:01'
			visit_times = para[len(para)-1]
			last_time_visit = now
			ip = self.request.remote_ip
			location = isp = ""
			# try:
			# 	url = "http://ip.taobao.com//service/getIpInfo.php?ip=%s"%(ip)
			# 	cli = AsyncHTTPClient()
			# 	res_ = yield cli.fetch(url,method="GET")
			# 	res_su = res_.body.decode('utf-8')
			# 	result = Jsonloads__(res_su)
			# 	location = "%s-%s-%s"%(str(result['data']['country']),\
			# 						str(result['data']['area']),\
			# 						str(result['data']['city']))
			# 	isp = result['data']['isp']
			# except tornadoHTTPTimeoutError:
			# 	Warning__("get taobao ip faied because Timeout")
			# except tornadoHTTPClientError:
			# 	Warning__("get taobao ip failing because HTTPClienterror ")
			# except Exception:
			# 	Warning__("get taobao ip failed , unknown reason")
			self.set_header('welcome',uuid)
			######################
			#### Init params finished
			#########################
			casual_user = 1
			### select visit_times = from trackself_visiter where `tokens` = '153251bd49e90db2c799f5b9531bf440$$783100800959609886451892633';
			sql = """select visit_times from trackself_visiter where `tokens` = '{tokens}';""".format(tokens=tokens)
			cursor = yield self.POOL.execute(sql)
			if cursor.rowcount  == 1:
				casual_user = 1 if int(visit_times) == int(cursor.fetchone()[0]) else 0
			else:
				Warning__("Something went run !!!!!!!!!!!!!\nsql:\n%s"%(sql))		
			if para[len(para)-1] == "1":
				first_time_visit = now
			else:
				is_first = False
			if not visit_times.isdigit():
				visit_times = -1
			else:
				visit_times = int(visit_times)
			# insert into trackself_visiter (`first_time_visit`,`last_time_visit`,`friend_status`,`visit_times`,`tokens`,`location_city`)value('2018-11-17/09:10:10','2018-11-17/09:10:10','0',8,'helloworld','shenzhen');
			if is_first:
				sql = """insert into trackself_visiter (`first_time_visit`,`last_time_visit`,`friend_status`,`visit_times`,`tokens`,`device`,`os`,`browser`,`casual_user`,`ip`,`location`,`isp`,`uuid`)value('{first_time_visit}','{last_time_visit}','{friend_status}','{visit_times}','{tokens}','{device}','{os}','{browser}','{casual_user}','{ip}','{location}','{isp}','{uuid}');""".format(\
					first_time_visit=first_time_visit,\
					last_time_visit=last_time_visit,\
					friend_status=friend_status,\
					visit_times=visit_times,\
					tokens=tokens,\
					device=device,os=os,browser=browser,\
					casual_user=casual_user,\
					ip=ip,\
					location=location,\
					isp=isp,\
					uuid=uuid)
			else:
				# update trackself_visiter set `last_time_visit` = '2018-12-19' , visit_times = 101 where `tokens` = 'helloworld';
				sql = """update trackself_visiter set `last_time_visit`='{last_time_visit}',`friend_status`={friend_status},`visit_times`='{visit_times}' where `tokens`='{tokens}';""".format(\
				 	last_time_visit=last_time_visit,friend_status=friend_status,\
				 	visit_times=visit_times,tokens=tokens)
			#Info__(sql)	
			cursor = yield self.POOL.execute(sql)#'insert into   (first_time_visit
			#self.flush()
			headers = {'Content-Security-Policy':'script-src',
						'Access-Control-Allow-Origin':'*',
						"Content-Security-Policy":"script-src gitee.fyping.cn:65533 https://fingerecho.gitee.io",
						"Cache-Control":"Private",
						"Content-Type":"application/javascript"
					}
			for k,v in headers.items():
				self.set_header(k,v)
			self.write("console.log('helloworld from gitee.fyping.cn');")
			self.finish()
		else:
			self.set_status(status_code=204,reason='NoNeedReas')
			self.finish()
	@gen.coroutine
	def get(self):
		params = self.get_argument('params')
		print(params)
		self.write(params)
		self.finish()
class PageviewHandler(web.RequestHandler):
	POOL = pools.Pool(
	connParam,
	max_idle_connections = 1,
	max_recycle_sec=3
	)
	@gen.coroutine
	def post(self):
		#self.set_status(status_code=204,reason="WELOME HACKERS")
		language = xhtml_escape(self.get_argument('language',''))
		referer = xhtml_escape(self.get_argument("referrer","-"))
		brows_page = xhtml_escape(self.get_argument("location","-"))
		residencetime = xhtml_escape(self.get_argument("timesec"))
		random_ = xhtml_escape(self.get_argument('randoms','-'))
		platform = xhtml_escape(self.get_argument('platform','-'))
		screen = xhtml_escape(self.get_argument('screen','-'))
		#cursor = yield self.POOL.execute("select `id` from trackself_visiter where uuid = '%s' "%(uuid))
		#if cursor.rowcount == 1:
		#	id = str(cursor.fetchone()[0])
		sql = """insert into trackself_pageview (`brow_page`,`referer`,`language`,`residencetime`,`random`,`platform`,`screen`)value('{brows_page}','{referer}','{language}','{time_sec}','{random}','{platform}','{screen}');""".format(brows_page=brows_page,\
			referer=referer,\
			time_sec=residencetime,\
			language=language,\
			random=random_,\
			platform=platform,\
			screen=screen)
		#Warning__(sql)
		cur = yield self.POOL.execute(sql)
		self.set_status(status_code=204,reason="200ok")
		self.set_header("Access-Control-Allow-Origin","*")	
		#else:
		#	self.set_status(status_code=204,reason="BECAUSEYOUWERENOTUNIQUE")
		#	self.set_header("Access-Control-Allow-Origin","*")
		self.finish()
class LeavingsHandler(web.RequestHandler):
	POOL = pools.Pool(
		connParam,
		max_idle_connections = 1,
		max_recycle_sec=3
		)
	@gen.coroutine
	def get(self):
		ip = self.request.remote_ip
		url = "http://ip.taobao.com//service/getIpInfo.php?ip=%s"%(ip)
		cli = AsyncHTTPClient()
		res = yield cli.fetch(url,method="GET")
		res_su = res.body.decode("utf-8")
		result = Jsonloads__(res_su)
		location = "%s-%s-%s"%(result['data']['country'],\
							result['data']['area'],\
							result['data']['city'])
		isp = result['data']['isp']
		self.write({"ip":ip,"location":location,"isp":isp})
		self.finish()
	@gen.coroutine
	def post(self):
		first_name = xhtml_escapte(self.get_argument("first_name",""))
		last_name = xhtml_escapte(self.get_argument("last_name",""))
		username = xhtml_escapte(self.get_argument("username",""))
		email = xhtml_escapte(self.get_argument("email"))
		address = xhtml_escapte(self.get_argument("address",""))
		address2 = xhtml_escapte(self.get_argument("address2",""))
		content = xhtml_escapte(self.get_argument("content",""))
		tm_t = localtime()
		subtime = "%s-%s-%s"%(tm_t.tm_year,tm_t.tm_mon,tm_t.tm_mday)
		#insert into leavingshandle_leavings (`first_name`,`last_name`,`username`,`email`,`address`,`address2`,`content`,`subtime`) values('fyping','fang','fingerecho','33333@qq.com','jiangxi','shangyou','helloworld',2018-11-22')
		sql = "insert into leavingshandle_leavings (`first_name`,`last_name`,`username`,`email`,`address`,`address2`,`content`) values('{first_name}','{last_name}','{username}','{email}','{address}','{address2}','{content}')".format(first_name=first_name,last_name=last_name,username=username,email=email,address=address,address2=address2,content=content)
		cursor = yield self.POOL.execute(sql)
		headers = {"Access-Control-Allow-Origin":"*"}
		for k , v in headers.items():
			self.set_header( k , v)
		self.write({'first_name':first_name,'last_name':last_name,\
			'username':username,'email':email,'address':address,'address2':address2,\
			'content':content})	
		self.finish()
# if __name__ == "__main__":
# 	today = localtime()
# 	today = "{0}-{1}-{2}={3}".format(today.tm_year,today.tm_mon,today.tm_mday,today.tm_hour)
# 	#BasicConfig__(filename="log/serv_{date}.log".format(date=today))
# 	port = argv[1]
# 	app = web.Application([
# 		(r'/serve/tck',SortHandler),
# 		(r'/serve/leav',LeavingsHandler),
# 		(r'/serve/pgv',PageviewHandler),
# 		],autoreload=True
# 		)
# 	app.listen(port,xheaders=True);print("start listen")
# 	IOLoop.current().start()

