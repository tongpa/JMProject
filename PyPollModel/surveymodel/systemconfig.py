# -*- coding: utf-8 -*-
"""
Auth* related model.

This is where the models used by the authentication stack are defined.

It's perfectly fine to re-use this definition in the PollandSurvey application,
though.

"""
import os
from datetime import datetime
from hashlib import sha256


from sqlalchemy.sql import text
from sqlalchemy import Table, ForeignKey, Column,sql,desc, func
from sqlalchemy.types import Unicode, Integer, DateTime, String,TIMESTAMP,BigInteger,Text
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.orm import relation, synonym
from surveyobject.mastermodel import MasterBase


#from pollandsurvey.model import DeclarativeBase, metadata, DBSession
from surveymodel import DeclarativeBase, metadata, DBSession, User 

 
__all__ = ['SystemEnvironment', 'FixLanguage','FixCountry', 'FixContent' 'ZoneBanner' ] 

 

class SystemEnvironment(MasterBase,DeclarativeBase):
    
    __tablename__ = 'sur_sys_environment'

    id_sys_environment =  Column(BigInteger, autoincrement=True, primary_key=True); 
    environment_key = Column(String(20), nullable=False);
    description = Column(Text, nullable=True);
    active  = Column(String(255), nullable=True);
    
    
    create_date  = Column( TIMESTAMP(timezone=True), nullable=True ,default=sql.func.utc_timestamp());
   
    def __init__(self,id_sys_environment=None, environment_key=None, description=None, active=1):
        super(SystemEnvironment, self).__init__(DBSession)
        
        self.id_sys_environment = id_sys_environment
        self.environment_key = environment_key
        self.description = description        
        if(active is None):
            self.active = 1;

    def __repr__(self):
        return '<SystemEnvironment: key=%s, description=%s >' % (
                repr(self.environment_key), repr(self.description) )

    def __unicode__(self):
        return self.environment_key or self.description
    
    @classmethod
    def getAll(cls,active):
        return DBSession.query(cls).filter(cls.active == str(active).decode('utf-8')).all(); 
    
    @classmethod
    def getbyKey(cls,key):
        return DBSession.query(cls).filter(cls.environment_key  == str(key).decode('utf-8') ,cls.active == str('1').decode('utf-8')).first();
    
    @classmethod
    def getServerUrl(cls):
        env =  DBSession.query(cls).filter(cls.environment_key  == str('SERVER_URL').decode('utf-8') ,  cls.active == str('1').decode('utf-8')).first();
        return env.description;
    
    @classmethod
    def getScoreViewHtml(cls):
        env =  DBSession.query(cls).filter(cls.environment_key  == str('SCORE_VIEW_HTML').decode('utf-8') ,  cls.active == str('1').decode('utf-8')).first();
        return env.description;
    

class FixLanguage(MasterBase, DeclarativeBase): #User,
   
    __tablename__ = 'sur_fix_language'

    id_language =   Column(BigInteger, autoincrement=True, primary_key=True);    
    code = Column(String(5), nullable=True);    
    description = Column(String(255), nullable=True);
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(DateTime, default=datetime.now); 
     
    def __init__(self,id_language=None, code=None, description=None, active=1, create_date = None):
        super(FixLanguage, self).__init__(DBSession)
        
        self.id_language = id_language
        self.code = code
        self.description = description
        self.create_date = create_date        
        if(active is None):
            self.active = 1;
            

    def __repr__(self):
        return '<Language: code_language=%s, description=%s>' % (
                repr(self.code), repr(self.description) )

    def __unicode__(self):
        return self.description  
    
   
    
    @classmethod
    def getAll(cls,active):
        return DBSession.query(cls).filter(cls.active == str(active).decode('utf-8') ).all(); 
    
    
    def to_json(self):
        return {"code": self.code, "description": self.description  };
    
class FixCountry(MasterBase, DeclarativeBase): #User,
   
    __tablename__ = 'sur_fix_country'

    id_country =   Column(BigInteger, autoincrement=True, primary_key=True);    
    code = Column(String(5), nullable=True);    
    description = Column(String(255), nullable=True);
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(DateTime, default=datetime.now); 
     
    
    def __init__(self,id_country=None, code=None, description=None, active=1, create_date = None):
        super(FixCountry, self).__init__(DBSession)
        
        self.id_country = id_country
        self.code = code
        self.description = description
        self.create_date = create_date        
        if(active is None):
            self.active = 1;
             

    def __repr__(self):
        return '<Country: code=%s, description=%s>' % (
                repr(self.code_language), repr(self.description) )

    def __unicode__(self):
        return self.description 
    
    
    @classmethod
    def getAll(cls,active):
        return DBSession.query(cls).filter(cls.active == str(active).decode('utf-8') ).all(); 
    
    
    def to_json(self):
        return {"code": self.code, "description": self.description  };
    
    
 

