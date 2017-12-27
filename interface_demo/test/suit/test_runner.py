import unittest
import os
from utils.log import ROOT_PATH
from utils.HTMLTestRunner_PY3 import HTMLTestRunner

report_name = os.path.join(ROOT_PATH,'report\\report.html')
fp = open(report_name,'wb')
case_path = os.path.dirname(os.path.abspath('.'))+r'\case'
suite = unittest.TestLoader().discover(case_path)
if __name__=="__main__":

    #runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(stream=fp,verbosity=2,title='接口测试报告',description='网站接口')
    runner.run(suite)
