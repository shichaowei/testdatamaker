#coding:utf-8
'''
Created on 2016��1��19

@author: Administrator
'''
from postsql import *
import time

if __name__=="__main__":
    timestring=time.strftime("%Y-%m-%d %X", time.localtime())
    #print type(timestring)
    print timestring
    
    for id in range(101,200):
        latitude=30.0
        longitude=120.0
        print id/1000.0
        latitude=latitude+id/1000.0
        longitude=id/1000.0+longitude
        print longitude
        tempsql="INSERT INTO edn_car_alert VALUES (nextval('seq_edn_car_alert'), '17000000004', null, %f,\
         %f, '杭州滨江', '1', null, '0', null, now(),'魏士超手动' , null, null, '0')"%(latitude,longitude)
        print tempsql
         
        print executesql(tempsql)
    