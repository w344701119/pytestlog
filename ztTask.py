import mysql.connector

try:
    dbConn = mysql.connector.connect(host="localhost",user="root",passwd="709394",database="zentaopms",port="3306")
    dbCursor = dbConn.cursor(dictionary=True)
except Exception as e:
    print ("fail to connect ",e)
    exit()
dbCursor.execute("SELECT id,`name`,project FROM zt_task")
rows = dbCursor.fetchall()  # fetchall() 获取所有记录
print(rows)
for row in rows:
    print (row["name"].strip())

dbConn.close()