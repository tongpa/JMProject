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

from datetime import datetime ;
from pollandsurvey.controllers.utility import Utility
from pollandsurvey import model

log = logging.getLogger(__name__);
from  survey import LogDBHandler;
class UserObject(object):
    def __init__(self):
        self.fullname = None;
        self.fulllastname = None;
        self.email = None;
        self.city = None;
        self.country = None;
        self.address = None;
        self.password = None;
        self.rpassword = None;
        self.tnc = None;
        
        dh = LogDBHandler( config=config,request=request);        
        log.addHandler(dh)
        

class RegisterService(object):

    def __init__(self):
        
        self.utility = Utility();
        pass;
    
    def createUser(self, kw):
        
        self.fullname = kw.get('fullname');
        self.fulllastname = kw.get('fulllastname');
        self.email = kw.get('email');
        self.city = kw.get('city');
        self.country = kw.get('country');
        self.address = kw.get('address');
        self.password = kw.get('password');
        self.rpassword = kw.get('rpassword');
        self.tnc = kw.get('tnc');
        self.id_gender = kw.get('gender');
        
        
        
        self.user = model.UserService();
        self.user.user_name = self.email;
        self.user.email_address = self.email;
        self.user.display_name = self.fullname + " " + self.fulllastname;
        self.user._set_password(self.password); 
        self.user.first_name = self.fullname
        self.user.last_name = self.fulllastname
        self.user.address =self.address
        self.user.city =self.city
        self.user.country = self.country
        self.user.id_gender = self.id_gender;
        self.user.accept_tnc = self.utility.convertToBit(self.tnc);
        self.user.save();
        self.user.updateGroupUserVoter();
        
        
        self.userGenCode = self.createUserGenCode(self.user);
        
        return self.user,self.userGenCode;
    
    def createUserGenCode(self,user):
        self.userGenCode = model.UserGenCode();
        self.userGenCode.user_id =  user.user_id;
        self.userGenCode.id_gen_code_type = 2 ;# register
        self.userGenCode.code = str(self.userGenCode.user_id)+ self.utility.my_random_string(15);
        self.userGenCode.expire_date =  self.utility.plusDate(datetime.today(),30);
        self.userGenCode.save();
        
        return self.userGenCode;
    
    def reActivateUserGenCode(self,userGenCode,user):
        if(userGenCode):
            self.userGenCode = userGenCode;
            
            self.userGenCode.code = str(self.userGenCode.user_id)+ self.utility.my_random_string(15);
            self.userGenCode.expire_date =  self.utility.plusDate(datetime.today(),30);
            self.userGenCode.create_date = datetime.today();
            self.userGenCode.count = self.userGenCode.count +1;
            self.userGenCode.success = 0;
            return self.userGenCode;
        
        return userGenCode;