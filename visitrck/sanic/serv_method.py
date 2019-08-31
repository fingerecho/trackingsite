
from time import ctime,time
from datetime import datetime
from rdflib import Graph, Literal, URIRef, term
from database.rdf import insert

from subprocess import run, PIPE

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


