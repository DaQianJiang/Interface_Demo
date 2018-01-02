import unittest
import os
from utils.config_reader import ROOT_PATH
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.mail import Email

report_name = os.path.join(ROOT_PATH,'report\\report.html')
print('testrunner',ROOT_PATH)
fp = open(report_name,'wb')
case_path = os.path.dirname(os.path.abspath('.'))+r'\case'
suite = unittest.TestLoader().discover(case_path)
if __name__=="__main__":

    #runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(stream=fp,verbosity=2,title='接口测试报告',description='网站接口')
    runner.run(suite)
    email = Email(server='smtp.qq.com',
                  sender='1404482005@qq.com',
                  reveicer='1404482005@qq.com',
                  password='txtsoccqguvxhaca',
                  path=report_name,
                  message='接口测试报告',
                  title='测试报告发送'
    )
    email.send()
