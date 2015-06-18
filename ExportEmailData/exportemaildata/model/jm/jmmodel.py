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

from exportemaildata.model.jm.jmdatamodel import SysMUser,SysMUserLang,SysMUserMapRole,JobMUserEmail,JobMUserGeneralSetting,SysMPhone,SysMAddres,JobAApplicant,JobAApPiPersonalDatum,JobAApplicantCertificate,SysMUserMapAddres,SysMUserMapPhone,SysMAddressMapPhone; 
import logging;
log = logging.getLogger(__name__);
class MUser(SysMUser):
    
   
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
             
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
    
    def saveObject(self,email,mapprefix):
        
        
        
        self.USERNAME = email.email
        self.PASSWORD = "12345678";
         
        self.ID_PREFIX_NAME =  mapprefix.get( email.prefix  );
        self.ID_PREFIX_NAME = 'NULL' if self.ID_PREFIX_NAME == None else self.ID_PREFIX_NAME; 
         
        self.FIRST_NAME = email.firstname_eng

        self.LAST_NAME = email.lastname_eng
        self.CREATE_USER ="EXTERNAL";
        self.CREATE_DATE = email.date_time;#datetime.now();
        self.STATUS = "A";
        
        self.save();
    
    def insertToSQL(self,email,mapprefix):
        
        self.USERNAME = email.email
        self.PASSWORD = "12345678";
         
        self.ID_PREFIX_NAME =  mapprefix.get( email.prefix  );
        self.ID_PREFIX_NAME = 'NULL' if self.ID_PREFIX_NAME == None else self.ID_PREFIX_NAME; 
         
        self.FIRST_NAME = email.firstname_eng

        self.LAST_NAME = email.lastname_eng
        self.CREATE_USER ="EXTERNAL";
        self.CREATE_DATE = email.date_time;#datetime.now();
        self.STATUS = "A";
        
        self.sql = """INSERT INTO """  + self.__tablename__.upper() + """(USERNAME,PASSWORD,ID_PREFIX_NAME,FIRST_NAME,LAST_NAME,CREATE_USER,CREATE_DATE,REF_ID) VALUES('""" + self.USERNAME + """',md5(12345678), """+ str(self.ID_PREFIX_NAME) + """,'""" +  self.FIRST_NAME + """','""" + self.LAST_NAME  + """','"""+ str(self.CREATE_USER ) + """','"""+ str(self.CREATE_DATE) + """',""" + str(email.id) +""");"""
                       
        
        
        
        return self.sql;
                    

class MUserLang(SysMUserLang):
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
             
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
        
    
    def saveObject(self,email ):
        self.ID_USER = email.id_user;
        self.LANG_CODE3 = 'THA';
        self.FIRST_NAME = email.firstname_thai;         
        self.LAST_NAME = email.lastname_thai;
        
        self.CREATE_USER ="EXTERNAL";
        self.CREATE_DATE = email.date_time;#datetime.now();
        #self.save();
        
        self.sql = """INSERT INTO """  + self.__tablename__.upper() + """  (ID_USER,LANG_CODE3,FIRST_NAME,LAST_NAME,CREATE_USER,CREATE_DATE )   SELECT SYS_M_USER.ID_USER,'""" +self.LANG_CODE3  + """','""" + str(self.FIRST_NAME) + """','""" + str(self.LAST_NAME) + """','"""+ str(self.CREATE_USER ) + """','"""+ str(self.CREATE_DATE) + """' from SYS_M_USER WHERE REF_ID = """ +str(email.id) + """;"""
        
         
                       
         
        return self.sql;
        

