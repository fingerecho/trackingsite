import sys
sys.path.append("..")

from serv_method import init_graph, parse_upstream_nginx_conf_port, fuseki_squery_cmd, fuseki_squery_cmd_echarts
import unittest


class MyTestCase(unittest.TestCase):
    def test_init_graph(self):
        tokens = "AHW5MfBGNffWrmMmia7hb3KmFCttGrQe"
        ip="gitee.fyping.cn: 65533"
        device="Firefox"
        browser="Mozilla / 5.0(X11"
        os="Ubuntu Linux x86_64"
        ua="rv: 68.0) Gecko / 20100101 Firefox / 68."
        res = init_graph(tokens, ip, device, os, browser, ua)
        import time
        print("res:",res,"\nlocaltime:",time.time())
        self.assertEqual(False, res)
    def test_parse_upstream_nginx_conf_port(self):
        res_ports = parse_upstream_nginx_conf_port()
        self.assertEqual(True,True if len(res_ports) > 0 else False)
    def test_fuseki_squery_cmd(self):
        qs = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix urn: <http://fliqz.com/>
        select * where { ?id ?p ?s} 
        """
        qs = '''
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix urn: <http://fliqz.com/>
        select * where { <https://fangself.com.cn/trackingsite/nullA3pW7zPRawRniT7ZA3Fz48EDFCTFkp2H> ?p ?s}
        '''
        rs = fuseki_squery_cmd(qs)
        print("rs:",rs)
        self.assertEqual(False,isinstance(rs,Exception))

if __name__ == '__main__':
    unittest.main()
