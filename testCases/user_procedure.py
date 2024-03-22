import pymysql

# 连接数据库
conn = pymysql.connect(
    host='172.18.132.18',
    port=3306,
    user='root',
    password='aoi2014',
    database='AoiUserManager'
)

# 创建存储过程
create_procedure_query = '''
CREATE PROCEDURE insert_user_data()
BEGIN
    DECLARE counter INT DEFAULT 1;
    WHILE counter <= 500 DO
        SET @user_name = CONCAT('user', counter);
        SET @user_real_name = CONCAT('Real Name', counter);
        SET @user_pwd = CONCAT('password', counter);
        SET @user_role = CONCAT('role', counter);
        SET @user_phone = CONCAT('phone', counter);

        INSERT INTO tb_user (user_name, user_real_name, user_pwd, user_role, user_phone)
        VALUES (@user_name, @user_real_name, @user_pwd, @user_role, @user_phone);

        SET counter = counter + 1;
    END WHILE;
END
'''

# 执行创建存储过程的SQL语句
with conn.cursor() as cursor:
    cursor.execute(create_procedure_query)

# 调用存储过程插入数据
with conn.cursor() as cursor:
    cursor.callproc('insert_user_data')
    conn.commit()
# 查询tb_user表
query = "SELECT COUNT(*) FROM AoiUserManager.tb_user"

# 执行查询语句
with conn.cursor() as cursor:
    cursor.execute(query)
    result = cursor.fetchone()
# 打印查询结果
print(f"tb_user表的行数：{result[0]}")
# 关闭数据库连接
conn.close()