class MUserMapRole(SysMUserMapRole):
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
             
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
        
    
    def saveObject(self,email ):
        self.ID_USER = email.id_user;
         
        self.ID_ROLE = 6
        
        self.CREATE_USER ="EXTERNAL";
        self.CREATE_DATE = email.date_time;#datetime.now();
        #self.save();
        self.sql = """INSERT INTO """  + self.__tablename__.upper() + """  (ID_USER,ID_ROLE,CREATE_USER,CREATE_DATE )   SELECT SYS_M_USER.ID_USER,'""" + str(self.ID_ROLE)  + """','"""+ str(self.CREATE_USER ) + """','"""+ str(self.CREATE_DATE) + """' from SYS_M_USER WHERE REF_ID = """ +str(email.id) + """;"""
        
        return self.sql;
        
    def insertToSQL(self,email):
        
        self.sql = """INSERT INTO """  + self.__tablename__.upper() + """(USERNAME,PASSWORD)""" 
        

class MUserEmail(JobMUserEmail):
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
             
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
        
    
    def saveObject(self,email ):
        self.ID_USER = email.id_user;
         
        
        self.EMAIL = email.email
        self.IS_LOGIN = '1'
        self.IS_SUBSCRIBE = '1'
         
        
        self.CREATE_USER ="EXTERNAL";
        self.CREATE_DATE = email.date_time;#datetime.now();
        #self.save();
        
        self.sql = """INSERT INTO """  + self.__tablename__.upper() + """  (ID_USER,EMAIL,IS_LOGIN,IS_SUBSCRIBE,CREATE_USER,CREATE_DATE )  SELECT SYS_M_USER.ID_USER,'""" + str(self.EMAIL)  + """','"""+ str(self.IS_LOGIN)  + """','"""+ str(self.IS_SUBSCRIBE)  + """','"""+ str(self.CREATE_USER ) + """','"""+ str(self.CREATE_DATE) + """' from SYS_M_USER WHERE REF_ID = """ +str(email.id) + """;"""
        
        return self.sql;

class MUserGeneralSetting(JobMUserGeneralSetting):
    
    def __init__(self):
        pass;
        
    def setMainUser(self,user):
        self.ID_USER = user.ID_USER;
        #self.USERNAME = user.USERNAME;
        #self.PASSWORD = user.PASSWORD;
         
        #self.ID_PREFIX_NAME =  user.ID_PREFIX_NAME;
         
        #self.FIRST_NAME = user.FIRST_NAME;

        #self.LAST_NAME = user.LAST_NAME;
        self.CREATE_USER =user.CREATE_USER;
        self.STATUS = user.STATUS;
        
        
        
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
             
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
        
    
    def saveObject(self,email,mapprefix,mapprovince ):
        
        
        self.ID_USER = email.id_user;
        
        #self.USERNAME = email.email
        #self.PASSWORD = "12345678";
        #self.ID_PREFIX_NAME =  mapprefix.get( email.prefix  );
        #self.FIRST_NAME = email.firstname_eng
        #self.LAST_NAME = email.lastname_eng
        #self.CREATE_USER ="SYSTEM";
        #self.CREATE_DATE = datetime.now();
        #self.STATUS = "A";
        
         
        
        self.ID_LANGUAGE = 1
        self.ID_TIME_ZONE = 1
        self.ID_COUNTRY = 221
        self.ID_PROVINCE =    mapprovince.get( email.province  )   ; 
        self.ID_PROVINCE = '0' if self.ID_PROVINCE == None else self.ID_PROVINCE;
        
        self.ID_CURRENCY = 3 #Baht
        self.MANY_POSITION = '1'
        self.IS_USE_SERVICE = 'Y'
        
        self.CREATE_USER ="EXTERNAL";
        self.CREATE_DATE = email.date_time;#datetime.now();
        
        self.sql = """INSERT INTO """  + self.__tablename__.upper() + """  (ID_USER,ID_LANGUAGE ,ID_TIME_ZONE, ID_COUNTRY, ID_PROVINCE, ID_CURRENCY, MANY_POSITION, IS_USE_SERVICE, CREATE_USER, CREATE_DATE )  SELECT SYS_M_USER.ID_USER,'""" + str(self.ID_LANGUAGE)  + """','"""+ str(self.ID_TIME_ZONE)   + """','"""+ str(self.ID_COUNTRY)  + """','"""+ str(self.ID_PROVINCE)  +  """','"""+  str(self.ID_CURRENCY)  +   """','"""+ str(self.MANY_POSITION)  + """','"""         +str(self.IS_USE_SERVICE)  + """','"""         +str(self.CREATE_USER ) + """','"""+ str(self.CREATE_DATE) + """' from SYS_M_USER WHERE REF_ID = """ +str(email.id) + """;"""
        
        return self.sql;
    
        #self.save();

