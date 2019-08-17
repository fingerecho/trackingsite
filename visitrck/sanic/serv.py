import sys
import os
from time import ctime,time
from datetime import datetime
from uuid import uuid4

from utils.utils import genera_uuid
from utils.utils import ua_paser_str
from utils.utils import ip_to_isp_loc
from utils.utils import generate_random_str

from database.rdf import insert 
import config

from rdflib import Graph, Literal, URIRef, term

import uvicorn
NAMESPACE_PREFIX = config.NAMESPACE_PREFIX

debug = config.DEBUG_MODEL


HOST = "0.0.0.0"
DEBUG_MODE = False
LOG_LEVEL  = "debug"

async def read_tokens(receive):
    body = b""
    more_body = True
    while more_body:
        message = await receive()
        body = message.get('body',b'')
        more_body = message.get('more_body',False)
    tokens = body.decode("utf-8")
    return tokens

def init_graph(tokens,ip,device,os,browser,ua):
    g = Graph()
    tokens = NAMESPACE_PREFIX + tokens
    if debug:
        g.add((URIRef(tokens),URIRef(u"urn:recordtime"),Literal(str(time()))))
    else:
        g.add((URIRef(tokens), URIRef(u"urn:recordtime"), Literal(str(str(datetime.now())[:-8]) + "0")))
    g.add((URIRef(tokens),URIRef(u"urn:useragent"),Literal(ua)))
    if ip:
        g.add((URIRef(tokens),URIRef(u"urn:ip"),Literal(ip)))
    g.add((URIRef(tokens),URIRef(u"urn:device"),Literal(device)))
    if os:
        g.add((URIRef(tokens),URIRef(u"urn:os"),Literal(os)))
    g.add((URIRef (tokens),URIRef(u"urn:browser"),Literal(browser)))
    try:
        insert(g)
    except Exception as e:
        print("error:",str(e)," could not insert graph into TDB")
        return e
    else:
        return False

async def app(scope, receive, send):

    assert scope['type'] == 'http'
    tokens = await read_tokens(receive)
    headers_ = scope['headers']
    ua,ip = "",""
    for i in headers_:
        if not ua:
            if i[0].decode("utf-8") == "user-agent":
                ua = i[1].decode('utf-8')
        if not ip:
            if i[0].decode('utf-8') in ['host','X-Real-Ip']:
                ip = i[1].decode('utf-8')
    device, os, browser = ua_paser_str(ua)
    #isp, location = ip_to_isp_loc(ip)    
    res = init_graph(tokens,ip,device,os,browser,ua)
    if not res:
        await send({
            'type': 'http.response.start',
            'status': 204
        })
        await send({
            'type':'http.response.body'
        })
    else:
        await send({
            'type':'http.response.start',
            'status':200,
        })
        await send({
            'type':'http.response.body',
            'Content-Length':str(len(str(res))),
            'body':(str(res)).encode('utf-8')
        })

if __name__ == "__main__":
    port = sys.argv[1]
    if port:
        uvicorn.run(app=app,host=HOST,port=int(port),debug=DEBUG_MODE,log_level=LOG_LEVEL)
        print("startind server...")