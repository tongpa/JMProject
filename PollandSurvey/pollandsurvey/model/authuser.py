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



from sqlalchemy import Table, ForeignKey, Column,sql,desc
from sqlalchemy.types import Unicode, Integer, DateTime, String,TIMESTAMP,BigInteger
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.orm import relation, synonym

from pollandsurvey.model import DeclarativeBase, metadata, DBSession, User

 
__all__ = ['UserService','UserGenCode' ] 

 

class UserService(User):
    """
    User definition.

    This is the user definition used by :mod:`repoze.who`, which requires at
    least the ``user_name`` column.

    """
    __tablename__ = 'sur_user'

    user_id =  Column(Integer, ForeignKey(u'tg_user.user_id'), primary_key=True)  
    first_name = Column(String(255), nullable=True);
    last_name = Column(String(255), nullable=True);
    address  = Column(String(255), nullable=True);
    city  = Column(String(255), nullable=True);
    country  = Column(String(255), nullable=True);
    accept_tnc  = Column(String(255), nullable=True);
    id_gender =Column(   Integer,ForeignKey('sur_m_gender.id_gender'), nullable=False, index=True) ; 
       
    #code_activate = Column(String(255), nullable=True);
    
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
    
    @classmethod
    def getByUserId(cls,user_id):
        return DBSession.query(cls).filter(cls.user_id == str(user_id).decode('utf-8') ).first();
 
        
class UserGenCode(DeclarativeBase):
    __tablename__ = 'sur_user_gen_code';
    
    id_user_gen_code =   Column(BigInteger, autoincrement=True, primary_key=True);
    user_id =  Column(Integer, ForeignKey(u'tg_user.user_id') );
    id_gen_code_type =  Column(Integer, ForeignKey(u'sur_fix_email_template_type.id_email_template_type'))
    code = Column(String(255), nullable=True);
    success = Column(BIT, nullable=True, default=0);
    count =  Column(Integer,default=0 );
    #active =  Column(BIT, nullable=True, default=1);
    expire_date = Column(DateTime, nullable=False);
    create_date = Column(DateTime, nullable=False, default=datetime.now);
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    @classmethod
    def getUserActivated(cls,user_id):
        return DBSession.query(cls).filter(cls.id_gen_code_type == str('2').decode('utf-8'),cls.success == str("1").decode('utf-8'),cls.user_id == str(user_id).decode('utf-8')).order_by(desc( cls.create_date )).first();    
    @classmethod
    def getByActivateCode(cls,code):
        return DBSession.query(cls).filter(cls.id_gen_code_type == str('2').decode('utf-8'),cls.code == str(code).decode('utf-8')).order_by(desc( cls.create_date )).first();
 
