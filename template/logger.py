#!/usr/bin/python
#encoding=utf-8

import logging.handlers  
from settings import BASE_DIR

LOG_FILE = BASE_DIR + '/daily.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

loggerDaily = logging.getLogger('Daily')
loggerDaily.addHandler(handler)
loggerDaily.setLevel(logging.INFO)