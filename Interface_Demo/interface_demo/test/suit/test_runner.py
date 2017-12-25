import unittest
import os
#from test.case.sign_in_test import Sign_In_Test

case_path = os.path.dirname(os.path.abspath('.'))+r'\case'
#print(case_path)
suite = unittest.TestLoader().discover(case_path)
if __name__=="__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)
