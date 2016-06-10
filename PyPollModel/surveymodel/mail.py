# -*- coding: utf-8 -*-
"""Sample model module."""

import os
from datetime import datetime
from hashlib import sha256


from sqlalchemy import Table, ForeignKey, Column,and_
from sqlalchemy.types import Unicode,   DateTime, Date, Integer, String, Text,Boolean,BigInteger

from sqlalchemy.util import KeyedTuple;
from sqlalchemy.orm import relation, synonym, Bundle
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.sql import text
#from pollandsurvey.model import DeclarativeBase, metadata, DBSession
from surveymodel import DeclarativeBase, metadata, DBSession
import transaction
__all__ = ['SendMail']



class SendMail(DeclarativeBase):
    __tablename__ = 'sur_send_mail'
    
    id_send_mail =  Column(BigInteger, autoincrement=True, primary_key=True)
    id_question_option=  Column(BigInteger)
    id_voter=  Column(BigInteger)
    user_id=  Column(Integer)
    sender_name = Column(String(255) )
    receive = Column(String(255) )
    
    subject = Column(String(255) )
    content = Column(Text )
    status= Column(String(1) )  #W = wait, S = Send
    
    create_date =  Column(DateTime, nullable=False, default=datetime.now); 
    send_date =  Column(DateTime, default=datetime.now); 
    sended_date =  Column(DateTime); 
    create_user = Column(String(255) )
    
    
     
    
    def __init__(self,id_question_option,id_voter,user_id,sender_name,receive,subject,content):
        self.id_question_option = id_question_option;
        self.id_voter = id_voter;
        self.user_id = user_id;
        self.sender_name = sender_name;
        self.receive = receive;
        self.subject = subject;
        self.content = content; 
        self.status = 'W';
        
    def __str__(self):
        return '"%s"' % (self.position )
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
        
    @classmethod
    def querySendMail(cls,page=0,page_size=None):
        query = DBSession.query(cls).filter(cls.status == str('W')  );
        if page_size:
            query = query.limit(page_size)
        if page: 
            query = query.offset(page*page_size)
        
        value = query.all();
        
         
        
        return value;
    
    @classmethod
    def updateStatusSended(cls,id):
        
        try:
            #sql = "update sur_send_mail set status= 'F', sended_date='" + str(datetime.now()) + "' where id_send_mail = " + str(id);
            #result = DBSession.execute(sql);
            #DBSession.flush() ;            
            #DBSession.execute("UNLOCK TABLES");
            #email = DBSession.query(cls).filter(cls.id_send_mail == id).first();
            #email.status = 'F';
            
            DBSession.query(cls).filter(cls.id_send_mail == id).update({"status": 'F',"sended_date" : datetime.now() }) ;
            DBSession.flush() ;
            
            return True, 'success';
        except Exception as  e:
            print e;  
            return False, 'Cannot delete.';#e.__str__();
        
    @classmethod
    def getInvitationNumberByPublicId(cls,idpublic,page=0, page_size=None):
        result = [];
        try:
            param = {};
            sql = """select  
                        sur_voter.id_voter,
                        sur_voter.email,
                        CONCAT(sur_voter.firstname , ' ' , sur_voter.lastname) as name,
                        count(sur_send_mail.id_send_mail) as no_send,
                        MAX(sur_send_mail.send_date) as last_create_date
                    from 
                    sur_voter LEFT JOIN sur_respondents on sur_voter.id_voter = sur_respondents.id_voter
                    LEFT OUTER JOIN sur_send_mail on (sur_respondents.id_voter = sur_send_mail.id_voter and sur_respondents.id_question_option = sur_send_mail.id_question_option)
                    where sur_respondents.id_question_option = :idpublic 
                    GROUP BY
                        sur_voter.id_voter 
                    """  ;
            param['idpublic'] = idpublic;   
            
            colunmResult = DBSession.execute(text(sql), param );
            count=  str(colunmResult.rowcount);
            
            
            if page_size:
                sql = sql + """  limit :limit """;
                param['limit'] = page_size;
            if page: 
                page = 0 if page < 0 else page;
                sql = sql + """ offset :offset """;
                param['offset'] = str(page*page_size) ; 
                
            colunmResult = DBSession.execute(text(sql), param );
            
            
            for row in colunmResult :
                if row[0]:
                    result.append({'id_voter':row[0],'email': row[1],'name': row[2],'no_send': row[3],'last_create_date': row[4]})
                else:
                    count =0;
                

            
            return True, result, count;
        except Exception as  e:
            print e;  
            return False, result, 0;#e.__str__();
        
        
        
        