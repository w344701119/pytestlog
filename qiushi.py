#/usr/bin/python3
import re,urllib.request,ssl
import unidecode as unidecode

saveFile="./data/qiushi.txt"
fileObj=open(saveFile,"a")
pattern = re.compile("<span>\s*.*\s*</span>")
headers ={
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
}
context = ssl._create_unverified_context()
for i in range(1):
    reqUrl = "https://www.qiushibaike.com/text/page/"+str(i+2)+"/"
    request = urllib.request.Request(reqUrl, headers=headers)
    req = urllib.request.urlopen(request,context=context)
    statusCode=req.getcode()
    print(statusCode)
    result=req.read().decode("UTF-8")
    lines=pattern.findall(result)
    if lines=="":
        print("err page=")
    else:
        for line in lines:
            line=line.replace("<br/>","\n")
            line = line.replace("</span>", "\r\n")
            line = line.replace("\u200b", "(图片)")
            line = re.sub("&[a-zA-Z0-9]+;", "(图片2)",line)
            line=line.lstrip("<span>").strip()
            #line=unidecode(str(line))
            if len(line)< 40:
                continue
            else:
                #print("=====================\n"+line+"("+str(len(line))+")\n=================================\n")
                try:
                    fileObj.write("=====================\n"+line+"("+str(len(line))+")\n=================================\n")
                except Exception as e:
                    print(line,e)
fileObj.close()



