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
from sqlalchemy import Table, ForeignKey, Column,sql,desc
from sqlalchemy.types import Unicode, Integer, DateTime, String,TIMESTAMP,BigInteger,Text
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.orm import relation, synonym

from pollandsurvey.model import DeclarativeBase, metadata, DBSession, User
 

 
__all__ = ['SystemEnvironment', 'FixLanguage','FixCountry', 'ZoneBanner' ] 

 

class SystemEnvironment(DeclarativeBase):
    
    __tablename__ = 'sur_sys_environment'

    id_sys_environment =  Column(BigInteger, autoincrement=True, primary_key=True); 
    environment_key = Column(String(20), nullable=False);
    description = Column(Text, nullable=True);
    active  = Column(String(255), nullable=True);
    
    
    create_date  = Column( TIMESTAMP(timezone=True), nullable=True ,default=sql.func.utc_timestamp());
    

    def __repr__(self):
        return '<SystemEnvironment: key=%s, description=%s >' % (
                repr(self.environment_key), repr(self.description) )

    def __unicode__(self):
        return self.environment_key or self.description
    
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
        
    
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
    

class FixLanguage( DeclarativeBase): #User,
   
    __tablename__ = 'sur_fix_language'

    id_language =   Column(BigInteger, autoincrement=True, primary_key=True);    
    code = Column(String(5), nullable=True);    
    description = Column(String(255), nullable=True);
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(DateTime, default=datetime.now); 
     
     

    def __repr__(self):
        return '<Language: code_language=%s, description=%s>' % (
                repr(self.code), repr(self.description) )

    def __unicode__(self):
        return self.description  
    
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
        
    
    @classmethod
    def getAll(cls,active):
        return DBSession.query(cls).filter(cls.active == str(active).decode('utf-8') ).all(); 
    
    
    def to_json(self):
        return {"code": self.code, "description": self.description  };
    
class FixCountry( DeclarativeBase): #User,
   
    __tablename__ = 'sur_fix_country'

    id_country =   Column(BigInteger, autoincrement=True, primary_key=True);    
    code = Column(String(5), nullable=True);    
    description = Column(String(255), nullable=True);
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(DateTime, default=datetime.now); 
     
     

    def __repr__(self):
        return '<Country: code=%s, description=%s>' % (
                repr(self.code_language), repr(self.description) )

    def __unicode__(self):
        return self.description 
    
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
        
    
    @classmethod
    def getAll(cls,active):
        return DBSession.query(cls).filter(cls.active == str(active).decode('utf-8') ).all(); 
    
    
    def to_json(self):
        return {"code": self.code, "description": self.description  };
    
    
 

class ZoneBanner(DeclarativeBase):
    
    __tablename__ = 'sur_sys_zone_banner'

    id_sys_zone_banner =  Column(BigInteger, autoincrement=True, primary_key=True); 
    page_name = Column(String(255), nullable=False);
    zone_number = Column(Integer, nullable=False);
    script_text = Column(Text, nullable=True);
    description = Column(String(255), nullable=True);
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(TIMESTAMP(timezone=True), nullable=True ,default=sql.func.utc_timestamp());
    
    
    
    

    def __repr__(self):
        return '<ZoneBanner: page_name=%s, zone_number=%s >' % (
                repr(self.page_name), repr(self.zone_number) )

    def __unicode__(self):
        return self.page_name 
    
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
        
    
    @classmethod
    def getAll(cls,active):
        return DBSession.query(cls).filter(cls.active == str(active).decode('utf-8')).all(); 
    
    @classmethod
    def getByPageandZone(cls,pageName,ZoneNumber,active=1):
        return DBSession.query(cls).filter( cls.page_name.ilike("%"+pageName+"%") , cls.zone_number == str(ZoneNumber), cls.active == str(active).decode('utf-8')).first(); 
    
     
    