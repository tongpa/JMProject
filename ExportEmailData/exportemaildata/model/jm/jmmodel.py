# -*- coding: utf-8 -*-
import os
from datetime import datetime
from hashlib import sha256
__all__ = ['DayConfig','SysMUser']
 
from sqlalchemy import BigInteger, Column, Date, DateTime, Enum, ForeignKey, Index, Integer, Numeric, SmallInteger, String, Text, Time, VARBINARY, text
from sqlalchemy.types import Unicode, Integer, DateTime,BigInteger
from sqlalchemy.orm import relation, synonym,mapper,relationship
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.ext.automap import automap_base

from sqlalchemy.exc import IntegrityError
from exportemaildata.model import DeclarativeBase2, metadata2, DBSession2 

from exportemaildata.model.jm.jmdatamodel import SysMUser,SysMUserLang,SysMUserMapRole,JobMUserEmail,JobMUserGeneralSetting,JobMUserPhone,JobMUserAddres; 

class MUser(SysMUser):
    
   
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
            print "save project"
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
    
    def saveObject(self,email,mapprefix):
        self.USERNAME = email.email
        self.PASSWORD = "12345678";
         
        self.ID_PREFIX_NAME =  mapprefix.get( email.prefix  );
         
        self.FIRST_NAME = email.firstname_eng

        self.LAST_NAME = email.lastname_eng
        self.CREATE_USER ="SYSTEM";
        self.CREATE_DATE = datetime.now();
        self.STATUS = "W";
        
        self.save();
    

class MUserLang(SysMUserLang):
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
            print "save project"
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
        
    
    def saveObject(self,email ):
        self.ID_USER = email.id_user;
        self.LANG_CODE3 = '221';
        self.FIRST_NAME = email.firstname_thai;         
        self.LAST_NAME = email.lastname_thai;
        
        self.CREATE_USER ="SYSTEM";
        self.CREATE_DATE = datetime.now();
        self.save();
        

class MUserMapRole(SysMUserMapRole):
    pass;

class MUserEmail(JobMUserEmail):
    pass;

class MUserGeneralSetting(JobMUserGeneralSetting):
    pass;

class MUserPhone(JobMUserPhone):
    pass;

class MUserAddres(JobMUserAddres):
    pass;
