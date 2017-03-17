# -*- coding: utf-8 -*-
import pprint

def response(flow):
    if '天安門事件'.encode('utf-8') in flow.response.content:
        flow.response.content = '検閲済み'.encode('utf-8')
