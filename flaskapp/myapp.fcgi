#!/usr/local/bin/python
 
from flup.server.fcgi import WSGIServer
import sys
sys.path.insert(0, '~/myflask/bin/activate')
 
from myapp import app
 
if __name__ == '__main__':
    WSGIServer(app).run()