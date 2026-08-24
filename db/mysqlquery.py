import pymysql
conn = pymysql.connect(host='localhost', port=6033, user='root', password='1qaz@wsx', 
charset='utf8mb4', database='pythondb') # 連結資料庫

 
with conn.cursor() as cursor:
    sql = "select * from scores"
    cursor.execute(sql)
    datas = cursor.fetchall()     # 取出所有資料
    print(datas)
    print('-' * 30)               # 畫分隔線

    sql = "select * from scores"
    cursor.execute(sql)
    data = cursor.fetchone()      # 取出第一筆資料
    print(data)    

    conn.close()