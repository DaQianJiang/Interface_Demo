import logging
import os
from  logging.handlers import TimedRotatingFileHandler
import time
from  utils.config_reader import YmalReader,ROOT_PATH

#ROOT_PATH = os.path.split(os.path.dirname(os.path.abspath('.')))[0]
LOGGER_PATH = os.path.join(ROOT_PATH,'log')
#print(os.path.split(os.path.dirname(os.path.abspath('.'))))
class Logger(object):
    def __init__(self,logger_name):
        self.yaml_reader = YmalReader().get_value('logger')
        #获取配置文件信息
        try:
            self.console_level = self.yaml_reader.get('console_level')
            self.file_level = self.yaml_reader.get('file_level')
            self.fmt = self.yaml_reader.get('%Y-%m-%d:%H:%M:%S')
            self.when = self.yaml_reader.get('when')
        except:
            raise ('获取配置文件信息失败')

        nowtime = time.strftime('%Y%m%d')
        self.file_name = os.path.join(LOGGER_PATH,nowtime+r'.log')
        #print(self.file_name)
        self.logger = logging.getLogger(logger_name) #创建一个logger对象
        self.logger.setLevel(logging.DEBUG) #设置日志级别为debug,则比debug级别高的都能输出

        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(self.console_level) #比debug低的日志级别忽略不输出
        self.file_handler = TimedRotatingFileHandler(self.file_name,when='D',interval=1,delay=False,encoding='utf-8')
        self.file_handler.setLevel(self.file_level)
        self.formatter = logging.Formatter(fmt="%(asctime)s%(filename)s[line:%(lineno)d]%(levelname)s-%(message)s",
                                           datefmt='%Y-%m-%d:%H:%M:%S')
    def get_logger(self):
        self.console_handler.setFormatter(self.formatter)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.console_handler)
        self.logger.addHandler(self.file_handler)
        return self.logger
if __name__=="__main__":
    log1 = Logger('test_logger').get_logger()
    log1.debug("debuge")
    log1.warning("woring")
    log1.info("info")

