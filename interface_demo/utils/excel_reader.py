import xlwt
from xlutils.copy import copy
import os
import xlrd
from utils.log import Logger
from utils.config_reader import ROOT_PATH

excel_path = r'D:\python\PycharmProjects\interface_demo\data\login.xlsx'
EXCELPATH = os.path.join(ROOT_PATH,'data\login.xlsx')
class ExcelReaser(object):
    #logger = Logger('excel_reade').get_logger()
    def __init__(self,excel,sheet=0,title = True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('excel文件未找到')
        self.sheet = sheet
        self.title = title
        self.data = list()
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
        if self.title:
            head_title = self.s.row_values(0)
            for row in range(1,self.s.nrows):
                #data为list类型
                self.data.append(dict(zip(head_title,self.s.row_values(row))))
        else:
            for row in range(0,self.s.nrows):
                self.data.append(self.s.row_values(row))
       # self.logger.info('excel数据读取成功')
        return self.data

    def wirte_excel_data(self,value_data):
        #打开文件，并且按原格式
        self.rbook = xlrd.open_workbook(excel_path)
        self.wbook = copy(self.rbook)
        self.r_sheet = self.rbook.sheet_by_index(self.sheet)
        self.w_sheet = self.wbook.get_sheet(self.sheet)
        clo_num = self.r_sheet.ncols
        row_num = self.r_sheet.nrows
        for row in range(1,row_num):
            self.w_sheet.write(row,clo_num-2,value_data)
        self.wbook.save(excel_path)

if __name__=="__main__":
    excel = ExcelReaser(excel_path)
    excel.wirte_excel_data(['1','2','3'])
    excel_data = excel.get_excel_data()
    print(excel_data)
