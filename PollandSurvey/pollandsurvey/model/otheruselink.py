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
from pollandsurvey.model import DeclarativeBase, metadata, DBSession
import transaction
import random; 
__all__ = ['UseExtenalLink']





class UseExtenalLink(DeclarativeBase):
    __tablename__ = 'sur_use_external_link'

    id_use_external_link =  Column(BigInteger, autoincrement=True, primary_key=True);
    id_user = Column(BigInteger, nullable=True);
    user_name = Column(String(255), nullable=True);
    user_type = Column(String(255), nullable=True);
    id_test  = Column(BigInteger, nullable=True);
    
    no_test  = Column(Integer, nullable=True);
    id_question_option = Column(BigInteger, nullable=True);
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(DateTime, default=datetime.now);
     
    def __init__(self):
        self.active = 1;
        self.create_date =  datetime.now();
        
    def save (self):
        
        DBSession.add(self); 
        DBSession.flush() ;
    
        
    
    