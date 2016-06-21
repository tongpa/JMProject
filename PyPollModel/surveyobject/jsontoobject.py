# -*- coding: utf-8 -*-
import json

class JsontoObject(object):
    def __init__(self, d):
         
        for a, b in d.items():
            
            if isinstance(b, (list, tuple)):
                setattr(self, a, [JsontoObject(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, JsontoObject(b) if isinstance(b, dict) else b)
                