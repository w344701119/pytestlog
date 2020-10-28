import mysql.connector
##数据库配置
db_host="172.16.0.200"
db_user="root"
db_pwd="709394"
db_databases="channel"
db_port="3306"
##数据库配置
try:
    dbConn = mysql.connector.connect(host=db_host,user=db_user,password=db_pwd,database=db_databases,port=db_port)
    dbCursor = dbConn.cursor(dictionary=True)
except Exception as e:
    print ("fail to connect ",e)
    exit()
sqlStr="SELECT id,`sort` FROM `channel_channel_release` ORDER BY `sort` ASC"
dbCursor.execute(sqlStr)
rows = dbCursor.fetchall()  # fetchall() 获取所有记录
fileObj=open("./update.sql","a+")
reArr=[]
sqlForm="UPDATE vo_channel  SET sort_id={0} WHERE temp_id={1};"
for row in rows:
    reSql=sqlForm.format(row["sort"],row["id"])
    reArr.append(reSql)
fileObj.write("\n".join(reArr))
fileObj.close 
dbConn.close()