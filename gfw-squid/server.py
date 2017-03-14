#!/bin/env python
# -*- coding: utf8 -*-

import random
import SocketServer
import time
from urlparse import urlparse

from pyicap import *

class ThreadingSimpleServer(SocketServer.ThreadingMixIn, ICAPServer):
    pass

class ICAPHandler(BaseICAPRequestHandler):
    def gfw_RESPMOD(self):
        buf = ''
        while True:
            chunk = self.read_chunk()
            self.write_chunk(chunk)
            if chunk == '':
                break
            buf += chunk
        print(buf)

port = 1344

server = ThreadingSimpleServer(('', port), ICAPHandler)
try:
    while 1:
        server.handle_request()
except KeyboardInterrupt:
    print "Finished"
