# -*- coding: utf-8 -*-
class SearchObject(object):
    
    def __init__(self, keysearch = None, page =0 , start=0, limit=None, _dc=None):
        self.keysearch = keysearch
        self.page = page
        self.start = start
        self.limit = limit
        self._dc = _dc
        
        
    
        