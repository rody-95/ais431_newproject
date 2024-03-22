# 脚本项目，关键字驱动
# author = 'zhangXinLin'
一、环境依赖：
1.python3以上，标准库支持： 第三方依赖库：requests，openpyxl，allure
2.mySQL：版本建议_V5.0以上，依据实际情况而定，pymysql等
3.适用于windows/linux，linux需要额外配置环境及开发规范依据公司标准

二、工程目录解读：
###########目录结构及描述
├── config                                  # 配置目录
│       ├── dbConfig.ini                    # 配置文件，存放数据库常量数据
│       ├── log                             #日志配置模块
├── control                                 # 控制中心，用于管理模块的服务及配置
|       ├── reade_config.py                 # 封装了读取配置文件的模块
|       ├── reade_config.py                 # 封装了读取配置文件的模块
├── public                                  # 存放公共方法，便于统一维护
|       ├── dbConnect.py                    # 数据库连接池
|       ├── login.py                        # PC登录
├── reports                                 # 生成测试报告的目录地址
├── testCases                               # 存放测试用例，关键字驱动
├── tools                                   # 存放第三方工具
|       ├── allure                          # 配置allure报告
├── readme.md                               # 码前必读
├── runAll.py                               # 运行项目的所有测试用例


三、用前必读：
1.此项目用于自动化脚本