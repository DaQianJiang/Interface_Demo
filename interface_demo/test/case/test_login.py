import requests
import unittest

class Login_In_Test(unittest.TestCase):

    def setUp(self):
        self.count = 0
        self.url='http://www.senbaba.cn/'
    @classmethod
    def tearDownClass(cls):
        #cls.count+=1
        print("登录测试test完成")

    #测试密码错误 http://www.senbaba.cn/login?uname=18408249437&pwd=11111
    def test_username_erro(self):
        data_param={'uname':'1840xxxx37','pwd':'11111'}
        res = requests.get(self.url+r'/login',params=data_param)
        result=res.json()
        self.assertEqual(res.status_code,200)
        self.assertEqual(result['status'],'failed')
        self.assertEqual(result['error']['msg'],"用户名或密码错误")
    def test_password_erro(self):
        data_param = {'uname':'184xxxx','pwd':'123456'}
        res = requests.get(self.url+r'/login',params=data_param)
        result = res.json()
        self.assertEqual(res.status_code,200)
        self.assertEqual(result['status'],'failed')
        self.assertEqual(result['error']['msg'],"用户名或密码错误")

    def test_infom_right(self):
        data_param = {'uname':'184xxx437','pwd':'123456'}
        res = requests.get(self.url+r'/login',params=data_param)
        result = res.json()
        self.assertEqual(res.status_code,200)
        self.assertEqual(result['status'],'ok')
        self.assertEqual(result['data']['user']['customerName'],"DDQ")
        self.assertEqual(result['data']['user']['contactNo'], "18408249437")


