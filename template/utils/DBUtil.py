#encoding=utf-8

from template.conf.ConfigUtil import CONNECTION_POOL
from template.logger import loggerDaily

LOGGER = loggerDaily

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

