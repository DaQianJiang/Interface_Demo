import requests
import unittest
import json

class Get_Event_List_Test(unittest.TestCase):
    def setUp(self):
        self.url='http://127.0.0.1:8000/api/get_event_list/'
    def tearDown(self):
        print("测试完成")

    #测试用户名为空
    def test_get_event_parameter_null(self):
        data1={'eid':'','name':''}
        res = requests.get(self.url,data1)
        result=res.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],"parameter error")

    def test_get_event_eid_null(self):
        data1={'eid':'1'}
        res = requests.get()


