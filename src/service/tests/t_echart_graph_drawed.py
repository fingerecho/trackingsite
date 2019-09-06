from pyecharts import Page, Style
from pyecharts import Graph as EHGraph
from jinja2 import Template

import sys
sys.path.append("sanic")
from template.graph_echarts_render import template as custom_t

def say_hello():
    def cut_str(st):
        return "".join(st.split(" "))[-3:].strip("/").strip(":")
    def rend():
        result = {'head': {'vars': ['id', 'p', 's']}, 'results': {'bindings': [{'id': {'type': 'uri', 'value': 'https://fangself.com.cn/trackingsite/abcdefghijklmnopqrstuvwxyz'}, 'p': {'type': 'uri', 'value': 'urn:useragent'}, 's': {'type': 'literal', 'value': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}}, {'id': {'type': 'uri', 'value': 'https://fangself.com.cn/trackingsite/abcdefghijklmnopqrstuvwxyz'}, 'p': {'type': 'uri', 'value': 'urn:recordtime'}, 's': {'type': 'literal', 'value': '1567652403.8379083'}}, {'id': {'type': 'uri', 'value': 'https://fangself.com.cn/trackingsite/abcdefghijklmnopqrstuvwxyz'}, 'p': {'type': 'uri', 'value': 'urn:recordtime'}, 's': {'type': 'literal', 'value': '1567652403.7510242'}}, {'id': {'type': 'uri', 'value': 'https://fangself.com.cn/trackingsite/abcdefghijklmnopqrstuvwxyz'}, 'p': {'type': 'uri', 'value': 'urn:browser'}, 's': {'type': 'literal', 'value': 'Firefox'}}, {'id': {'type': 'uri', 'value': 'https://fangself.com.cn/trackingsite/abcdefghijklmnopqrstuvwxyz'}, 'p': {'type': 'uri', 'value': 'urn:device'}, 's': {'type': 'literal', 'value': ''}}]}}
        nodes = []
        links = []
        bindings  = result['results']['bindings']
        for bd in bindings:
            if bd[head[0]]['value'] != '' and bd[head[2]]['value'] != '':
                #bd[head[0]]['value'] = cut_str(bd[head[0]]['value'])
                #bd[head[2]]['value'] = cut_str(bd[head[2]]['value'])
                if bd[head[0]]['value'] not in cuts:
                    nodes.append({"name":bd[head[0]]['value'],'symbolSize':50,"value":1})
                    cuts.append(bd[head[0]]['value'])
                if bd[head[2]]['value'] not in cuts:
                    nodes.append({'name':bd[head[2]]['value'],'symbolSize':20,"value":2})
                    cuts.append(bd[head[2]]['value'])
                links.append({'source':bd[head[0]]['value'],'target':bd[head[2]]['value']})
        page = Page()
        style = Style(width=800,height=600)
        print(nodes,links)
        chart = EHGraph('relationship',**style.init_style)
        chart.add("", nodes, links, label_pos="right", graph_repulsion=50,
                  is_legend_show=False, line_curve=0.2, label_text_color=None)
        page.add(chart)
        page.render()
        js_markup = page.render_embed()
        with open("js_mk.html","w",encoding='utf-8') as f:
            f.write(js_markup)
        _template = Template(custom_t)
        resp = _template.render(__markup_custom=js_markup)
    rend()

if __name__ == "__main__":
    say_hello()
