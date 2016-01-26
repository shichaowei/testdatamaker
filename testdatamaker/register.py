#coding:utf-8
'''
Created on 2015-11-10

@author: Administrator
'''

import json
import httplib, urllib
import time
 
 
def register(datatemp):
    data_string = json.dumps(datatemp) 
    print data_string
    httpClient = None
    try:
        '''
        params = urllib.urlencode({'name': 'tom', 'age': 22})
        print params
        '''
        headers = {"Content-type": "application/json"
                        , "Accept": "application/json"}
     
        httpClient = httplib.HTTPConnection("192.168.1.251", 5000, timeout=30)
        httpClient.request("POST", "/user/register", data_string, headers)
     
        response = httpClient.getresponse()
        resulttemp=response.read()
        resulttemp=json.dumps(json.loads(resulttemp,encoding='utf-8'),ensure_ascii = False,indent=1)
        return resulttemp+'\n'
    except Exception, e:
        print 'register is failed error is %s'%e
    finally:
        if httpClient:
            httpClient.close()
            
if __name__=="__main__":
    datatemp={"mobile":"17000000001","msgcodeid":"244ee18b-2e51-40c9-9bde-31875fb8b711",\
              "msgcode":"73917","passwd":"123456","secretkey":"12345678"}
    
    resulttemp=register(datatemp)
    print resulttemp
    

    