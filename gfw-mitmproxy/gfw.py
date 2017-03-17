# -*- coding: utf-8 -*-
import pprint

def response(flow):
    if '天安門事件'.encode('utf-8') in flow.response.content:
        flow.response.content = '<img src="http://cdn-ak.f.st-hatena.com/images/fotolife/x/xshintarox/20131228/20131228164639.jpg">'.encode('utf-8')
