#coding:utf-8
'''
Created on 2015��11��16��

@author: Administrator
'''
import psycopg2
import time
def executesql(sqltemp):
    conn = psycopg2.connect(host='111.1.17.197', port=1921, user='edntest', password='edntest', database='edntest')
    cur=conn.cursor()
    cur.execute(sqltemp)
    conn.commit()
    
    '''
    cur.execute("select * from edn_user where mobile='13071892616'")
    print cur.fetchall()
    conn.commit()
    '''
    cur.close()
    conn.close()

def executeselectsql(sqltemp):
    conn = psycopg2.connect(host='111.1.17.197', port=1921, user='edntest', password='edntest', database='edntest')
    cur=conn.cursor()
    cur.execute(sqltemp)
    temp=cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    print temp
    return temp

if __name__=="__main__":
   #executesql("update edn_user set status=0 where mobile='13071892616'")
   executeselectsql("select status from edn_car where id=1024") 
   executesql("update edn_car set status=1 where id=1024")
   executeselectsql("select status from edn_car where id=1024")
   
   '''
   #增加order订单表
   id=2102
   orderid=time.strftime("%Y%m%d%x", time.localtime()).replace('/','')
   print orderid
   executesql("INSERT INTO edn_user_car_order VALUES \
   (%d, %s, 21.00, 100.01, 100.01, 1500.01, 20.01, \
   0, 100.00, 30.01, 2000.00, 1842.01, 0, NULL, NULL, NULL, 0, NULL, \
   '2015-11-20 15:08:33', '2015-11-20 15:08:35', NULL, NULL, 1, 1007, 1007, \
   'test', 'test', 1380, 'test', '17091613448', 1, '浙A8QK70', '众泰', '众泰',\
    '众泰', '云100', 0, 3, 1, NULL, NULL, 1000, '2015-11-20 15:10:07', \
    'test', '2015-11-21 12:34:28.262493', '1380', 0);"%(id,orderid))
   '''
    

    
   #executesql("update edn_user_auth set status=0 where create_user='13071892616'")