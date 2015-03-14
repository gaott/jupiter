#!/bin/bash

PIDFILE="uwsgi.pid"

if [ -f $PIDFILE ]; then
     kill -9 `cat -- $PIDFILE`
fi

sleep 3

uwsgi -x uwsgi.xml

