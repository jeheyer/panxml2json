#!/usr/bin/env python

import sys,os,ssl

libpath = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(libpath, os.pardir, 'lib')]

from panxapi import *
import pan.xapi
import pan.rc

xapi = pan.xapi.PanXapi(hostname='firewall-us-west-1.ops.hightail.com', api_key='LUFRPT1ZdXdjSGphZ2pWbWozMWY0bmRrZEVHdCszMDA9bU9jTWd5VDQwVUhHTWsydmVGbHhiVjZ1Zk84TnJvbWNTTDFyMFFnZlh6cz0=', ssl_context=ssl._create_unverified_context())
action = 'show'
xapi.show()
print_status(xapi, action)
