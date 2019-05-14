#!/usr/bin/python
from time import sleep
from subprocess import call
from multiprocessing import Process
from os.path import join
from sys import exit

class MULP(Process):
	def __init__(self,port):
		Process.__init__(self)
		self.port = str(port)
	def run(self):
		init_(self.port)
def init_python_pro():
	flag_0 = not 1==call(['python3','-m','compileall','.'])
	#flag_1 = not 1==call(['mkdir','__pycache__/models'])
	#flag_2 = not 1==call(['mkdir','__pycache__/utils'])
	flag_3 = not 1==call(['mv','utils/__pycache__/__init__.cpython-36.pyc','__pycache__/utils'])
	flag_3 = not 1==call(['mv','utils/__pycache__/utils.cpython-36.pyc','__pycache__/utils'])
	flag_3 = not 1==call(['mv','models/__pycache__/__init__.cpython-36.pyc','__pycache__/models'])
	flag_3 = not 1==call(['mv','models/__pycache__/models.cpython-36.pyc','__pycache__/models'])
	#flag_5 = not 1==call(['mv','__pycache__/models/__init__.cpython-36.pyc','__pycache__/models/__init__.pyc'])
#	flag_6 = not 1==call(['mv','__pycache__/models/models.cpython-36.pyc','__pycache__/models/models.pyc'])
#	flag_7 = not 1==call(['mv','__pycache__/utils/__init__.cpython-36.pyc','__pycache__/models/__init__.pyc'])
#	flag_7 = not 1==call(['mv','__pycache__/utils/utils.cpython-36.pyc','__pycache__/models/utils.pyc'])
#	
	# if flag_0 and flag_1 and flag_2 and flag_3 and flag_4:
	if True:	
		print("compile python program finished")
		return 1
	else:
		print("compile python program failed")
		return 0
def init_(port):
	if 1==call(['nohup','python3','__pycache__/serv.cpython-36.pyc',port,'&']):
		print("success")
	else:
		print("failed")
	#sleep(1)
if __name__ == "__main__":
	if 0 == init_python_pro():
		exit()
	for port in range(8010,8018):
		tmp = MULP(port)
		tmp.start()
