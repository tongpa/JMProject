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
from sqlalchemy.types import Unicode, Integer, DateTime, String,TIMESTAMP,BigInteger
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.orm import relation, synonym

from pollandsurvey.model import DeclarativeBase, metadata, DBSession, User
 

 
__all__ = ['SysTemEnvironment' ] 

 

class SysTemEnvironment(DeclarativeBase):
    
    __tablename__ = 'sur_sys_environment'

    id_sys_environment =  Column(BigInteger, autoincrement=True, primary_key=True); 
    environment_key = Column(String(20), nullable=False);
    description = Column(String(255), nullable=True);
    active  = Column(String(255), nullable=True);
    
    
    create_date  = Column( TIMESTAMP(timezone=True), nullable=True ,default=sql.func.utc_timestamp());
    

    def __repr__(self):
        return '<SysTemEnvironment: key=%s, description=%s >' % (
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
    def getServerUrl(cls):
        env =  DBSession.query(cls).filter(cls.environment_key  == str('SERVER_URL').decode('utf-8') ,  cls.active == str('1').decode('utf-8')).first();
        return env.description;
    
 
    