class MUserPhone(SysMPhone):
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
             
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
        
    
    def saveObject(self,email,  mapprovince ):
        self.ID_USER = email.id_user;
        
        self.sql = "";
        #mobile phone 1
        if email.mobile and    len(str(email.mobile).strip()) >0    :
             
            self.ID_PHONE_TYPE = 1
            self.PHONE_PREFIX = '+66'
            self.PHONE_NO = email.mobile[1:]    
            self.TIME_START = '08:00:00'
            self.TIME_END = '16:00:00'
            self.TIME_DURATION_MINUTE = 480
            
            self.CREATE_USER ="EXTERNAL";
            self.CREATE_DATE = email.date_time;#datetime.now();
            #self.save();
            
            self.sql = """INSERT INTO """  + self.__tablename__.upper() + """ (ID_PHONE_TYPE,PHONE_PREFIX ,PHONE_NO, TIME_START, TIME_END, TIME_DURATION_MINUTE, CREATE_USER, CREATE_DATE ,REF_ID, ID_USER)   SELECT '""" + str(self.ID_PHONE_TYPE) + """','"""+ str(self.PHONE_PREFIX)   + """','"""+ str(self.PHONE_NO)  + """','"""+ str(self.TIME_START)  +  """','"""+  str(self.TIME_END)  +   """','"""+ str(self.TIME_DURATION_MINUTE)  + """','""" +str(self.CREATE_USER ) + """','"""+ str(self.CREATE_DATE) + """','"""+ str(email.id)+'1' +   """', SYS_M_USER.ID_USER  from SYS_M_USER WHERE REF_ID = """ +str(email.id) + """;"""
            
            
            self.sql = self.sql + "\n";
            
            
        #telephone   3
        if email.telephone and    len(str(email.telephone).strip()) >0 :
             
            self.ID_PHONE_TYPE = 3
            self.PHONE_PREFIX = '+66'
            self.PHONE_NO = email.telephone[1:]    
            self.TIME_START = '08:00:00'
            self.TIME_END = '16:00:00'
            self.TIME_DURATION_MINUTE = 480
            
            self.CREATE_USER ="EXTERNAL";
            self.CREATE_DATE = email.date_time;#datetime.now();
            #self.save();
            
            self.sql = """INSERT INTO """  + self.__tablename__.upper() + """ (ID_PHONE_TYPE,PHONE_PREFIX ,PHONE_NO, TIME_START, TIME_END, TIME_DURATION_MINUTE, CREATE_USER, CREATE_DATE , REF_ID, ID_USER)   SELECT '""" + str(self.ID_PHONE_TYPE) + """','"""+ str(self.PHONE_PREFIX)   + """','"""+ str(self.PHONE_NO)  + """','"""+ str(self.TIME_START)  +  """','"""+  str(self.TIME_END)  +   """','"""+ str(self.TIME_DURATION_MINUTE)  + """','""" +str(self.CREATE_USER ) + """','"""+ str(self.CREATE_DATE) + """','"""+ str(email.id)+'2' +   """', SYS_M_USER.ID_USER  from SYS_M_USER WHERE REF_ID = """ +str(email.id) + """;"""
            self.sql = self.sql + "\n";
            
        
        return self.sql;

