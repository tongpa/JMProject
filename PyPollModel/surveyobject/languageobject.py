# -*- coding: utf-8 -*-
class LanguageObject(object):
    
    lang= None
    langDefault = None
    def __init__(self):
        pass
    
    @classmethod
    def setLanguage(cls,lang):
         
        cls.lang = []
        cls.langDefault = {}
        for l in lang:
            language = Language(id_language_label= l.id_language_label,
                            module= l.module,
                             default_label= l.default_label,
                             message_en= l.message_en,
                             message_th= l.message_th
                             )
            cls.lang.append( language)
            cls.langDefault[l.default_label] = language
    
    @classmethod
    def getLanguage(cls):
        return cls.lang
    
    @classmethod
    def getdata(cls,key,lang='EN'):
        if (cls.langDefault is not None and cls.langDefault[key] is not None) :
            if 'th'.upper() == lang.upper():
                return cls.langDefault[key].message_th
            else:
                return cls.langDefault[key].message_en
        return key
    

class Language(object):
    def __init__(self,id_language_label=None,module=None,default_label=None,message_en=None, message_th=None):
        self.id_language_label = id_language_label
        self.module = module
        self.default_label =  default_label
        self.message_en = message_en
        self.message_th = message_th