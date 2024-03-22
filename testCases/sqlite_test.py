import sqlite3

# 连接网络上的SQLite数据库
db_path = r'\\172.18.132.18\base\basedb.db'  # 共享文件夹的完整路径
conn = sqlite3.connect(db_path)

# 执行SQL查询或操作
cursor = conn.cursor()
cursor.execute("SELECT * FROM BaseDb")
results = cursor.fetchall()

# 输出查询结果
for row in results:
    print(row)

# 关闭数据库连接
conn.close()
