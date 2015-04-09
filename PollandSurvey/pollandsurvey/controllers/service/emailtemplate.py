import os
import os.path
import base64 
import json 
import logging;
import types;
import datetime;
import os.path
log = logging.getLogger(__name__); 
class EmailTemplate(object):




    def __init__(self):
        self.template = """
            to <b>[user]</b>
            
               test 1234
               
            thank you
             [sender]
             
        """;
        
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