class ZoneBanner(MasterBase,DeclarativeBase):
    
    __tablename__ = 'sur_sys_zone_banner'

    id_sys_zone_banner =  Column(BigInteger, autoincrement=True, primary_key=True); 
    page_name = Column(String(255), nullable=False);
    zone_number = Column(Integer, nullable=False);
    script_text = Column(Text, nullable=True);
    description = Column(String(255), nullable=True);
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(TIMESTAMP(timezone=True), nullable=True ,default=sql.func.utc_timestamp());
    
    
    def __init__(self,id_sys_zone_banner=None, page_name=None, zone_number=None, script_text=None,
                 description=None, active=1, create_date = None):
        super(ZoneBanner, self).__init__(DBSession)
        
        self.id_sys_zone_banner = id_sys_zone_banner
        self.page_name = page_name
        self.zone_number = zone_number
        self.script_text = script_text
        self.description = description
        self.create_date = create_date        
        if(active is None):
            self.active = 1;
    

    def __repr__(self):
        return '<ZoneBanner: page_name=%s, zone_number=%s >' % (
                repr(self.page_name), repr(self.zone_number) )

    def __unicode__(self):
        return self.page_name 
    
    @classmethod
    def getAll(cls,active):
        return DBSession.query(cls).filter(cls.active == str(active).decode('utf-8')).all(); 
    
    @classmethod
    def getByPageandZone(cls,pageName,ZoneNumber,active=1):
        return DBSession.query(cls).filter( cls.page_name.ilike("%"+pageName+"%") , cls.zone_number == str(ZoneNumber), cls.active == str(active).decode('utf-8')).first(); 
    

class FixContent(MasterBase, DeclarativeBase): #User,
   
    __tablename__ = 'sur_fix_content_type'

    id_content =   Column(BigInteger, autoincrement=True, primary_key=True);    
    description = Column(String(255), nullable=True);
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(DateTime, default=datetime.now); 
    
    def __init__(self,id_content=None, description=None, active=1, create_date = None):
        super(ZoneBanner, self).__init__(DBSession)
        
        self.id_content = id_content
        self.description = description
        self.create_date = create_date        
        if(active is None):
            self.active = 1; 
     

    def __repr__(self):
        return '<Content Type: id_contente=%s, description=%s>' % (
                repr(self.id_content), repr(self.description) )

    def __unicode__(self):
        return self.description  
    
    
    @classmethod
    def getAll(cls,active):
        return DBSession.query(cls).filter(cls.active == str(active).decode('utf-8') ).all(); 
    
    
    def to_json(self):
        return {"id_content": self.id_content, "description": self.description  };  
    
    
class Content(MasterBase, DeclarativeBase): #User,
   
    __tablename__ = 'sur_sys_content'

    id_sys_content =   Column(BigInteger, autoincrement=True, primary_key=True)
    id_content_type =  Column(   BigInteger,ForeignKey('sur_fix_content_type.id_content'), nullable=False, index=True) 
    contentType = relation('FixContent', backref='sur_sys_content_id_content_type');
    id_language =  Column(   BigInteger,ForeignKey('sur_fix_language.id_language'), nullable=False, index=True) 
    language = relation('FixLanguage', backref='sur_sys_content_id_language');
    content =   Column(Text,  nullable=False)  
    start_date = Column(DateTime, nullable=False, default=datetime.now)
    active  = Column(BIT, nullable=True, default=1)
    create_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, nullable=False, onupdate=sql.func.utc_timestamp() )
    
    def __init__(self,id_content=None, description=None, active=1, create_date = None):
        super(ZoneBanner, self).__init__(DBSession)
        
        self.id_content = id_content
        self.description = description
        self.create_date = create_date        
        if(active is None):
            self.active = 1; 
     

    def __repr__(self):
        return '<Content Type: id_contente=%s, description=%s>' % (
                repr(self.id_content), repr(self.description) )

    def __unicode__(self):
        return self.description  
    
    
    @classmethod
    def getAll(cls,active):
        return DBSession.query(cls).filter(cls.active == str(active).decode('utf-8') ).all(); 
    
    @classmethod
    def getByContentType(cls,idContentType,lang='en',active=1):
        return DBSession.query(cls).join(cls.language).\
            filter( func.upper(  FixLanguage.code) ==  func.upper(lang )).\
            filter(cls.active == str(active).decode('utf-8'), cls.id_content_type == str(idContentType ).decode('utf-8')) .first(); 
    
    def to_json(self):
        return {"id_content": self.id_content, "description": self.description  };    
    