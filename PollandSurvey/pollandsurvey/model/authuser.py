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
from sqlalchemy.types import Unicode, Integer, DateTime, String,TIMESTAMP,BigInteger, Date
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.orm import relation, synonym

from pollandsurvey.model import DeclarativeBase, metadata, DBSession, User
 

 
__all__ = ['UserService','UserGenCode' ,'UserSocialNetwork' , 'ClientProject', 'UserClientAuthen','UserSessionAuthen'] 

 

class UserService( DeclarativeBase): #User,
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
    
    birthdate     = Column(Date, nullable=True);
    language = Column(String(255), nullable=True);
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
    
    def updateGroupUserVoter(self):
        sql = "insert into  tg_user_group values ()";
        s = text("insert into tg_user_group values(:user_id,2)");
        
        
        result = DBSession.execute('insert into tg_user_group values(:user_id,:group_id)', {'user_id': self.user_id,'group_id':2})
        #DBSession.execute(s, user_id= self.user_id ).fetchall() 
        DBSession.flush() ;
        
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


class UserSocialNetwork(DeclarativeBase): 
    __tablename__ = 'sur_user_social_network';
    
    id_user_social_network = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey(u'tg_user.user_id'))
    provider_id = Column(String(255))
    provider_user_id = Column(String(255))
    access_token = Column(String(255))
    secret = Column(String(255))
    display_name = Column(String(255))
    profile_url = Column(String(512))
    image_url = Column(String(512))
    rank = Column(Integer)
    
class ClientProject(DeclarativeBase):
    __tablename__ = 'sur_m_client_project';
    
    id_client_project = Column(BigInteger, autoincrement=True, primary_key=True)
    description = Column(String(255), nullable=True);
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(DateTime, default=datetime.now);
    update_date = Column(DateTime,onupdate=sql.func.utc_timestamp() );
    
class UserClientAuthen(DeclarativeBase):
    __tablename__ = 'sur_user_client_authen';
    
    id_user_client_authen = Column(BigInteger, autoincrement=True, primary_key=True)
    
    user_id = Column(Integer, ForeignKey(u'tg_user.user_id'))
    user = relation('User', backref='sur_user_client_authen_user_id');
    
    client_id = Column(String(255), nullable=True);
    client_secret = Column(String(255), nullable=True);
    
    id_client_project = Column(BigInteger, ForeignKey(u'sur_m_client_project.id_client_project'))
    client_project = relation('ClientProject', backref='sur_user_client_authen_id_client_project');
    
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(DateTime, default=datetime.now);
    update_date = Column(DateTime,onupdate=sql.func.utc_timestamp() );
    
    
    @classmethod
    def getUserClientAuthen(cls,client_id,client_secret):
        return DBSession.query(cls).filter(cls.client_id == str(client_id).decode('utf-8'),cls.client_secret == str(client_secret).decode('utf-8'),cls.active == str('1').decode('utf-8')).first();

class UserSessionAuthen(DeclarativeBase):
    __tablename__ = 'sur_user_session_authen';
    
    session_value =  Column(String(255),  primary_key=True);
    
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(DateTime, default=datetime.now);
    expire_date = Column(DateTime, default=datetime.now);
   # update_date = Column(DateTime,onupdate=sql.func.utc_timestamp() );
    
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    @classmethod 
    def createSessionAuthen(cls,session,start,expire):
        userSessionAuthen = UserSessionAuthen();
        userSessionAuthen.session_value = session;
        userSessionAuthen.create_date = start;
        userSessionAuthen.expire_date = expire;
        userSessionAuthen.save();
        
    @classmethod
    def currentSessionAuthen(cls,session):
        
        sql = """ select ( expire_date > NOW() ) as result  from sur_user_session_authen where session_value = :sessionKey limit 1 """;
        
        
        colunmResult = DBSession.execute(text(sql), {'sessionKey' : session} );
        result = -1;
        for row in colunmResult :
            result = row[0];
        
        print "result value : " + str(result);
        if (result <=0):
            return False;
        else:
            return True;
        pass;
    
    
    