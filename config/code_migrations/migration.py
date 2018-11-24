#!/usr/bin/python3

from os import walk , chdir ,path  
from subprocess import call
from os import sep as SEP
from sys import argv
from os import system

PORT = 2222
HOST = "va.fyping.cn"
USER = "dubbo"
RSA_FILE = "luby.rsa"
PRO_NAME = "trackingsite"

def handle(path:str):
    global PORT,HOST,USER,RSA_FILE
    #print("<<<<<<<<",path,">>>>>>>")
    origin_file = path.strip("..{SEP}..{SEP}".format(SEP=SEP))
    origin_linux = "/".join(origin_file.split(SEP))
    cm_meta = "scp -i ..{SEP}..{SEP}..{SEP}..{SEP}administrator{SEP}.ssh{SEP}{RSA} \
    	-P {PORT} -r ..{SEP}..{SEP}{ORIGIN}\
    	 {USERNAME}@{HOST}:{SEP_LINUX}srv{SEP_LINUX}{PRO_NAME}{SEP_LINUX}{ORIGIN_LINUX}".format(\
    		SEP=SEP,PORT=PORT,ORIGIN=origin_file,\
    		USERNAME=USER,HOST=HOST,\
    		RSA=RSA_FILE,PRO_NAME=PRO_NAME,\
    		ORIGIN_LINUX=origin_linux,\
    		SEP_LINUX="/")
    print(cm_meta)
    if 0==call(cm_meta):
    	print("execute success")
    else:
    	print("execute failed , please check process code")

def run_all(path:str):
    tr = walk(path)
    for t in tr:
        for file_ in t[2]:
            handle(file_)
def run_all_opt(path:str):
    ZZ = [ [t[0],t[2]] for t in walk(path)]
    res_ = []
    for xx in ZZ:
  	    for yy in xx[1]:
  	    	res_.append("%s%s%s"%(xx[0],SEP,yy))
  	        #res_.append(path.join(xx[0],yy))
    [handle(file_) for file_ in res_]
if __name__ == "__main__":
    #run_all_opt("..%s..%s"%(SEP,SEP))
    #if len(argv) > 1 :
    #	handle(argv[1])
    head = "scp -i ../../administrator/.ssh/vt.va.rsa -P"
    if len(argv) > 1:
        if argv[1] == "leavingshandle" or argv[1]== "leave":
            chdir("../../")
            print("start async")
            system("{head} {port} -r ./leavingshandle/* root@va.fyping.cn:/srv/trackingsite/leavingshandle".format(port=PORT,head=head))
        if argv[1] == "fontvsitck_" or argv[1] == "tornado":
            chdir("../../")
            print("start async")
            system("{head} -P {port} -r ./fontvisittck_torna/* root@va.fyping.cn:/srv/trackingsite/fontvisittck_torna".format(port=PORT,head=head))
        if argv[1] == 'all':
            chdir("../../")
            print("async all")
            system("{head} {port} -r  ./* root@va.fyping.cn:/srv/trackingsite".format(port=PORT))
        if argv[1] == "re-sqlfile":
            chdir("../../")
            system("{head} {port} -r  root@va.fyping.cn:/srv/trackingsite/data/trackingsite_bak_181124.sql ./data".format(port=PORT,head=head))
            print("download")            