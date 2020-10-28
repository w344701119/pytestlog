
import json,time,http.client
from typing import Any

host ="127.0.0.1:3007"
def HttpPost(url,data):
    #dataUrlEncode = urllib.parse.urlencode(postData)
    # print(dataUrlEncode)
    data=json.dumps(data)
    try:
        conn = http.client.HTTPConnection(host)
    except Exception as e:
        print ("fail to connection:",e)
        return False
    header = {"Content-type": "application/json", "Accept": "text/plain"}
    try:
        conn.request("POST", url, data, header)
    except Exception as e:
        print("fail to request ",e)
        return False
    response = conn.getresponse()  # type: Any
    if response.status!=200:
        print("fail to request width http code:",response.status)
        return False
    res = response.read()
    resp = json.loads(res)
    return resp




