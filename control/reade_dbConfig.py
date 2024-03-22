import configparser
import os

config = configparser.ConfigParser()
root_dir = os.path.dirname(os.path.abspath('.'))  # 获取当前文件所在目录的上一级目录
db_dir = config.read(root_dir + "\\config\\vitrual_aoi_host.ini", "utf8")  # 拼接文件路径读取db配置文件


# 获取[鑫林]的host
def get_section(section):
    data1 = config.get(section, "host")
    return data1


if __name__ == "__main__":
    print(get_section('DB_Connect'))
