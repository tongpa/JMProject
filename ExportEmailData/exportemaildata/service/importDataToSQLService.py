from exportemaildata import model

import threading
import sys
from exportemaildata.controllers.utility import Utility
import logging;
import math;
log = logging.getLogger(__name__);


class ImportDataToSQLService(threading.Thread):
    
    utility = Utility();
    def __init__(self,threadID):
        
        reload(sys).setdefaultencoding('utf8')
        threading.Thread.__init__(self)
        
        self.threadID = threadID;
        self.page =0;
        self.page_size = 5000;
        self.size_in_file = 50000;
        
    def run(self):
        
        log.info("Starting importData : " + str(self.threadID));
        
        self.importData();
        
    def sampleRunThread(self):
        log.info("Start run Thread");
        
    
    
    def importData(self):
        
        gender = model.MapGender.getAll();
        prefix = model.MapPrefix.getAll();
        province = model.MapProvince.getAll();
        #city = model.MapCity.getAll();
        #county = model.MapCounty.getAll();
        
        
        self.mapgender = {};
        self.mapprefix = {};
        self.mapprovince = {};
        self.mapcity = {};
        self.mapcounty = {}; 
        for g in gender: self.mapgender[str(g.name).decode('utf-8')] = g.ref_id_gender_jm;
        for g in prefix: self.mapprefix[str(g.name).decode('utf-8')] = g.ref_id_prefix_jm;
        #for g in prefix: self.mapprefix[g.name] = g.ref_id_prefix_jm;
        
        for g in province: self.mapprovince[str(g.name).decode('utf-8')] = g.ref_id_province_jm;
        #for g in city: self.mapcity[str(g.name).decode('utf-8')] = g.ref_id_city_jm;
        #for g in county: self.mapcounty[str(g.name).decode('utf-8')] = g.ref_id_county_jm;
        
        #step 2 load data email 
        size = 200000; #model.EmailTemp.getSizeForExport();
        
        self.numFile =  int( math.ceil(size/float(self.size_in_file)) );
        log.info( "size email : %s" ,size );
        
        
        log.info( "num file : %s" ,self.numFile );
        #self.totalPage = int( math.ceil   (size/float(self.page_size)) ); # + 1;
        self.totalPage = int( math.ceil   (self.size_in_file/float(self.page_size)) ); # + 1;
        
        log.info( "self.totalPage : %s" ,self.totalPage );
        
        
        from datetime import datetime
        
        for npage in range(0,self.numFile):
        
            startTime  = datetime.now();
            #step 3 replace name to id ex: prefix, sex, country, city, province, countryname
        
            file  = 'insert_sql-'+ str(npage) +'-' +  startTime.strftime("%Y-%m-%d-%H-%M-%S") + '.sql';
            
            
            
             
            
            f = open(file, 'w');
            rows = 1;
            for num in range(0,self.totalPage):
                log.info( "%s to %s total %s" ,num , (num*self.page_size), self.page_size);
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
                    #muser.saveObject(email,self.mapprefix); 
                    
                    email.date_time =start;
                    
                    sql = muser.insertToSQL(email,self.mapprefix);
                    
                    f.write(sql);
                    f.write("\n");
                    
                    email.id_user = muser.ID_USER
                    #log.info( "ID USER : " +  str(email.id_user));
                    #log.info(email.email);
                    #step 4.2 insert data to table sys_m_user_lang
                    muserLang = model.MUserLang();
                    #muserLang.saveObject(email); 
                    sql = muserLang.saveObject(email);
                    f.write(sql);
                    f.write("\n");
                    
                    
                    #step 4.3 insert data to table sys_m_user_map_role
                    muserRole = model.MUserMapRole();
                    sql = muserRole.saveObject(email); 
                    f.write(sql);
                    f.write("\n");
                    
                    #step 4.4 insert data to table job_m_user_email
                    muserEmail = model.MUserEmail();
                    sql =muserEmail.saveObject(email); 
                    f.write(sql);
                    f.write("\n");
                    
                    #step 4.5 insert data to table job_m_user_general_setting
                    muserGeneral = model.MUserGeneralSetting();
                    sql = muserGeneral.saveObject(email,self.mapprefix,self.mapprovince); 
                    f.write(sql);
                    f.write("\n");
                    
                    #step 4.6 insert data to table job_m_user_phone
                    muserPhone = model.MUserPhone(); 
                    sql = muserPhone.saveObject(email, self.mapprovince); 
                    f.write(sql);
                    f.write("\n");
                    
                    muserMapPhone = model.MSysMUserMapPhone();
                    sql = muserMapPhone.saveObject(email ); 
                    f.write(sql);
                    f.write("\n");
                    
                    #step 4.6 insert data to table job_m_user_phone
                    muserAddres = model.MUserAddres();
                    sql = muserAddres.saveObject(email,self.mapprovince,self.mapcity,self.mapcounty); 
                    f.write(sql);
                    f.write("\n");
                    
                    muserMapAddress = model.MSysMUserMapAddres();
                    sql = muserMapAddress.saveObject(email ); 
                    f.write(sql);
                    f.write("\n");
                    
                    #step 4.7 insert data to table job_a applicant
                    mjobAApplicant = model.MJobAApplicant();
                    sql = mjobAApplicant.saveObject(email  );
                    f.write(sql);
                    f.write("\n");
                    
                    mjobAApPiPersonalDatum = model.MJobAApPiPersonalDatum();
                    sql = mjobAApPiPersonalDatum.saveObject(email,self.mapgender );
                    f.write(sql);
                    f.write("\n");
                    
                    mjobAApplicantCertificate = model.MJobAApplicantCertificate();
                    sql = mjobAApplicantCertificate.saveObject(email );
                    f.write(sql);
                    f.write("\n");
                    
                    f.write("-- ---------------"+ str(rows) +"---------------\n" );
                    
                    rows = rows +1;
                    
                    email.updateExported(num);
                    model.transaction.commit();
                    #model.transaction.commit();
            
                    
            f.close();
                
            stopTime  = datetime.now();
            
            #call end 
            self.usedSize = (npage+1) *  self.size_in_file ;
            self.sum = size - self.usedSize;
            if (self.sum < self.size_in_file):
                self.totalPage =  int( math.ceil   (self.sum/float(self.page_size)) );
            
            
            #log.info ( 'size in file  %s ',self.usedSize);
            #log.info ('real size : %s' , (self.sum));
            #log.info ('real totalPage : %s' , (self.totalPage));
            
            
            
            log.info( "finish start : %s to %s" , startTime   , stopTime)