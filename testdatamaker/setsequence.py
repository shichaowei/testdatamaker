#coding:utf-8
'''
Created on 2016��1��7��
修改sequence均为1000开始计数
@author: Administrator
'''
from postsql import *


if __name__=="__main__":

    temp=executeselectsql("select sequence_name from information_schema.sequences where sequence_schema = 'public';")
    for i in temp:
        print i[0]
        sqltemp="SELECT setval('%s', 1000)"%i[0]
        print sqltemp
        executeselectsql(sqltemp)
