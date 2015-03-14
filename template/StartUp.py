#encoding=utf-8
'''
Created on 2014年7月1日

@author: gaott
'''


def start():
    
    '''
     初始化数据库连接
    '''
    
    from DBUtils.PooledDB import PooledDB
    import MySQLdb
    from template.conf import ConfigUtil
    from template.utils.ParamUtil import getParamDict
    
    connParams = getParamDict(ConfigUtil.CONN_STRING)
    username = connParams.get('user')
    passwd = connParams.get('passwd')
    db = connParams.get('db')
    port = eval(connParams.get('port'))
    host = connParams.get('host')

    ConfigUtil.CONNECTION_POOL = PooledDB(creator=MySQLdb, host=host , port=port , user=username , passwd=passwd ,db=db,mincached=10 , maxcached=20 ,maxconnections=30,use_unicode=False,charset='UTF8')
