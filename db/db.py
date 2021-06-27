import pymysql
import threading
import time



host = 'localhost'
port = 3306
db = 'hd_server_local'
user = 'root'
password = '1'


# ---- 用pymysql 操作数据库
def get_connection():
    conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password)
    return conn

def insert_log(logparm):
    time = logparm[0]
    device = logparm[1]
    type = logparm[2]
    logMessage = logparm[3]
    details = logparm[4]
    conn = get_connection()
    cursor = conn.cursor()
    sql = """INSERT INTO log(time, device, type, logMessage, details)
         VALUES (%s, %s, %s, %s, %s)"""
    # now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    param = (time, device, type, logMessage, details)
    try:
        cursor.execute(sql, param)
        conn.commit()
    except:
        conn.rollback()
    conn.close()



def check_it():
    conn = get_connection()
    # 使用 cursor() 方法创建一个 dict 格式的游标对象 cursor
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select count(type) as total from log")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("-- 当前数量: %d " % data['total'])
    # 关闭数据库连接
    cursor.close()
    conn.close()


if __name__ == '__main__':
    test = ['2021/02/25 02:49:47.36', 'SW1', 'Info', '02/25/2021 02:49:47.36 <Info:vlan.dbg.info> Media 1000T is removed from Port 25', '{"time": "02/25/2021 02:49:47.36", "type": "Info:vlan.dbg.info", "Media": "1000T", "action": "remove", "port": "25"}']
    insert_log(test)