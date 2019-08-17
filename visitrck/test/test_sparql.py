import sys
sys.path.append("../database")

import json

import rdf as localrdf

from rdflib import Graph, Literal, URIRef
from datetime import datetime


china = Literal("china")
china_url = URIRef("http://www.china.cn/index.html")
china_ns  = URIRef("http://www.china.cn")
tokens = "http://www.fff.com/12345678901236780"
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
ip = "192.168.0.1"
device = "Win"
os     = "Windows 10"
browser= "firefox"

g = Graph()
g.add((URIRef(tokens),URIRef(u"urn:recordtime"),Literal(datetime.now())))
g.add((URIRef(tokens),URIRef(u"urn:useragent"),Literal(ua)))
g.add((URIRef(tokens),URIRef(u"urn:ip"),Literal(ip)))
g.add((URIRef(tokens),URIRef(u"urn:device"),Literal(device)))
g.add((URIRef(tokens),URIRef(u"urn:os"),Literal(os)))
g.add((URIRef(tokens),URIRef(u"urn:browser"),Literal(browser)))

print(g.serialize(format='n3').decode('utf-8'))

#qstr = "select * where { ?page ?ns  ?name . }"

# res = localrdf.query(qstr)
# print(res)

# ustr = 'delete data { <http://www.china.cn/index.html> <http://www.china.cn> "china"}; '

# res = localrdf.update(ustr)
# print(res)

# ustr = 'insert data { <http://www.china.cn/hello.html> <http://www.china.cn> "china"};'
# res = localrdf.update(ustr)
# print(res)


# qstr = "select * where { ?page ?ns  ?name . }"

# res = localrdf.query(qstr)
# print(res)
