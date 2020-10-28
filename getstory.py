#/usr/bin/python3
import re,urllib.request

regx=re.compile("([\u4E00-\u9FFF]+.*[\u4E00-\u9FFF]+\s?。\s?.*[\u4E00-\u9FFF》])")
saveFile="./data/story.txt"
fileObj=open(saveFile,"a")
pattern = re.compile(r'<[^<|^>]+>',re.S)
for i in range(100):
    reqUrl = "https://so.gushiwen.cn/mingju/default.aspx?p="+str(i)
    req = urllib.request.urlopen(reqUrl)
    result=req.read().decode("UTF-8")
    result = pattern.sub('', result)
    lines=regx.findall(result)
    if lines=="":
        print("err page=",i)
    else:
        for line in lines:
            line
            fileObj.write(line.strip()+"\n")
fileObj.close()





