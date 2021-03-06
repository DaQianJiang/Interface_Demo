import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.log import Logger
import os
import re
from utils.config_reader import YmalReader

class Email(object):
    logger = Logger('mail').get_logger()
    yaml_reader = YmalReader().get_value('mail')
    def __init__(self,path):
        self.server = self.yaml_reader.get('server')
        self.sender = self.yaml_reader.get('sender')
        self.reveicer = self.yaml_reader.get('reveicer')
        self.password = self.yaml_reader.get('password')
        self.message = self.yaml_reader.get('message')
        self.title = self.yaml_reader.get('title')
        self.path = path
        self.msgRoot = MIMEMultipart('related') #创建MIMEMultipart对象

    def upload_file(self,file):
        if os.path.isdir(file):
            for f in os.listdir(file):
                self.file_path = os.path.join(file,f)
                if f.endswith(('.xlsx','.xls','.py')):
                    self.msgFile = MIMEText(open(self.file_path,'rb').read(),"base64","utf-8")
                else:
                    self.msgFile = MIMEText(open(self.file_path).read(),"utf-8")
                self.msgFile["Content-Type"] = 'application/octet-stream'
                self.msgFile["Content-Disposition"] = 'attachment; filename=' + f
                self.msgRoot.attach(self.msgFile)
                self.logger.info("upload file {} is".format(self.file_path))
        elif os.path.isfile(file):
            self.fname = re.split(r'[\\|/]',file)
            if self.fname[-1].endswith(('.xlsx','.xls','.py')):
                self.msgFile = MIMEText(open(file,'rb').read(),"base64","utf-8")
            else:
                self.msgFile = MIMEText(open(file,'r',encoding="utf-8").read())
            self.msgFile["Content-Type"] = 'application/octet-stream'
            self.msgFile["Content-Disposition"] = 'attachment; filename=' + self.fname[-1]
            self.msgRoot.attach(self.msgFile)
            self.logger.info("upload file {} is".format(file))
        else:
            raise ("路径不合法或文件不存在")

    def send(self):
        self.msgRoot['From'] = self.sender
        self.msgRoot['To'] = ','.join(self.reveicer) #用,将list中的每一项连接
        self.msgRoot['Subject'] = self.title

        if self.path:
            if isinstance(self.path,list):
                for f in self.path:
                    self.upload_file(f)
            elif isinstance(self.path,str):
                self.upload_file(self.path)
            else:
                raise("配置文件格式错误")
        try:
            stmp_server = smtplib.SMTP_SSL(self.server,465)
            stmp_server.set_debuglevel(1)
        except smtplib.SMTPConnectError as e:
            self.logger.warning("服务器连接失败%"%e)
        else:
            try :
                stmp_server.login(self.sender,self.password)
            except smtplib.SMTPAuthenticationError as e:
                self.logger.warning("服务器登录失败%s"%e)
            else:
                try:
                    stmp_server.sendmail(self.sender,self.reveicer,self.msgRoot.as_string())
                    stmp_server.quit()
                    self.logger.info('发送邮件"{0}"成功!收件人"{1}"如果未收到邮件请检查垃圾箱或确认'
                                     '邮件地址是否正确'.format(self.title, self.reveicer))
                except smtplib.SMTPException as e:
                    self.logger.warning("邮件发送失败：%s"%e)
                    raise "邮件发送失败"
# if __name__=="__main__":
#     report = r'E:\PycharmProjects\interface_demo\report\report.html'
#     email = Email(server='smtp.qq.com',
#                   sender='1404482005@qq.com',
#                   reveicer='1404482005@qq.com',
#                   password='txtsoccqguvxhaca',
#                   path=report,
#                   message='接口测试报告',
#                   title='测试报告发送'
#     )
#     email.send()





