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


from sqlalchemy.sql import text, and_
from sqlalchemy import Table, ForeignKey, Column,sql,desc
from sqlalchemy.types import Unicode, Integer, DateTime, String,TIMESTAMP,BigInteger, Date
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.orm import relation, synonym

#from pollandsurvey.model import DeclarativeBase, metadata, DBSession, User
from surveymodel import DeclarativeBase, metadata, DBSession, User 

from surveyobject.mastermodel import MasterBase
 
__all__ = ['UserService','UserGenCode' ,'UserSocialNetwork' , 'ClientProject', 'UserClientAuthen','UserSessionAuthen', 'SocialType'] 

 

class UserService(MasterBase, DeclarativeBase): #User,
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
    post_code = Column(String(10), nullable=True);
    count_send_activate = Column(Integer,default=0 );
    count_send_forgot    = Column(Integer,default=0 );
    
    
    create_date  = Column( TIMESTAMP(timezone=True), nullable=True ,default=sql.func.utc_timestamp());
    create_user = Column(String(255) , nullable=True, default='SYSTEM');
    
    update_date = Column(TIMESTAMP(timezone=True), nullable=True,onupdate=sql.func.utc_timestamp() );
    update_user = Column(String(255) , nullable=True );

    
    def __init__(self,user_id=None, first_name=None, last_name=None, address=None, city=None, country=None, accept_tnc=None, id_gender=None, birthdate=None, language=None, 
                 post_code=None, count_send_activate=None, count_send_forgot=None, create_date=None, create_user=None, update_date=None, update_user=None):
        print "init in UserService"
        super(UserService, self).__init__(DBSession)
        
                
        self.user_id =  user_id
        self.first_name = first_name
        self.last_name = last_name
        self.address  = address
        self.city  = city
        self.country  = country
        self.accept_tnc  = accept_tnc
        self.id_gender =id_gender
        
        self.birthdate     = birthdate
        self.language = language
     
        self.post_code = post_code
        self.count_send_activate = count_send_activate
        self.count_send_forgot    = count_send_forgot
        
        
        self.create_date  = create_date
        self.create_user = create_user
        
        self.update_date = update_date
        self.update_user = update_user
        

    def __repr__(self):
        return '<UserService: name=%s, user_id=%s >' % (
                repr(self.first_name), repr(self.user_id) )

    def __unicode__(self):
        return self.display_name or self.user_name
    
            
    @classmethod
    def getById(cls,user_id):
      
        return DBSession.query(cls).filter(cls.user_id == str(user_id).decode('utf-8') ).first();
    
    @classmethod
    def getByUserId(cls,user_id):
      
        return DBSession.query(User).filter(User.user_id == str(user_id).decode('utf-8') ).first();
    
    def updateGroupUserVoter(self):
       
        result = DBSession.execute('insert into tg_user_group values(:user_id,:group_id)', {'user_id': self.user_id,'group_id':2})
        #DBSession.execute(s, user_id= self.user_id ).fetchall() 
        DBSession.flush() ;
    
    def updateGroupUserCreator(self):
        result = DBSession.execute('insert into tg_user_group values(:user_id,:group_id)', {'user_id': self.user_id,'group_id':4})
        DBSession.flush() ;
 
    def updateByValue1(self,**kw):
        print "update by value"
        for c in self.__table__.columns :
             
            if c.name in kw  and kw[c.name] :
                print "name : %s value : %s" %(c.name, kw[c.name])   
                setattr(self,c.name,kw[c.name] )
                if isinstance(c.type, TIMESTAMP):
                    setattr(self,c.name,   datetime.strptime(kw[c.name] ,  '%d/%m/%Y')  )
        
    
    def updateall(self):
        print "update"
        DBSession.merge(self,load=True)
           
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
    
    @classmethod
    def getByDeactivateCode(cls,code):
        return DBSession.query(cls).filter(cls.id_gen_code_type == str('6').decode('utf-8'),cls.success == str("1").decode('utf-8') ,cls.code == str(code).decode('utf-8')).order_by(desc( cls.create_date )).first();


class UserSocialNetwork(DeclarativeBase): 
    __tablename__ = 'sur_user_social_network';
    
    id_user_social_network = Column(BigInteger, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey(u'tg_user.user_id'))
    id_social_type =  Column(Integer, ForeignKey(u'sur_m_social_type.id_social_type') ) 
    social_type = relation('SocialType', backref='sur_user_social_network_id_social_type');
    provider_user_id = Column(String(100))
    access_token = Column(String(500))
    secret = Column(String(255))
    display_name = Column(String(255))
    profile_url = Column(String(512))
    image_url = Column(String(512))
    rank = Column(Integer)
    expiresin = Column(String(10))
    singed_request = Column(String(700))
     
    access_token_expiry  = Column(DateTime, nullable=False)
    create_date  = Column( TIMESTAMP(timezone=True), nullable=True ,default=sql.func.utc_timestamp());
    create_user = Column(String(255) , nullable=True, default='SYSTEM');
    
    update_date = Column(TIMESTAMP(timezone=True), nullable=True,onupdate=sql.func.utc_timestamp() );
    update_user = Column(String(255) , nullable=True );
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    @classmethod
    def getSocialByUserId(cls,user_id):
        return DBSession.query(SocialType,cls).outerjoin(cls, and_(SocialType.id_social_type == cls.id_social_type,  cls.user_id == str(user_id).decode('utf-8') ) ).all();
    
    @classmethod
    def getByUserId(cls,user_id):
        return DBSession.query(cls).filter(cls.user_id == str(user_id).decode('utf-8') ).all();
    
    
    @classmethod
    def getByUserIdAndSocialId(cls,user_id,socialId):
        return DBSession.query(cls).filter(cls.user_id == str(user_id).decode('utf-8'), cls.id_social_type == str(socialId).decode('utf-8') ).first();
    
    @classmethod
    def getBySocial(cls,social_id, socialtype_id):
        return DBSession.query(cls).filter(cls.provider_user_id == str(social_id).decode('utf-8'), cls.id_social_type == str(socialtype_id).decode('utf-8') ).first();
    
    
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
    
class SocialType(DeclarativeBase):

    __tablename__ = 'sur_m_social_type'

    id_social_type =  Column(BigInteger, autoincrement=True, primary_key=True)
    description = Column(String(255),unique=True, nullable=False)
    active  = Column(BIT, nullable=True, default=1)
    
    def __init__(self):
        self.active = 1;
        
    def __str__(self):
        return '"%s"' % (self.description )
    
    @classmethod
    def getByid(cls,id,act):
        return DBSession.query(cls).filter( cls.id_social_type == str(id).decode('utf-8')   , cls.active == str(act).decode('utf-8') ).first();
    
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls) .all();
        
    def to_json(self):
        return {"id_social_type": self.id_social_type, "description": self.description, "active": self.active };
    def to_dict(self):
        return {"id_social_type": self.id_social_type, "description": self.description, "active": self.active };    
    
 
    