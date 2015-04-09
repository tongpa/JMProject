import os
import os.path
import base64 
import json 
import logging;
import types;
import datetime;
import os.path


from pollandsurvey import model

log = logging.getLogger(__name__);
 
class RegisterService(object):

    def __init__(self):
        pass;
    
    
    def forGotPassword(self,email):
        
        user = model.User.by_email_address(email);
        
        user._set_password('1234');
        
        
        print user;
        pass;