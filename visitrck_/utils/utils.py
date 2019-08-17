from ua_parser import user_agent_parser
from time import time
from random import sample
from string import ascii_letters

def para_contains(li:list,value):
	for i in li:
		if i.strip() == value:
			return True
	return False


def ua_paser_str(ua_str:str):
	if not ua_str:
		return "-","-","-"
	info = user_agent_parser.Parse(ua_str)
	device = info['device']['brand'] if info['device']['brand']!= None else ""
	device = device + info['device']['family'] if info['device']['family']!=None else ""
	device = device + info['device']['model'] if info['device']['model']!= None else ""
	os = info['os']['family'] if info['os']['family'] else ""
	os = os + info['os']['major'] if info['os']['major'] else ""
	os = os + info['os']['minor'] if info['os']['minor'] else ""
	os = os + info['os']['patch'] if info['os']['patch'] else ""
	os = os + info['os']['patch_minor'] if info['os']['patch_minor']  else ""
	browser = info['user_agent']['family'] if info['user_agent']['family']!=None else ""
	return device , os , browser

def genera_uuid(ua_str:str):
	t_ = str(time()*1000000)
	return hash(ua_str+t_)
def generate_random_str():
	return "".join(sample(ascii_letters,8))
def ip_to_isp_loc(ip):
	return "-isp-","-loc-"
