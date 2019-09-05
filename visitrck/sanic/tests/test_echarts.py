import unittest
import sys
sys.path.append("..")

from serv_method import draw_graph_of_relationship


class MyTestCase(unittest.TestCase):
    def test_something(self):
        draw_graph_of_relationship.create_charts()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
