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
	if not 1==call(['python3','-m','compileall','serv.py']):
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
