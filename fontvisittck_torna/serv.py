#!/usr/bin/python3
from tornado.ioloop import IOLoop
from tornado import gen,web
from tornado_mysql import pools
from tornado.httpclient import AsyncHTTPClient
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

DB_PORT = 10299
DB_PS = "helloworld\%joiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJ\%helloworld"
MAX_IDLE = 1024
MAX_REC = 64

connParam = { 'host': 'localhost', 'port': DB_PORT, 'user': 'dubbo','passwd': DB_PS, 'db': 'trackingsite','charset':"utf8"}
class SortHandler(web.RequestHandler):
	POOL = pools.Pool(
		connParam,
		max_idle_connections = MAX_IDLE,
		max_recycle_sec=MAX_REC
		)

	@gen.coroutine
	def post(self):
		ua_str = self.request.headers['User-Agent']
		device , os , browser = ua_paser_str(ua_str)
		device = xhtml_escape(device)
		os = xhtml_escape(os)
		browser = xhtml_escape(browser)
		brows_pages = "/".join(self.request.headers['referer'].split("//")[1:])
		params = self.get_argument('params')
		para = params.split("$$");
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
		url = "http://ip.taobao.com//service/getIpInfo.php?ip=%s"%(ip)
		cli = AsyncHTTPClient()
		res_ = yield cli.fetch(url,method="GET")
		res_su = res_.body.decode('utf-8')
		result = Jsonloads__(res_su)
		location = "%s-%s-%s"%(str(result['data']['country']),\
							str(result['data']['area']),\
							str(result['data']['city']))
		isp = result['data']['isp']
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
			sql = """insert into trackself_visiter (`first_time_visit`,`last_time_visit`,`friend_status`,`visit_times`,`tokens`,`device`,`os`,`browser`,`brows_pages`,`casual_user`,`ip`,`location`,`isp`)value('{first_time_visit}','{last_time_visit}','{friend_status}','{visit_times}','{tokens}','{device}','{os}','{browser}','{brows_pages}','{casual_user}','{ip}','{location}','{isp}');""".format(\
				first_time_visit=first_time_visit,\
				last_time_visit=last_time_visit,\
				friend_status=friend_status,\
				visit_times=visit_times,\
				tokens=tokens,\
				device=device,os=os,browser=browser,\
				brows_pages=brows_pages,\
				casual_user=casual_user,\
				ip=ip,\
				location=location,\
				isp=isp)
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
	@gen.coroutine
	def get(self):
		params = self.get_argument('params')
		print(params)
		self.write(params)
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
if __name__ == "__main__":
	today = localtime()
	today = "{0}-{1}-{2}={3}".format(today.tm_year,today.tm_mon,today.tm_mday,today.tm_hour)
	BasicConfig__(filename="log/serv_{date}.log".format(date=today))
	port = argv[1]
	app = web.Application([
		(r'/serve/tck',SortHandler),
		(r'/serve/leav',LeavingsHandler),
		],autoreload=True
		)
	app.listen(port,xheaders=True);print("start listen")
	IOLoop.current().start()

