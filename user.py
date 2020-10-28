import time
import common.common

#updateUserInfo();
def updateUserInfo():
    nowTime=time.time()
    url="/api/updateuserinfo"
    reqData={
        'buildVersion'  :'9111ccc',
        'channel'       :'1024',
        'mac'           :'6C:C7:EC:A8:01:9A',
        'model'         :'SM-N960F',
        'sn'            :'3094062',
        'softVersion'   :'26100',
        'uuid'          :'e9ce08094a8a41029ebc490a3d84bde4',
        'vendorID'      :'3094062rttt',
        'wifiMac'       :'6C:C7:EC:A8:01:9E',
        'pkgName'       :'com.vooco.yashitv',
        'ipAddr'        :'192.168.1.199',
        'chipId'        :'40034b97',
        'phoneNum'      :'18344043066',
        'type'          :1,
        'platformType'  :2,
        'timestamp'     :str(nowTime)
    }
    resp=common.common.HttpPost(url,reqData)
    if resp["code"]==0 :
        print ("success to request")
    else:
        print("fail to request")
if __name__=="__main__":
    updateUserInfo()