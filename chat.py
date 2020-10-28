#!/usr/bin/python3
import  json,sys,os
from typing import Any

param=sys.argv
fileName=param[1].strip()
destName=param[2].strip()
if fileName=="" :
    print("请输入要读取的文件\n")
    exit(0)
if destName=="":
    print ("请输入存放文件的目录\n")
    exit(0)
#或存放目录
p=destName.rfind("/")
destDir=destName[0:p]
b=os.path.exists(destDir)
if b==False:
    try:
        os.mkdir(destDir,777)
    except Exception as e:
        print("创建目标目录失败\n")
        exit(0)
# fileName="./tb_chat_201807.json"
# destName="./chat.txt"
fileObj= open(fileName,mode='r', encoding='utf-8')  # type: Any
destObj= open(destName,mode="a+",encoding='utf-8')  # type: Any
##循环遍历
for row in fileObj:
    row = row.strip()
    if row != "":
        try:
            json_data = json.loads(row)
            destObj.write(json_data["source"].strip() + "\n")
        except Exception as e :
            print(e)
            continue
#关闭文件
fileObj.close()
destObj.close()





