#coding:utf-8
'''
Created on 2016��1��7��

@author: Administrator
'''
import register
import redis
import time
import multiprocessing

def setredispara(name,value):
    r=redis.Redis(host='192.168.1.251',port=6379,db=0)
    r.set(name,value)

def deleteredispara(name):
    r=redis.Redis(host='192.168.1.251',port=6379,db=0)
    r.delete(name)

def userfactory(i):
    try:
        redisname='msg#code#244ee18b-2e51-40c9-9bde-31875fb8b711'+str(i)
        msgcodeid='244ee18b-2e51-40c9-9bde-31875fb8b711'+str(i)
        print msgcodeid
        redisvalue='73917'
        qian=i/1000
        bai=i/100%10
        shi=i/10%10
        ge=i%10
        mobile='1700000'+str(qian)+str(bai)+str(shi)+str(ge)
        print mobile
        
        #mobile='13588120225'
        setredispara(redisname, redisvalue)
        datatemp={"mobile":mobile,"msgcodeid":msgcodeid,\
                  "msgcode":redisvalue,"passwd":"123456","secretkey":"2a7d228d-4dbd-4167-a3dd-882968efd685"}
        resulttemp=register.register(datatemp)
        print resulttemp
        try:
            deleteredispara(redisname)
        except Exception,e:
            print "delete redis param error %s"%e
    except Exception,e:
        print "make user %s failed,because error is %s"%(mobile,e)
     
       
if __name__=="__main__":
    record=[]
    '''
    for i in range(1,1000):
        process=multiprocessing.Process(target=userfactory,args=(i,))
        process.start()
        record.append(process)
    for process in record:
        process.join(30)
    '''
    userfactory(1000)
    