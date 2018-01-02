import  yaml
import os

ROOT_PATH = os.path.split(os.path.dirname(os.path.abspath('.')))[0]
CONFIG_PATH = r'E:\PycharmProjects\interface_demo\config\config.yaml'
#CONFIG_PATH = os.path.join(ROOT_PATH,'config\config.yaml')
class YmalReader(object):
    def get_value(self,element):
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH,'rb') as f:
                self.vaulList = yaml.load(f).get(element)
           # print(self.vaulList)
            return self.vaulList
        else:
            raise FileNotFoundError("配置文件不存在")
# if __name__ =="__main__":
#     y = YmalReader()
#     f_data = y.get_value('mail')
#     print(f_data)
#     f_data1 = y.get_value('logger')
#     print(f_data1)


