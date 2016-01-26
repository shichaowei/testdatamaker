#coding:utf-8
'''
Created on 2015-11-10

@author: weishichao

'''

import json
import storeresult
import httplib, urllib
import time
import login
import storeresult
import sys
import fileupload
import postsql
import multiprocessing

reload(sys)
sys.setdefaultencoding('utf-8')

 
def auth(datatemp): 
    data_string = json.dumps(datatemp)
    httpClient = None
    try:
        headers = {"Content-type": "application/json"
                        , "Accept": "application/json"}
     
        httpClient = httplib.HTTPConnection("192.168.1.251", 5000, timeout=30)
        httpClient.request("POST", "/user/auth", data_string, headers)
     
        response = httpClient.getresponse()
        resulttemp=response.read()
        return resulttemp    
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

        
def testwork(uid,token,userpic,username,idcardpic1,idcardpic2,\
             drivercardpic1,drivercardpic2,cardtype,cardno,secretkey):
    params={'uid':uid,'token':token,'userpic':userpic,\
           'username':username,'idcardpic1':idcardpic1,'idcardpic2':idcardpic2,"drivercardpic1":drivercardpic1,\
           'drivercardpic2':drivercardpic2,'cardtype':cardtype,'cardno':cardno,'secretkey':secretkey}
    print params
    try:
        resultupload=auth(params)
        print resultupload
        resultuploaddic=json.loads(resultupload)    #json to dic
        resultmes=resultuploaddic["resultMessage"]
        resultcode=resultuploaddic["resultCode"]
    except Exception,err:
        print "测试 %s failed，参数有问题"%(testmes)
        print err
        return err
    try:
        assert  resultcode==200
    except AssertionError, err:
        print " is failed"%uid

           

 
def authwork(temp):
    try:
        i=temp
        qian=i/1000
        bai=i/100%10
        shi=i/10%10
        ge=i%10
        mobile='1700000'+str(qian)+str(bai)+str(shi)+str(ge)
        print mobile
    
        #先登录拿到token值
        logindatatemp={"mobile":mobile,"passwd":"123456","secretkey":"12345678"}
        loginresult=login.login(logindatatemp)
        loginresdic=json.loads(loginresult)    #json to dic
        
        logintokentemp=loginresdic['token']
        logintoken=str(logintokentemp)
        loginuid=str(loginresdic['userinfo']['uid'])
        

        resultpicall=[]
        fuploaduid=loginuid
        fuploadtoken=logintoken
        tertype=1
        secrekey='12345678'
        filedir=r'F:\test\edn-test\edn-test\testinterface\idcardpic1.jpg'
        params={'uid':str(fuploaduid),'token':str(fuploadtoken),'terminalType':str(tertype),\
               'file':open(filedir,"rb"),'secretkey':str(secrekey)}
        

        for i in range(1,6):
            try:
                resultpic=fileupload.uploadpic(params)
                resultpicdic=json.loads(resultpic)    #json to dic
                resultmes=resultpicdic["fid"]
                print resultmes
                resultpicall.append(resultmes)
            except Exception,e:
                print "fileupload failed error is %s"%e

        

        authuid=loginuid
        authtoken=logintoken
        secretkey='12345678'
        #postsql.executesql("delete from edn_user_auth where create_user='18667046248'")
        try:
            testwork(uid=authuid, token=authtoken, userpic=resultpicall[4],\
                     username='魏士超',\
                     idcardpic1=resultpicall[0],\
                     idcardpic2=resultpicall[1],\
                     drivercardpic1=resultpicall[2],\
                     drivercardpic2=resultpicall[3],\
                     cardtype=1, cardno='410581165896524580', secretkey=secretkey)
        except Exception,e:
            print "testwork failed error is %s"%e
    except Exception,e:
        print e              
       
if __name__=="__main__":
    '''
    #普通模式
    record=[]
    for i in range(1,2):
        process=multiprocessing.Process(target=authwork,args=(i,))
        process.start()
        record.append(process)
    for process in record:
        process.join(30)
    '''
    #多进程使用进程池
    pool = multiprocessing.Pool(processes = 4)
    for i in range(1,1000):
        pool.apply_async(authwork, (i,))   
    pool.close()
    pool.join()
        
    
    