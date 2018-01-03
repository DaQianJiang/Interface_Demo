import xlwt
import os
import xlrd
from utils.log import Logger
from utils.config_reader import ROOT_PATH

excel_path = r'E:\PycharmProjects\interface_demo\data\login.xlsx'
EXCELPATH = os.path.join(ROOT_PATH,'data\login.xlsx')
class ExcelReaser(object):
    def __init__(self,excel,sheet=0,title = True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('excel文件未找到')
        self.sheet = sheet
        self.title = title
    #读取excel文件信息
    def get_excel_data(self):
        #打开文件，创建excel文件对象
        self.workbook = xlrd.open_workbook(excel_path)
        if type(self.sheet) not in [int,str]:
            raise ('sheetTypeErro')
        elif type(self.sheet)==int:
            self.s = self.workbook.sheet_by_index(self.sheet)
        else:
            self.s = self.workbook.sheet_by_name(self.sheet)

    def wirte_excel_data(self):
        writebook = xlwt