class MUserAddres(SysMAddres):
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
             
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
        
    
    def saveObject(self,email,mapprovince,mapcity,mapcounty  ):
        self.ID_USER = email.id_user;
         
        
        #PRESENT  
        self.ID_USER_ADDRESS_TYPE = 2
   
        try:
            self.HOUSING_NO = email.house_no
            self.STREET_ADDRESS1 = str(email.building_village)   + ' ' + str(email.moo)
            self.STREET_ADDRESS2 = str(email.soi) + ' '  + str(email.road)
            self.ID_COUNTRY = 221
            self.ID_PROVINCE =  mapprovince.get(email.province);
            self.ID_PROVINCE = '0' if self.ID_PROVINCE == None else self.ID_PROVINCE;
             
            self.ID_CITY = mapcity.get(email.city);
            self.ID_CITY = '0' if self.ID_CITY == None else self.ID_CITY;
             
            self.ID_COUNTY =mapcounty.get(email.county);
            self.ID_COUNTY = '0' if self.ID_COUNTY == None else self.ID_COUNTY; 
            
            self.ZIPCODE = email.postcode
            
          #  if email.telephone and    len(str(email.telephone).strip()) >0 :
          #      self.TEL_PREFIX_NO = '+66'
          #      self.TEL_NO = email.telephone[0:]
                
          #  if email.mobile and    len(str(email.mobile).strip()) >0    :
          #      self.MOBILE_PREFIX_NO = '+66'
          #      self.MOBILE_NO = email.mobile[0:]
            #self.FAX_PREFIX_NO = Column(String(255))
            #self.FAX_NO = Column(String(255))
            #self.FAX_EXT_NO = Column(String(255))
            
            
            
            self.CREATE_USER ="EXTERNAL";
            self.CREATE_DATE = email.date_time;#datetime.now();
            #self.save();
            
            self.sql = """INSERT INTO """  + self.__tablename__.upper() + """ (HOUSING_NO,STREET_ADDRESS1 ,STREET_ADDRESS2, ID_COUNTRY, ID_PROVINCE, ZIPCODE , CREATE_USER, CREATE_DATE , REF_ID ,ID_USER) SELECT '""" + str(self.HOUSING_NO) + """','"""+ str(self.STREET_ADDRESS1)   + """','"""+ str(self.STREET_ADDRESS2)  + """','"""+ str(self.ID_COUNTRY)  +  """','"""+  str(self.ID_PROVINCE)  +"""','"""+ str(self.ZIPCODE) + """','"""+ str(self.CREATE_USER) + """','"""+ str(self.CREATE_DATE) + """','"""+ str(email.id) +  """', SYS_M_USER.ID_USER  from SYS_M_USER WHERE REF_ID = """ +str(email.id) + """;"""
            self.sql = self.sql + "\n";
            
            return self.sql;
            
        except Exception as e:
            log.info( "---error---");
            log.info(email.email);
            return self.sql;

class MJobAApplicant(JobAApplicant):
    
    
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
             
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
        
    def saveObject(self,email  ):
        self.ID_APPLICANT = email.id_user;
        self.ID_USER = email.id_user;
        
        self.CREATE_USER ="EXTERNAL";
        self.CREATE_DATE = email.date_time;#datetime.now();
        
        #self.save();
        
        self.sql = """INSERT INTO """  + self.__tablename__.upper() + """ (ID_APPLICANT,ID_USER,STATUS, CREATE_USER, CREATE_DATE ) SELECT SYS_M_USER.ID_USER, SYS_M_USER.ID_USER,'W', '""" + str(self.CREATE_USER)+ """','""" + str(self.CREATE_DATE)+ """'  from SYS_M_USER WHERE REF_ID = """ +str(email.id) + """;"""
        self.sql = self.sql + "\n";

        return self.sql;

        
