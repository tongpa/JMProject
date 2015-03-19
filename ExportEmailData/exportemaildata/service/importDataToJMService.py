from exportemaildata import model

from exportemaildata.controllers.utility import Utility

class ImportDataToJMService(object):
    
    utility = Utility();
    def __init__(self):
        self.page =0;
        self.page_size = 2;
        
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
        self.mapcountry = {}; 
        for g in gender: self.mapgender[str(g.name).decode('utf-8')] = g.ref_id_gender_jm;
        for g in prefix: self.mapprefix[str(g.name).decode('utf-8')] = g.ref_id_prefix_jm;
        #for g in prefix: self.mapprefix[g.name] = g.ref_id_prefix_jm;
        
        for g in province: self.mapprovince[str(g.name).decode('utf-8')] = g.ref_id_province_jm;
        for g in city: self.mapcity[str(g.name).decode('utf-8')] = g.ref_id_city_jm;
        for g in county: self.mapcountry[str(g.name).decode('utf-8')] = g.ref_id_county_jm;
         
        
        #step 2 load data email 
        size = model.EmailTemp.getSizeForExport();
        self.totalPage = (size/self.page_size) + 1;
        
        from datetime import datetime
        
        startTime  = datetime.now();
        
        for num in range(0,self.totalPage):
            print "%s to %s" ,num , (num*self.page_size);
            start = datetime.now();
            emailtemps = model.EmailTemp.getData(num, self.page_size);
            
            for email in emailtemps:
                
                muser = model.MUser();
                muser.saveObject(email,self.mapprefix); 
                email.id_user = muser.ID_USER
                print "ID USER : ",  email.id_user;
                
                muserLang = model.MUserLang();
                muserLang.saveObject(email); 
                
            stop  = datetime.now();
            
            print "start : " , start , " to :" , stop
            
            if num > 1:
                break;
        
        stopTime  = datetime.now();
        
        print "finish start : " , startTime , " to :" , stopTime
        #step 3 replace name to id ex: prefix, sex, country, city, province, countryname
        
        
        #step 4 insert data to table 
        
        #step 4.1 insert data to table sys_m_user
        
        #step 4.2 insert data to table sys_m_user_lang
        
        #step 4.3 insert data to table sys_m_user_map_role
        
        #step 4.4 insert data to table job_m_user_email
        
        #step 4.5 insert data to table job_m_user_general_setting
        
        #step 4.6 insert data to table job_m_user_phone
        
        #step 4.7 insert data to table job_m_user_address
        
        
        pass;