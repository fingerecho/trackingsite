import sys
import time

'''
from utils.utils import genera_uuid
from utils.utils import ua_paser_str
from utils.utils import ip_to_isp_loc
from utils.utils import generate_random_str
'''

from flask import render_template

from utils.utils import ua_paser_str

import config

from serv_method import pase_headers, init_graph, fuseki_squery_cmd, fuseki_sget_cmd, fuseki_squery_cmd_echarts, parse_upstream_nginx_conf_port
import uvicorn

from jinja2 import Environment, FileSystemLoader
from urllib.parse import unquote, parse_qsl
debug = config.DEBUG_MODEL


HOST = "0.0.0.0"
DEBUG_MODE = False

LOG_LEVEL  = "debug"

normal_res_st = {
    'type': 'http.response.start',
    'status': 200,
}
normal_res_ed = {
    'type': 'http.response.body',
}

async def uvicorn_render_template(send,body_file,content_type=b"text/html",**context):
    global normal_res_st, normal_res_ed
    env = Environment(loader=FileSystemLoader("./"))
    template = env.get_template(body_file)
    content = template.render(**context).encode('utf-8')
    content_length = str(len(content.decode('utf-8')))
    normal_res_st.update({
        'headers': [
            [b'content-type', content_type],
        ],
    })
    normal_res_ed.update({
        'headers': [
            [b'content-type', content_type],
        ],
        'body': content,
        #'Content-Length':content_length
        }
    )
    await send(normal_res_st)
    await send(normal_res_ed)

async def read_tokens(receive):
    body = b""
    more_body = True
    while more_body:
        message = await receive()
        body = message.get('body',b'')
        more_body = message.get('more_body',False)
    tokens = body.decode("utf-8").split("&")
    for token in tokens:
        if token.startswith("tokens"):
            tokens = token.lstrip("tokens=null")
            break
    if isinstance(tokens,list):
        tokens="localtime-"+str(time.time())
    return tokens

async def trackingsite_method(scope,receive,send):
    global  normal_res_st, normal_res_ed
    tokens = await read_tokens(receive)
    ua, ip = pase_headers(scope['headers'])
    device, os, browser = ua_paser_str(ua)
    # isp, location = ip_to_isp_loc(ip)
    #print(tokens, ip, device, os, browser, ua)
    res = init_graph(tokens, ip, device, os, browser, ua)
    if not res:
        normal_res_st.update({'status':200})
    else:
        normal_res_ed.update({
            'body': (str(res)).encode('utf-8'),
            #'Content-Length': str(len(str(res))),
        })
    await send(normal_res_st)
    await send(normal_res_ed)


async def app(scope, receive, send):
    global  normal_res_st
    assert scope['type'] == 'http'
    if scope['method'] == 'GET':
        if scope['path'].lstrip("/") in ['sparql','turtle']:
            if not scope['query_string']:
                await uvicorn_render_template(send,"template/sparql_search.html")
            else:
                qsld = dict(parse_qsl(scope['query_string']))
                if qsld[b'format'] == b'auto':
                    res = fuseki_squery_cmd(qsld[b'query'])
                    normal_res_st.update({'headers': [
                        [b'content-type', b'text/plain'],
                    ],})
                    normal_res_ed.update({'headers': [
                        [b'content-type', b'text/plain'],
                    ],})
                elif qsld[b'format'] == b'text/turtle':
                    res = fuseki_sget_cmd()
                    normal_res_st.update({'headers': [
                        [b'content-type', b'text/plain'],
                    ],})
                    normal_res_ed.update({'headers': [
                        [b'content-type', b'text/plain'],
                    ],})
                elif qsld[b'format'] == b'graph/echarts':
                    res = fuseki_squery_cmd_echarts(qsld[b'query'])
                    normal_res_st.update({'headers': [
                        [b'content-type', b'text/html'],
                    ],})
                    normal_res_ed.update({'headers': [
                        [b'content-type', b'text/html'],
                    ],})
                #await uvicorn_render_template(send, res)
                #res_length_ = str(len(str(res))) if isinstance(res, str) else str(len(str(res.decode('utf-8'))))
                res        = res.encode('utf-8') if isinstance(res, str) else res
                normal_res_ed.update({
                    'body': res,
                })
                await send(normal_res_st)
                await send(normal_res_ed)
        elif scope['path'].lstrip("/").split("/")[0] == 'static':
            await uvicorn_render_template(send, scope['path'].lstrip("/"),content_type=b"application/javascript")
        elif scope['path'].lstrip("/").split("/")[0] == "favicon.ico":
            await send(normal_res_st)
            await send(normal_res_ed)
        else:
            normal_res_st.update({"status":200})
            await send(normal_res_st)
            await send(normal_res_ed)
    if scope['method'] == 'POST':
        if scope['path'].lstrip("/") in ['pv','uv']:
            await trackingsite_method(scope,receive,send)

if __name__ == "__main__":
    port = sys.argv[1] if len(sys.argv) > 1 else None
    if debug:
        if not port:
            port = 8001
    if port:
        uvicorn.run(app=app,host=HOST,port=int(port),debug=DEBUG_MODE,log_level=LOG_LEVEL)
        print("startind  {port} server...".format(port=port))
    else:
        ports = parse_upstream_nginx_conf_port()
        for po_ in ports:
            uvicorn.run(app=app,host=HOST,port=int(po_),debug=DEBUG_MODE,log_level=LOG_LEVEL)


