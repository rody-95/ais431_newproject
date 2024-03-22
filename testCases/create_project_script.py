import paramiko
import sqlite3
# SSH连接信息
hostname = '172.18.132.18'
port = 22
username = 'aoi'
password = 'aoi2014'

# 建立SSH连接
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port, username, password)

# 执行脚本
command = '''
#!/bin/bash
# 复制文件夹并生成随机名称
auth=$(uuidgen)
shared_folder="/home/aoi/ais/projects/test16.1"
dest_folder="/home/aoi/ais/projects/"
#获取新路径
cp -r "$shared_folder" "$dest_folder/$auth"


# 插入数据到SQLite数据库
db_path="/home/aoi/ais/base/basedb.db"
versions='{"list": {"1": {"1": "2024-03-08 09:47:54", "2": "2024-03-06 17:22:49", "3": "2024-03-11 20:49:28", "4": "2024-03-08 09:52:51", "edit": "2024-03-21 15:54:02", "xinlin": "2024-03-18 11:49:59"}}}'
modify_time=$(date +"%Y-%m-%d %H:%M:%S")
create_time=$(date +"%Y-%m-%d %H:%M:%S")
modify_author=""
last_open_time=$(date +"%Y-%m-%d %H:%M:%S")

sqlite3 "$db_path" <<EOF
INSERT INTO BaseDb (uuid, islocked, side, name, separator, modifyTime, modifyTimestamp, host, author, path, thumb, versions, createTime, modifyAuthor, lastOpenTime)
VALUES ('$auth', 0, 1, '$auth', '.', '$modify_time', $(date +%s%3N), '127.0.0.1', 'admin', '$dest_folder/$auth', '/resource/metaData-thumb.png', '$versions', '$create_time', '$modify_author', '$last_open_time');
EOF

'''

stdin, stdout, stderr = client.exec_command(command)

# 循环执行脚本N次
for _ in range(3):
    stdin, stdout, stderr = client.exec_command(command)
    # 输出执行结果
    print(stdout.read().decode())
    print(stderr.read().decode())

# 关闭SSH连接
client.close()
# 关闭SSH连接
client.close()
