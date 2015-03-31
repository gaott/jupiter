# -*- coding: utf-8 -*-  

'''
Created on 2013-7-3

@author: gaott
'''
from jupiter.conf.ConfigUtil import CONNECTION_POOL
from jupiter.logger import loggerDaily

LOGGER = loggerDaily

'''
执行SQL，用于insert,update,delete
'''
def executeOpt(sqlStr, *params):
    conn = CONNECTION_POOL.connection()
    param = []
    if params :
        for i in range(0, len(params)):
            param.append(params[i])
            
    count = 0
    try:
        cursor = conn.cursor() 
        count = cursor.execute(sqlStr, tuple(param))
        conn.commit()
    except Exception,e:
        LOGGER.error(e)
    finally:
        cursor.close()
        conn.close()
    return count
'''
执行SQL，用于select
'''
def getSqlResult(sqlStr, *params):
    conn = CONNECTION_POOL.connection()
    param = []
    if params :
        for i in range(0, len(params)):
            param.append(params[i])
    result = ""
    try:
        cursor = conn.cursor()
        cursor.execute(sqlStr, tuple(param))
        result = cursor.fetchall()
    except Exception,e:
        LOGGER.error(e)
    finally:
        cursor.close()
        conn.close()
    return result

'''
用于事务操作
'''
def executeTransactionSqls(sqls):
    if not sqls :
        return
    
    conn = CONNECTION_POOL.connection()
    cursor = conn.cursor() 
    try:
        for i in range(0, len(sqls)):
            cursor.execute(sqls[i])
        conn.commit()
    except Exception,e:
        LOGGER.error(e)
    finally:
        cursor.close()
        conn.close()

