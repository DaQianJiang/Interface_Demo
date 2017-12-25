import unittest
import json
import requests

class Sign_In_Test(unittest.TestCase):
    def setUp(self):
        self.url='http://www.senbaba.cn'
    # /addcustomer?username=DDQ&password=123456&phoneMsg=9896&phone=18408249437'
    def tearDown(self):
        print("注册测试完成")

    def test_phonenum_erro(self):
        data_param = {'username':'DDQ','password':'123456','phoneMsg':'9896','phone':'18408249437'}
        res = requests.get(self.url+r'/addcustomer',params=data_param)
        data_json = json.loads(res.text)
        #data_json = res.json()
        print('查看json数据：%s'%data_json)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data_json['status'],'failed')
        self.assertEqual(data_json['error']['code'],'failed')
        self.assertEqual(data_json['error']['msg'],'您手机的验证码错误或失效')