
import json
from time import ctime,time
from datetime import datetime
from rdflib import Graph, Literal, URIRef, term
from database.rdf import insert
from pyecharts import Page, Style
from pyecharts import  Graph as EHGraph
from subprocess import run, PIPE
from jinja2 import Template
#from flask import render_template
from template.graph_echarts_render import template as custom_t

import config
debug = config.DEBUG_MODEL
NAMESPACE_PREFIX = config.NAMESPACE_PREFIX

def pase_headers(headers_):
    ua, ip = "", ""
    for i in headers_:
        if not ua:
            if i[0].decode("utf-8") == "user-agent":
                ua = i[1].decode('utf-8')
        if not ip:
            if i[0].decode('utf-8') in ['x-real-ip','x-forwarded-for']:
                ip = i[1].decode('utf-8')
    return ua,ip


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

## fuseki
# usage:   `s-query --service=endpointURL 'query string'`
def fuseki_squery_cmd(qs,service=config.SPARQL_QUERY_URI,timeout=config.SPARQL_TIMEOUT):
    try:
        res = run(['{fuseki_base}/bin/s-query'.format(fuseki_base=config.FUSEKI_BASE),
                   '--service={endpointURL}'.format(endpointURL=service),
                   '{qs}'.format(qs=qs.decode('utf-8') if isinstance(qs,bytes) else qs )],stdout=PIPE,timeout=timeout)
    except FileNotFoundError as ffe:
        return "FileNotFoundError on fuseki_squery_cmd/serv_method.py %s"%(str(ffe))
    except Exception as ffe:
        return "Exception on fuseki_squery_cmd/serv_method.py %s"%(str(ffe))
    return res.stdout

# usage: ` s-get http://localhost:3030/dataset default `
def fuseki_sget_cmd(endpointURL=config.SPARQL_QUERY_URI,timeout=config.SPARQL_TIMEOUT):
    try:
        res = run(['{fuseki_base}/bin/s-get'.format(fuseki_base=config.FUSEKI_BASE),
                   '{endpointURL}'.format(endpointURL=endpointURL),
                   'default'],stdout=PIPE,timeout=timeout)
    except FileNotFoundError as ffe:
        return "FileNotFoundError on fuseki_squery_cmd/serv_method.py %s"%(str(ffe))
    except Exception as ffe:
        return "Exception on fuseki_squery_cmd/serv_method.py %s"%(str(ffe))
    return res.stdout

# usage:   `s-query --service=endpointURL 'query string'`
def fuseki_squery_cmd_echarts(qs,service=config.SPARQL_QUERY_URI,timeout=config.SPARQL_TIMEOUT):
    if isinstance(qs,bytes):
        qs = qs.decode("utf-8")
    try:
        res = run(['{fuseki_base}/bin/s-query'.format(fuseki_base=config.FUSEKI_BASE),
                   '--service={endpointURL}'.format(endpointURL=service),
                   '{qs}'.format(qs=qs if isinstance(qs,bytes) else qs )],stdout=PIPE,timeout=timeout)
        result = json.loads(res.stdout.decode('utf-8'))
        nodes = []
        links = []
        bindings  = result['results']['bindings']
        head = result['head']['vars']
        for bd in bindings:
            nodes.append({"name":bd[head[0]]['value'],'symbolSize':30,"value":1})
            nodes.append({'name':bd[head[2]]['value'],'symbolSize':10,"value":2})
            links.append({'source':bd[head[0]]['value'],'target':bd[head[2]]['value']})
        page = Page()
        style = Style(width=800,height=600)
        chart = EHGraph('relationship',**style.init_style)
        chart.add("", nodes, links, label_pos="right", graph_repulsion=50,
                  is_legend_show=False, line_curve=0.2, label_text_color=None)
        page.add(chart)
        page.render()
        js_markup = page.render_embed()
        #with open("js_mk.html","w",encoding='utf-8') as f:
        #    f.write(js_markup)
        _template = Template(custom_t)
        resp = _template.render(__markup_custom=js_markup)

    except FileNotFoundError as ffe:
        return "FileNotFoundError on fuseki_squery_cmd_echarts/serv_method.py %s"%(str(ffe))
    except Exception as ffe:
        return "Exception on fuseki_squery_cmd_echarts/serv_method.py %s"%(str(ffe))
    return resp


def parse_upstream_nginx_conf_port(filepath=config.NGINX_CONF_PATH):
    with open(filepath,"r",encoding='utf-8') as f:
        text_lines = f.readlines()
        ports = []
        start_index = -1
        end_index_alias = 0
        for line in text_lines:
            if "upstream trackingsite_uvicorn{" == line.strip("\n").strip(" "):
                while True:
                    end_index_alias += 1
                    if text_lines[text_lines.index(line)+end_index_alias].strip("\n").strip(" ") == "}":
                        break
                    ports.append(text_lines[text_lines.index(line)+end_index_alias].split("server")[-1].strip("\n").strip(" ").strip(";").split(":")[1])
        return ports


