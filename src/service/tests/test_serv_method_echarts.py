#!/
import unittest
import sys
import json
sys.path.append("..")
from serv_method import fuseki_squery_cmd_echarts


class MyTestCase(unittest.TestCase):
    def test_echarts(self):
        prefix = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        prefix urn: <http://fliqz.com/>
        
        """
        qs = "select  *  where { ?s ?o ?b }"
        qs = prefix + qs
        qs = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\r\nprefix urn: <http://fliqz.com/>\r\n\r\nselect * where { ?id ?p ?s}\r\n\t\t\t """
        res_ = fuseki_squery_cmd_echarts(qs)
        #res = json.loads(res_)
        #tar = res_.render_embed()
        print("res_:",type(res_),res_) #"\ntar:",type(tar))#,tar)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
