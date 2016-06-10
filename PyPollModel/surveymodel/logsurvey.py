import os
from datetime import datetime
from hashlib import sha256


#from sqlalchemy.sql import func; 
from sqlalchemy import Table, ForeignKey, Column,and_ ,sql
from sqlalchemy.types import Unicode,   DateTime, Date, Integer, String, Text,Boolean,BigInteger,SmallInteger,CHAR,TIMESTAMP

from sqlalchemy.util import KeyedTuple;
from sqlalchemy.orm import relation, synonym, Bundle
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.mysql import BIT
#from pollandsurvey.model import DeclarativeBase, metadata, DBSession
from surveymodel import DeclarativeBase, metadata, DBSession
import transaction
import random; 
__all__ = ['LogSurvey']





class LogSurvey(DeclarativeBase):
    __tablename__ = 'sur_log_survey'

    id_log_survey =  Column(Integer, autoincrement=True, primary_key=True);
    ip_server = Column(String(20), nullable=True);
    ip_client = Column(String(20), nullable=True);
    status  = Column(String(20), nullable=True);
    
    relative_created  = Column(String(10), nullable=True);
    name = Column(String(255), nullable=True);
    log_level = Column(String(20), nullable=True);
    level_text = Column(String(20), nullable=True);
    message = Column(Text, nullable=True);
    file_name = Column(String(255), nullable=True);
    path_name = Column(Text, nullable=True);
    line_no = Column(String(10), nullable=True);
    milliseconds = Column(String(10), nullable=True);
    exception = Column(Text, nullable=True);
    thread = Column(String(10), nullable=True);
    
    current_page = Column(String(255), nullable=True);
    user_name = Column(String(255), nullable=True);
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(DateTime, default=datetime.now);
    #update_date = Column(DateTime ,onupdate=sql.func.utc_timestamp());
    
    def __init__(self):
        self.active = 1;
        self.create_date =  datetime.now();
        
    def save (self):
        
        
        DBSession.add(self); 
        DBSession.flush() ;
    
    @classmethod
    def insert(cls,ip_server=None,status=None,message=None,current_page=None,user_name=None):
        
        log = LogSurvey();
        log.ip_server = ip_server;
        log.status = status;
        log.message = message;
        log.current_page = current_page;
        log.user_name = user_name;
        
        log.save();
        
    @classmethod
    def insertSQL(cls,sql):
        result = DBSession.execute(sql);
        DBSession.flush() ;
        
        
    
    