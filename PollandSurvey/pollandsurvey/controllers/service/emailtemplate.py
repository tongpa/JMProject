import os
import os.path
import base64 
import json 
import logging;
import types;
import datetime;
import os.path

from tg.configuration import AppConfig, config
from tg import request
  
log = logging.getLogger(__name__); 
from logsurvey import LogDBHandler
class EmailTemplate(object):




    def __init__(self):
        self.template = """
            to <b>[user]</b>
            
               test 1234
               
            thank you
             [sender]
             
        """;
        
        dh = LogDBHandler( config=config,request=request);        
        log.addHandler(dh)
        
        
    def loadtemplate(self,values):
        print values;
        content = self.template
        for k,v in  values.iteritems():
            content = content.replace('[%s]' % k,v)
        
        print content;
        
    
d = EmailTemplate();

value = {};
value['user'] = 'tong';
value['sender'] = '5555';
d.loadtemplate(value);