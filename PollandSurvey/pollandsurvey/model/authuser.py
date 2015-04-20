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



from sqlalchemy import Table, ForeignKey, Column,sql
from sqlalchemy.types import Unicode, Integer, DateTime, String,TIMESTAMP,BigInteger,BIT
from sqlalchemy.orm import relation, synonym

from pollandsurvey.model import DeclarativeBase, metadata, DBSession, User
from trackproblems.model.configfield import __tablename__
 
__all__ = ['UserService' ] 

class UserService(User):
    """
    User definition.

    This is the user definition used by :mod:`repoze.who`, which requires at
    least the ``user_name`` column.

    """
    __tablename__ = 'sur_m_user'

    user_id =  Column(Integer, ForeignKey(u'tg_user.user_id'), primary_key=True)  
    first_name = Column(String(255), nullable=True);
    last_name = Column(String(255), nullable=True);
    address  = Column(String(255), nullable=True);
    city  = Column(String(255), nullable=True);
    country  = Column(String(255), nullable=True);
    accept_tnc  = Column(String(255), nullable=True);
    
    code_activate = Column(String(255), nullable=True);
    
    count_send_activate = Column(Integer,default=0 );
    count_send_forgot    = Column(Integer,default=0 );
    
    
    create_date  = Column( TIMESTAMP(timezone=True), nullable=True ,default=sql.func.utc_timestamp());
    create_user = Column(String(255) , nullable=True, default='SYSTEM');
    
    update_date = Column(TIMESTAMP(timezone=True), nullable=True,onupdate=sql.func.utc_timestamp() );
    update_user = Column(String(255) , nullable=True );

    def __repr__(self):
        return '<User: name=%s, email=%s, display=%s>' % (
                repr(self.first_name), repr(self.email_address), repr(self.display_name))

    def __unicode__(self):
        return self.display_name or self.user_name

    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
        
class UserGenCode(DeclarativeBase):
    __tablename__ = 'sur_m_user_gen_code';
    
    id_user_gen_code =   Column(BigInteger, autoincrement=True, primary_key=True);
    user_id =  Column(Integer, ForeignKey(u'tg_user.user_id') )  
    code = Column(String(255), nullable=True);
    success = Column(BIT, nullable=True, default=0);
    active =  Column(BIT, nullable=True, default=1);
    expire_date = Column(DateTime, nullable=False);
    create_date = Column(DateTime, nullable=False, default=datetime.now);
    
    
 
