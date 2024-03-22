import os
import shutil
import sqlite3
import uuid
from datetime import datetime
import json
from multiprocessing.pool import ThreadPool

current_time = datetime.now()


# 复制文件夹并生成随机名称
def copy_folder(shared_folder, dest_folder):
    try:
        new_folder_name = str(uuid.uuid4())  # 生成随机名称
        new_folder_path = os.path.join(dest_folder, new_folder_name)
        print(new_folder_path)
        shutil.copytree(shared_folder, new_folder_path)
        return new_folder_name
    except Exception as e:
        print(f"Error occurred during folder copy: {e}")
        return None


# 插入数据到SQLite数据库
def insert_data(new_folder_name):
    try:
        db_path = r'\\172.18.132.18\base\basedb.db'
        base_dir = '/home/aoi/ais/projects/'
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        versions = {"list": {"1": {"1": "2024-03-08 09:47:54", "2": "2024-03-06 17:22:49", "3": "2024-03-11 20:49:28",
                                   "4": "2024-03-08 09:52:51", "edit": "2024-03-21 15:54:02",
                                   "xinlin": "2024-03-18 11:49:59"}}}
        cursor.execute(
            "INSERT INTO BaseDb (uuid, islocked,side,name, separator,modifyTime,modifyTimestamp,host,author,path,thumb,versions,createTime,modifyAuthor,lastOpenTime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (new_folder_name, 0, 1, new_folder_name, '.', '2024-03-21 21:47:36', 1711007642046, '127.0.0.1', 'admin',
             base_dir+new_folder_name, '/resource/metaData-thumb.png', json.dumps(versions), '2024-03-06 12:12:33', '',
             '2024-03-20 15:32:52'))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error occurred during data insertion: {e}")


# 主函数
def main():
    shared_folder = r'\\172.18.132.18\test16.1'
    dest_folder = r'\\172.18.132.18\projects'
    num_threads = 1  # 设置线程数

    # 创建线程池
    pool = ThreadPool(num_threads)

    # 复制文件夹并生成随机名称
    copy_results = pool.apply_async(copy_folder, (shared_folder, dest_folder))

    # 获取复制结果
    copy_result = copy_results.get()
    if copy_result is not None:
        new_folder_name, new_folder_path, shared_folder = copy_result

        # 插入数据到SQLite数据库
        pool.apply_async(insert_data, (new_folder_name, new_folder_path))

    # 关闭线程池
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
