import sys

'''
from utils.utils import genera_uuid
from utils.utils import ua_paser_str
from utils.utils import ip_to_isp_loc
from utils.utils import generate_random_str
'''

from flask import render_template

from utils.utils import ua_paser_str

import config

from serv_method import pase_headers, init_graph, fuseki_squery_cmd, fuseki_sget_cmd

import uvicorn

from jinja2 import Environment, FileSystemLoader
from urllib.parse import unquote, parse_qsl
debug = config.DEBUG_MODEL


HOST = "0.0.0.0"
DEBUG_MODE = False
LOG_LEVEL  = "debug"

async def uvicorn_render_template(send,body_file,**context):

    env = Environment(loader=FileSystemLoader("./"))
    template = env.get_template(body_file)

    content = template.render(**context)
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/html'],
        ]
    })
    await send({
        'type': 'http.response.body',
        'headers': [
            [b'content-type', b'text/html'],
        ],
        'body': content.encode('utf-8'),
    })

async def read_tokens(receive):
    body = b""
    more_body = True
    while more_body:
        message = await receive()
        body = message.get('body',b'')
        more_body = message.get('more_body',False)
    tokens = body.decode("utf-8")
    return tokens

async def trackingsite_method(scope,receive,send):
    tokens = await read_tokens(receive)
    ua, ip = pase_headers(scope['headers'])
    device, os, browser = ua_paser_str(ua)
    # isp, location = ip_to_isp_loc(ip)
    res = init_graph(tokens, ip, device, os, browser, ua)
    if not res:
        await send({
            'type': 'http.response.start',
            'status': 204
        })
        await send({
            'type': 'http.response.body'
        })
    else:
        await send({
            'type': 'http.response.start',
            'status': 200,
        })
        await send({
            'type': 'http.response.body',
            'Content-Length': str(len(str(res))),
            'body': (str(res)).encode('utf-8')
        })

async def app(scope, receive, send):

    assert scope['type'] == 'http'
    if scope['method'] == 'GET':
        if scope['path'].lstrip("/") == 'sparql':
            if not scope['query_string']:
                await uvicorn_render_template(send,"template/sparql_search.html")
            else:
                qsld = dict(parse_qsl(scope['query_string']))
                if qsld[b'format'] == b'auto':
                    res = fuseki_squery_cmd(qsld[b'query'])
                elif qsld[b'format'] == b'text/turtle':
                    res = fuseki_sget_cmd()
                #await uvicorn_render_template(send, res)
                await send({
                    'type': 'http.response.start',
                    'status': 200,
                })
                await send({
                    'type': 'http.response.body',
                    'Content-Length': str(len(str(res))),
                    'body': res
                })
    if scope['method'] == 'POST':
        if scope['path'].lstrip("/") in ['pv','uv']:
            await trackingsite_method(scope,receive,send)

if __name__ == "__main__":
    port = sys.argv[1]
    if debug:
        if not port:
            port = 8001
    if port:
        uvicorn.run(app=app,host=HOST,port=int(port),debug=DEBUG_MODE,log_level=LOG_LEVEL)
        print("startind server...")