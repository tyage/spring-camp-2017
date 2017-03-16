#!/bin/env python
# -*- coding: utf8 -*-

import random
import SocketServer
import time
from urlparse import urlparse
import pprint

from pyicap import *

class ThreadingSimpleServer(SocketServer.ThreadingMixIn, ICAPServer):
    pass

class ICAPHandler(BaseICAPRequestHandler):
    def gfw_OPTIONS(self):
        self.set_icap_response(200)
        self.set_icap_header('Methods', 'RESPMOD')
        self.set_icap_header('Service', 'PyICAP Server 1.0')
        self.send_headers(False)

    def write_chunk_gfw(self, buf):
        self.write_chunk(buf.replace('天安門事件', '検閲済み!!!'))

    def gfw_RESPMOD(self):
        self.set_icap_response(200)

        self.set_enc_status(b' '.join(self.enc_res_status))
        for h in self.enc_res_headers:
            for v in self.enc_res_headers[h]:
                self.set_enc_header(h, v)

        if not self.has_body:
            self.send_headers(False)
            self.log_request(200)
            return

        if self.preview:
            prevbuf = b''
            while True:
                chunk = self.read_chunk()
                if chunk == b'':
                    break
                prevbuf += chunk
            if self.ieof:
                self.send_headers(True)
                if len(prevbuf) > 0:
                    self.write_chunk_gfw(prevbuf)
                self.write_chunk_gfw(b'')
                return
            self.cont()
            self.send_headers(True)
            buf = prevbuf
            while True:
                chunk = self.read_chunk()
                if chunk == b'':
                    break
                buf += chunk
            self.write_chunk_gfw(chunk)
        else:
            buf = ''
            while True:
                chunk = self.read_chunk()
                if chunk == b'':
                    break
                buf += chunk
            self.send_headers(True)
            self.write_chunk_gfw(buf)

port = 1344

server = ThreadingSimpleServer(('', port), ICAPHandler)
try:
    while 1:
        server.handle_request()
except KeyboardInterrupt:
    print "Finished"
