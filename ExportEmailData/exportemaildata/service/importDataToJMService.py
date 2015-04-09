from exportemaildata import model

import threading
import sys
from exportemaildata.controllers.utility import Utility
import logging;
log = logging.getLogger(__name__);

class ImportDataToJMService(threading.Thread):
    
    utility = Utility();
    def __init__(self,threadID):
        
        reload(sys).setdefaultencoding('utf8')
        threading.Thread.__init__(self)
        
        self.threadID = threadID;
        self.page =0;
        self.page_size = 10000;
    
    def run(self):
        
        log.info("Starting importData : " + str(self.threadID));
        
        self.importData();
        
    def sampleRunThread(self):
        log.info("Start run Thread");
    
    def importDataManual(self):
        
        from datetime import datetime;
        muser = model.MUser();
        #muserGeneral = model.MUserGeneralSetting();
 
        muser.USERNAME = "test@123.com"
        muser.PASSWORD = "12345678";
         
        muser.ID_PREFIX_NAME =  1;
         
        muser.FIRST_NAME = 'Test';

        muser.LAST_NAME = 'Test';
        muser.CREATE_USER ="SYSTEM";
        muser.STATUS = "W";
        
        muser.save();
        #muserGeneral.USERNAME = "test@123.com"
        #muserGeneral.PASSWORD = "12345678";
         
        #muserGeneral.ID_PREFIX_NAME =  1;
         
        #muserGeneral.FIRST_NAME = 'Test';

        #muserGeneral.LAST_NAME = 'Test';
        #muserGeneral.CREATE_USER ="SYSTEM";
        #muserGeneral.STATUS = "W";
        
        muserGeneral = model.MUserGeneralSetting();
        muserGeneral.setMainUser(muser);
        muserGeneral.ID_LANGUAGE = 1
        muserGeneral.ID_TIME_ZONE = 1
        muserGeneral.ID_COUNTRY = 221
        muserGeneral.ID_PROVINCE =  2 
        muserGeneral.ID_CURRENCY = 3 #Baht
        muserGeneral.MANY_POSITION = '1'
        muserGeneral.IS_USE_SERVICE = 'Y'
        muserGeneral.CREATE_DATE = datetime.now();
        muserGeneral.CREATE_USER ="SYSTEM";
        
        muserGeneral.save(); 
        
        pass;
        
    def importData(self):
        #step 1 load data map
        gender = model.MapGender.getAll();
        prefix = model.MapPrefix.getAll();
        province = model.MapProvince.getAll();
        city = model.MapCity.getAll();
        county = model.MapCounty.getAll();
        
        
        self.mapgender = {};
        self.mapprefix = {};
        self.mapprovince = {};
        self.mapcity = {};
        self.mapcounty = {}; 
        for g in gender: self.mapgender[str(g.name).decode('utf-8')] = g.ref_id_gender_jm;
        for g in prefix: self.mapprefix[str(g.name).decode('utf-8')] = g.ref_id_prefix_jm;
        #for g in prefix: self.mapprefix[g.name] = g.ref_id_prefix_jm;
        
        for g in province: self.mapprovince[str(g.name).decode('utf-8')] = g.ref_id_province_jm;
        for g in city: self.mapcity[str(g.name).decode('utf-8')] = g.ref_id_city_jm;
        for g in county: self.mapcounty[str(g.name).decode('utf-8')] = g.ref_id_county_jm;
         
        
        #step 2 load data email 
        size = model.EmailTemp.getSizeForExport();
        self.totalPage = (size/self.page_size) + 1;
        
        from datetime import datetime
        
        startTime  = datetime.now();
        #step 3 replace name to id ex: prefix, sex, country, city, province, countryname
        for num in range(0,self.totalPage):
            log.info( "%s to %s" ,num , (num*self.page_size));
            start = datetime.now();
            emailtemps = model.EmailTemp.getData(num, self.page_size);
            #step 4 insert data to table 
            for email in emailtemps:
                
                model.transaction.begin();
                #step 4.1 insert data to table sys_m_user not use
                
                #step 4.5 insert data to table job_m_user_general_setting
                #muserGeneral = model.MUserGeneralSetting();
                #muserGeneral.saveObject(email,self.mapprefix,self.mapprovince); 
                
                #email.id_user = muserGeneral.ID_USER;
                muser = model.MUser();
                muser.saveObject(email,self.mapprefix); 
                email.id_user = muser.ID_USER
                log.info( "ID USER : " +  str(email.id_user));
                log.info(email.email);
                #step 4.2 insert data to table sys_m_user_lang
                muserLang = model.MUserLang();
                muserLang.saveObject(email); 
                
                #step 4.3 insert data to table sys_m_user_map_role
                muserRole = model.MUserMapRole();
                muserRole.saveObject(email); 
                
                #step 4.4 insert data to table job_m_user_email
                muserEmail = model.MUserEmail();
                muserEmail.saveObject(email); 
                
                #step 4.5 insert data to table job_m_user_general_setting
                muserGeneral = model.MUserGeneralSetting();
                muserGeneral.saveObject(email,self.mapprefix,self.mapprovince); 
                
                #email.id_user = muserGeneral.ID_USER;
                
                
                #step 4.6 insert data to table job_m_user_phone
                muserPhone = model.MUserPhone(); 
                muserPhone.saveObject(email, self.mapprovince); 
                
                
                #step 4.6 insert data to table job_m_user_phone
                muserAddres = model.MUserAddres();
                muserAddres.saveObject(email,self.mapprovince,self.mapcity,self.mapcounty); 
                
                mjobAApplicant = model.MJobAApplicant();
                mjobAApplicant.saveObject(email  );
                
                
                
                mjobAApPiPersonalDatum = model.MJobAApPiPersonalDatum();
                mjobAApPiPersonalDatum.saveObject(email,self.mapprefix );
                
                
                mjobAApplicantCertificate = model.MJobAApplicantCertificate();
                mjobAApplicantCertificate.saveObject(email );
                
                
                email.updateExported();
                
                model.transaction.commit();
            stop  = datetime.now();
            
            log.info( "start : %s to : %s " , start  , stop);
            
            #if num > 1:
            #    break;
        
        stopTime  = datetime.now();
        
        log.info( "finish start : %s to %s" , startTime   , stopTime)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #step 4.7 insert data to table job_m_user_address
        
        
        pass;