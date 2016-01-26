#coding:utf-8
'''
Created on 2016��1��7��

@author: Administrator
'''
from postsql import *


if __name__=="__main__":

    for id in range(5999,6000):
        tempsql="INSERT INTO edn_car VALUES (%d, '浙A%s', '11111111', \
    '白色', '11111111', null, null, '1142', '1063', '1077', '0', '2015-12-19 17:32:56.377', \
    '2015-12-24 14:27:30.335', 'edianniu', 'edianniu', '0', 'img1/M01/00/05/wKgB-1Z1JEiAXgODAAOQ0fsYeg073..jpg',\
     'img1/M00/00/05/wKgB-1Z1JEiAAAd-AASw0BB9GWk69..jpg', null, '2015-12-19 00:00:00', '2015-12-19 00:00:00',\
      '200000', '2000', '1031')"%(id,id)
        print tempsql
         
        print executesql(tempsql)
