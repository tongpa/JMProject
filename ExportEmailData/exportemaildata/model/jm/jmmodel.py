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
        
        print "email : " + email.email;
        
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
        self.LANG_CODE3 = 'THA';
        self.FIRST_NAME = email.firstname_thai;         
        self.LAST_NAME = email.lastname_thai;
        
        self.CREATE_USER ="SYSTEM";
        self.CREATE_DATE = datetime.now();
        self.save();
        

class MUserMapRole(SysMUserMapRole):
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
         
        self.ID_ROLE = 6
        
        self.CREATE_USER ="SYSTEM";
        self.CREATE_DATE = datetime.now();
        self.save();

class MUserEmail(JobMUserEmail):
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
         
        
        self.EMAIL = email.email
        self.IS_LOGIN = '1'
        self.IS_SUBSCRIBE = '1'
         
        
        self.CREATE_USER ="SYSTEM";
        self.CREATE_DATE = datetime.now();
        self.save();

class MUserGeneralSetting(JobMUserGeneralSetting):
    
    def __init__(self,user):
        self.super = user;
        
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
            print "save project"
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
        
    
    def saveObject(self,email,mapprovince ):
        self.ID_USER = email.id_user;
         
        
        self.ID_LANGUAGE = 1
        self.ID_TIME_ZONE = 1
        self.ID_COUNTRY = 221
        self.ID_PROVINCE =  mapprovince.get( email.province  ); 
        self.ID_CURRENCY = 3 #Baht
        self.MANY_POSITION = '1'
        self.IS_USE_SERVICE = 'Y'
        
        self.CREATE_USER ="SYSTEM";
        self.CREATE_DATE = datetime.now();
        self.save();

class MUserPhone(JobMUserPhone):
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
            print "save project"
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
        
    
    def saveObject(self,email,mapcountry,mapprovince ):
        self.ID_USER = email.id_user;
        
        #mobile phone 1
        if email.mobile and    len(str(email.mobile).strip()) >0    :
            print 'save mobile : ',email.mobile;
            self.ID_PHONE_TYPE = 1
            self.PHONE_PREFIX = '+66'
            self.PHONE_NO = email.mobile[1:]    
            self.TIME_START = '08:00:00'
            self.TIME_END = '16:00:00'
            self.TIME_DURATION_MINUTE = 480
            
            self.CREATE_USER ="SYSTEM";
            self.CREATE_DATE = datetime.now();
            self.save();
        #telephone   3
        if email.telephone and    len(str(email.telephone).strip()) >0 :
            print 'save telephone : ',email.telephone;
            self.ID_PHONE_TYPE = 3
            self.PHONE_PREFIX = '+66'
            self.PHONE_NO = email.telephone[1:]    
            self.TIME_START = '08:00:00'
            self.TIME_END = '16:00:00'
            self.TIME_DURATION_MINUTE = 480
            
            self.CREATE_USER ="SYSTEM";
            self.CREATE_DATE = datetime.now();
            self.save();


class MUserAddres(JobMUserAddres):
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
            print "save project"
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
        
    
    def saveObject(self,email,mapprovince,mapcity,mapcounty  ):
        self.ID_USER = email.id_user;
         
        
        #PRESENT  
        self.ID_USER_ADDRESS_TYPE = 2
   
        
        self.HOUSING_NO = email.house_no
        self.STREET_ADDRESS1 = email.building_village   + ' ' + email.moo
        self.STREET_ADDRESS2 = email.soi + ' '  + email.road
        self.ID_COUNTRY = 221
        self.ID_PROVINCE =  mapprovince.get(email.province);
        self.ID_CITY = mapcity.get(email.city);
        self.ID_COUNTY =mapcounty.get(email.county);
        self.ZIPCODE = email.postcode
        
        if email.telephone and    len(str(email.telephone).strip()) >0 :
            self.TEL_PREFIX_NO = '+66'
            self.TEL_NO = email.telephone[0:]
            
        if email.mobile and    len(str(email.mobile).strip()) >0    :
            self.MOBILE_PREFIX_NO = '+66'
            self.MOBILE_NO = email.mobile[0:]
        #self.FAX_PREFIX_NO = Column(String(255))
        #self.FAX_NO = Column(String(255))
        #self.FAX_EXT_NO = Column(String(255))
        
        
        
        self.CREATE_USER ="SYSTEM";
        self.CREATE_DATE = datetime.now();
        self.save();