class MJobAApPiPersonalDatum(JobAApPiPersonalDatum):
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
             
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
        
    def saveObject(self,email,mapgender  ):
        self.ID_APPLICANT = email.id_user;
        self.ID_USER = email.id_user;
        
        
       # self.ID_PREFIX_NAME =  mapprefix.get( email.prefix  );
         
        #self.FIRST_NAME = email.firstname_eng
        #self.LAST_NAME = email.lastname_eng
        #self.ID_PREFIX_NAME_LOCAL =  mapprefix.get( email.prefix  );
        #self.FIRST_NAME_LOCAL = email.firstname_thai;
        #self.LAST_NAME_LOCAL =  email.lastname_thai;
        self.DATE_BIRTH = email.birthdate;
        self.ID_GENDER = mapgender.get( email.sex  );
        self.ID_GENDER = 'NULL' if self.ID_GENDER == None else self.ID_GENDER; 
        
        self.CREATE_USER ="EXTERNAL";
        self.CREATE_DATE = email.date_time;#datetime.now();
        #self.save();
        
        self.sql = """INSERT INTO """ + self.__tablename__.upper() + """(ID_APPLICANT, DATE_BIRTH, ID_GENDER, CREATE_USER, CREATE_DATE)  SELECT JOB_A_APPLICANT.ID_APPLICANT,'""" + str(self.DATE_BIRTH) + """','""" + str(self.ID_GENDER) + """','""" + str(self.CREATE_USER) + """','""" + str(self.CREATE_DATE) + """'  FROM JOB_A_APPLICANT INNER JOIN SYS_M_USER ON JOB_A_APPLICANT.ID_USER = SYS_M_USER.ID_USER WHERE SYS_M_USER.REF_ID = """ + str(email.id) +""";""";
        
        return self.sql;
        
class MJobAApplicantCertificate(JobAApplicantCertificate):
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
             
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
        
    def saveObject(self,email  ):
        self.ID_APPLICANT = email.id_user;    
        
        
         
    
        self.ID_APPLICANT_CERTIFICATE_TYPE = 7
        self.CREATE_USER ="EXTERNAL";
        self.CREATE_DATE = email.date_time;#datetime.now();
        #self.save();
        
        self.sql = """INSERT INTO """ + self.__tablename__.upper() + """(ID_APPLICANT, ID_APPLICANT_CERTIFICATE_TYPE,  CREATE_USER, CREATE_DATE)  SELECT JOB_A_APPLICANT.ID_APPLICANT,'""" + str(self.ID_APPLICANT_CERTIFICATE_TYPE)   + """','""" + str(self.CREATE_USER) + """','""" + str(self.CREATE_DATE) + """'  FROM JOB_A_APPLICANT INNER JOIN SYS_M_USER ON JOB_A_APPLICANT.ID_USER = SYS_M_USER.ID_USER WHERE SYS_M_USER.REF_ID = """ + str(email.id) +""";""";
        
        return self.sql;
        
class MSysMUserMapAddres(SysMUserMapAddres):
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
             
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
    
    def saveObject(self,email):
        
        self.CREATE_USER ="EXTERNAL";
        self.CREATE_DATE = email.date_time;#datetime.now();
        self.sql = """INSERT INTO """  + self.__tablename__.upper() + """ (ID_USER, ID_ADDRESS,  CREATE_USER, CREATE_DATE)    SELECT ID_USER,ID_ADDRESS,'"""   +str(self.CREATE_USER ) + """','"""+ str(self.CREATE_DATE) +   """'  from sys_m_address WHERE REF_ID =   """ +  str(email.id) + """;"""
                
        
        return self.sql;
         
class MSysMUserMapPhone(SysMUserMapPhone):
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
             
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
    
    def saveObject(self,email):
        
        self.CREATE_USER ="EXTERNAL";
        self.CREATE_DATE = email.date_time;#datetime.now();
        self.sql = """INSERT INTO """  + self.__tablename__.upper() + """ (ID_USER, ID_PHONE,  CREATE_USER, CREATE_DATE)    SELECT ID_USER,ID_PHONE,'"""   +str(self.CREATE_USER ) + """','"""+ str(self.CREATE_DATE) +   """'  from sys_m_phone WHERE REF_ID in ( """ +str(email.id)+'1' +""","""+ str(email.id)+'2' + """);"""
                
        
        return self.sql;
    
class MSysMAddressMapPhone(SysMAddressMapPhone):
    def save(self):
        try:
            DBSession2.add(self); 
            DBSession2.flush() ;
             
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
    