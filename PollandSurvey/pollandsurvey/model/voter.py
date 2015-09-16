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


from sqlalchemy import Table, ForeignKey, Column,and_
from sqlalchemy.types import Unicode,   DateTime, Date, Integer, String, Text,Boolean,BigInteger

from sqlalchemy.util import KeyedTuple;
from sqlalchemy.orm import relation, synonym, Bundle
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.mysql import BIT

from pollandsurvey.model import DeclarativeBase, metadata, DBSession ,QuestionOption,QuestionProject,QuestionProjectType,BasicQuestion
import transaction
__all__ = ['VoterType','Gender','MarriageStatus','Organization','TelephoneType','AddressType','Position','Telephone','Address','Voter','MemberUser', 'Respondents','RespondentReply','ReplyBasicQuestion']

class VoterType(DeclarativeBase):

    __tablename__ = 'sur_m_voter_type'

    id_voter_type =  Column(BigInteger, autoincrement=True, primary_key=True)
    description = Column(String(255),unique=True, nullable=False)
    active  = Column(BIT, nullable=True, default=1)
    
    
    def __init__(self):
        self.active = 1;
        
    def __str__(self):
        return '"%s"' % (self.description )
    
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls) .all();
        
    def to_json(self):
        return {"id_voter_type": self.id_voter_type, "description": self.description, "active": self.active };
    def to_dict(self):
        return {"id_voter_type": self.id_voter_type, "description": self.description, "active": self.active };
 
class Gender(DeclarativeBase):

    __tablename__ = 'sur_m_gender'

    id_gender =  Column(BigInteger, autoincrement=True, primary_key=True)
    description = Column(String(255),unique=True, nullable=False)
    active  = Column(BIT, nullable=True, default=1)
    
    def __init__(self):
        self.active = 1;
        
    def __str__(self):
        return '"%s"' % (self.description )
    
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls) .all();
        
    def to_json(self):
        return {"id_gender": self.id_gender, "description": self.description, "active": self.active };
    def to_dict(self):
        return {"id_gender": self.id_gender, "description": self.description, "active": self.active };
     
class MarriageStatus(DeclarativeBase):

    __tablename__ = 'sur_m_marriage_status'

    id_marriage_status =  Column(BigInteger, autoincrement=True, primary_key=True)
    description = Column(String(255),unique=True, nullable=False)
    active  = Column(BIT, nullable=True, default=1)
    
    def __init__(self):
        self.active = 1;
        
    def __str__(self):
        return '"%s"' % (self.description )
    
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls) .all();
        
    def to_json(self):
        return {"id_marriage_status": self.id_marriage_status, "description": self.description, "active": self.active };
    def to_dict(self):
        return {"id_marriage_status": self.id_marriage_status, "description": self.description, "active": self.active };

class Organization(DeclarativeBase):

    __tablename__ = 'sur_organization'

    id_organization =  Column(BigInteger, autoincrement=True, primary_key=True)
    description = Column(String(255),unique=True, nullable=False)
    active  = Column(BIT, nullable=True, default=1)
    
    def __init__(self):
        self.active = 1;
        
    def __str__(self):
        return '"%s"' % (self.description )
    
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls) .all();
        
    def to_json(self):
        return {"id_organization": self.id_organization, "description": self.description, "active": self.active };
    def to_dict(self):
        return {"id_organization": self.id_organization, "description": self.description, "active": self.active };


class TelephoneType(DeclarativeBase):

    __tablename__ = 'sur_m_telephone_type'

    id_telephone_type =  Column(BigInteger, autoincrement=True, primary_key=True)
    description = Column(String(255),unique=True, nullable=False)
    active  = Column(BIT, nullable=True, default=1)
    
    def __init__(self):
        self.active = 1;
        
    def __str__(self):
        return '"%s"' % (self.description )
    
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls) .all();
        
    def to_json(self):
        return {"id_telephone_type": self.id_telephone_type, "description": self.description, "active": self.active };
    def to_dict(self):
        return {"id_telephone_type": self.id_telephone_type, "description": self.description, "active": self.active };

class AddressType(DeclarativeBase):

    __tablename__ = 'sur_m_address_type'

    id_address_type =  Column(BigInteger, autoincrement=True, primary_key=True)
    description = Column(String(255),unique=True, nullable=False)
    active  = Column(BIT, nullable=True, default=1)
    
    def __init__(self):
        self.active = 1;
        
    def __str__(self):
        return '"%s"' % (self.description )
    
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls) .all();
        
    def to_json(self):
        return {"id_address_type": self.id_address_type, "description": self.description, "active": self.active };
    def to_dict(self):
        return {"id_address_type": self.id_address_type, "description": self.description, "active": self.active };



class Position(DeclarativeBase):

    __tablename__ = 'sur_position'

    id_position =  Column(BigInteger, autoincrement=True, primary_key=True)
    
    id_organization = Column(   BigInteger,ForeignKey('sur_organization.id_organization'), nullable=False, index=True) ;
    organization = relation('Organization', backref='sur_position_id_organization');
    
    position = Column(String(255),unique=True, nullable=False)
    department = Column(String(255),unique=True, nullable=False)
    
    id_voter = Column(   BigInteger,ForeignKey('sur_voter.id_voter'), nullable=False, index=True) ;
    
    
    def __init__(self):
        pass;
        
    def __str__(self):
        return '"%s"' % (self.position )
    
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls) .all();
        
    def to_json(self):
        return {"id_position": self.id_position, "id_organization": self.id_organization, "position": self.position, "department": self.department, "id_voter": self.id_voter };
    def to_dict(self):
        return {"id_position": self.id_position, "id_organization": self.id_organization, "position": self.position, "department": self.department, "id_voter": self.id_voter };

class Telephone(DeclarativeBase):

    __tablename__ = 'sur_telephone'

    id_telephone =  Column(BigInteger, autoincrement=True, primary_key=True)
    
    id_telephone_type = Column(   BigInteger,ForeignKey('sur_m_telephone_type.id_telephone_type'), nullable=False, index=True) ;
    type = relation('TelephoneType', backref='sur_telephone_id_telephone_type');
    
    description = Column(String(255) ) 
    
    id_voter = Column(   BigInteger,ForeignKey('sur_voter.id_voter'), nullable=False, index=True) ;
    
    
    def __init__(self):
        pass;
        
    def __str__(self):
        return '"%s"' % (self.position )
    
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls) .all();
        
    def to_json(self):
        return {"id_telephone": self.id_telephone, "id_telephone_type": self.id_telephone_type, "description": self.description, "id_voter": self.id_voter  };
    def to_dict(self):
        return {"id_telephone": self.id_telephone, "id_telephone_type": self.id_telephone_type, "description": self.description, "id_voter": self.id_voter  };

class Address(DeclarativeBase):

    __tablename__ = 'sur_address'

    id_address =  Column(BigInteger, autoincrement=True, primary_key=True)
    
    id_address_type = Column(   BigInteger,ForeignKey('sur_m_address_type.id_address_type'), nullable=False, index=True) ;
    addresstype = relation('AddressType', backref='sur_address_id_address_type');
    
    description = Column(String(255) ) 
    
    id_voter = Column(   BigInteger,ForeignKey('sur_voter.id_voter'), nullable=False, index=True) ;
    
    
    def __init__(self):
        pass;
        
    def __str__(self):
        return '"%s"' % (self.position )
    
    @classmethod
    def getById(cls,id):
        return DBSession.query(cls).get(id); 
    
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls) .all();
        
    def to_json(self):
        return {"id_address": self.id_address, "id_address_type": self.id_address_type, "description": self.description, "id_voter": self.id_voter  };
    def to_dict(self):
        return {"id_address": self.id_address, "id_address_type": self.id_address_type, "description": self.description, "id_voter": self.id_voter  };
     
class Voter(DeclarativeBase):

    __tablename__ = 'sur_voter'

    id_voter =  Column(BigInteger, autoincrement=True, primary_key=True)
    
    email = Column(String(255) ) 
    prefix = Column(String(255) )
    firstname = Column(String(255) ) 
    lastname = Column(String(255) ) 
    timezone = Column(String(255) ) 
    
    user_id_owner  = Column(   Integer,ForeignKey('tg_user.user_id'), nullable=False, index=True) ;
    user = relation('User', backref='sur_voter_user_id_owner');
    
    
    id_marriage_status = Column(   BigInteger,ForeignKey('sur_m_marriage_status.id_marriage_status'), nullable=False, index=True) ;
    marriagestatus = relation('MarriageStatus', backref='sur_voter_id_marriage_status');
    
    
    
    birthdate =   Column(Date);
    
    id_gender = Column(   BigInteger,ForeignKey('sur_m_gender.id_gender'), nullable=False, index=True) ;
    gender = relation('Gender', backref='sur_voter_id_gender');
    
    create_date =  Column(DateTime, nullable=False, default=datetime.now); 
    
    active  = Column(BIT, nullable=True, default=1);
    respondents = relation('Respondents')  ; 
    maptype = relation('VoterMapType');
    
    
    def __init__(self):
        pass;
        
    def __str__(self):
        return '"%s"' % (self.email )
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
        
    @classmethod
    def getId(cls,id):
        return DBSession.query(cls).get(id); 
    
    @classmethod
    def getAll(cls):
        return DBSession.query(cls) .all();
    
    @classmethod
    def getVoter(cls,user_id_owner,voter_type=5,search=None,page=0, page_size=None):
        query= DBSession.query(cls).join(VoterMapType).filter(cls.user_id_owner ==  str(user_id_owner).decode('utf-8'),
                                                               VoterMapType.id_voter_type ==  str(voter_type).decode('utf-8')
                                                              , VoterMapType.is_send ==  str('1').decode('utf-8')  );
        
        query_total = query;
        
        if page_size:
            query = query.limit(page_size)
        if page: 
            page = 0 if page < 0 else page;
            query = query.offset(page*page_size)
        
        values = query.all();  
        total = query_total.count();
          
        data = [];
        for v in values:
            data.append(v.to_json());
                         
        return values,total;
    
    def to_json(self):
        return {"id_voter": self.id_voter, "email": self.email, "prefix": self.prefix, "firstname": self.firstname , "lastname": self.lastname
                , "timezone": self.timezone, "id_marriage_status": self.id_marriage_status ,  "birthdate": self.birthdate
                , "id_gender": self.id_gender, "create_date": self.create_date};
    def to_dict(self):
        return {"id_voter": self.id_voter, "email": self.email, "prefix": self.prefix, "firstname": self.firstname , "lastname": self.lastname
                , "timezone": self.timezone, "id_marriage_status": self.id_marriage_status ,   "birthdate": self.birthdate
                , "id_gender": self.id_gender, "create_date": self.create_date};
    
        
    @classmethod
    def getVoterByOwnerAndEmail(cls,user_id_owner,email):
        return DBSession.query(cls).filter(cls.user_id_owner ==  str(user_id_owner).decode('utf-8'), cls.email ==  str(email).decode('utf-8') ).first();
    
        
    @classmethod
    def getListVoterByOwner(cls,user_id_owner,voter_type=5,search=None,page=0, page_size=None):
        
        query = DBSession.query(cls).join(VoterMapType).filter(cls.user_id_owner ==  str(user_id_owner).decode('utf-8'), VoterMapType.id_voter_type ==  str(voter_type).decode('utf-8') );#.all();
        query_total = query;
        
        if page_size:
            query = query.limit(page_size)
        if page: 
            page = 0 if page < 0 else page;
            query = query.offset(page*page_size)
        
        values = query.all();  
        total = query_total.count();
          
        data = [];
        for v in values:
            data.append({
                         "id_voter": v.id_voter,
                         "email": v.email,
                         "name" : "%s (%s %s %s)" %(v.email,  str(v.prefix) , str(v.firstname) , str(v.lastname))
                          
                         });
                         
        return data,total;
    @classmethod
    def getListSurveyByMember(cls,user_id,  page=0, page_size=None):
        query = DBSession.query(cls.id_voter,QuestionProject.id_question_project,QuestionProject.name,QuestionOption.id_question_option,QuestionOption.activate_date ,QuestionOption.expire_date ,Respondents.finished,QuestionProjectType.description).\
        join(MemberUser).join(Respondents).join(QuestionOption).join(QuestionProject).join(QuestionProjectType).filter(MemberUser.user_id  == str(user_id).decode('utf-8')) ;
        if page_size:
            query = query.limit(page_size)
        if page: 
            query = query.offset(page*page_size)
        
        values = query.all();
        data = [];
        for v in values:
            data.append({'id_voter':v.id_voter, 
                         'survey_name':v.name, 
                         'id_question_project': v.id_question_project,
                         'id_question_option':v.id_question_option, 
                         'activate_date':v.activate_date.strftime("%d/%m/%Y"),
                         'expire_date':v.expire_date.strftime("%d/%m/%Y"),
                         'duration_date' : str(v.activate_date.strftime("%d/%m/%Y")) + ' - ' + str(v.expire_date.strftime("%d/%m/%Y")),
                         'survey_type' : v.description,
                         'status':v.finished});
        values = None;
        return data;
         
class VoterMapType(DeclarativeBase):
    
    __tablename__ = 'sur_voter_map_type';

    id_voter_map_type =  Column(BigInteger, autoincrement=True, primary_key=True)
    
    id_voter = Column(   BigInteger,ForeignKey('sur_voter.id_voter'), nullable=False, index=True) ;
    voter = relation('Voter', backref='sur_voter_map_type_id_voter');
        
    
    id_voter_type = Column(   BigInteger,ForeignKey('sur_m_voter_type.id_voter_type'), nullable=False, index=True) ;
    votertype = relation('VoterType', backref='sur_voter_map_type_id_voter_type');
    
    is_send   = Column(BIT, nullable=True, default=1);
    create_date =  Column(DateTime, nullable=False, default=datetime.now); 
    update_date =  Column(DateTime, nullable=False ); 
    
    def __init__(self):
        pass;
        
    def __str__(self):
        return '"%s"' % (self.id_voter )
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    
                
class MemberUser(DeclarativeBase):

    __tablename__ = 'sur_member_user'

    id_member_user =  Column(BigInteger, autoincrement=True, primary_key=True)
    
     
    
    user_id = Column(   Integer,ForeignKey('tg_user.user_id'), nullable=False, index=True) ;
    user = relation('User', backref='sur_member_user_user_id');
    
    id_voter = Column(   BigInteger,ForeignKey('sur_voter.id_voter'), nullable=False, index=True) ;
    voter = relation('Voter', backref='sur_member_user_id_voter');
     
    
    create_date =  Column(DateTime, nullable=False, default=datetime.now); 
    update_date =  Column(DateTime, nullable=False, default=datetime.now); 
    
    def __init__(self):
        pass;
        
    def __str__(self):
        return '"%s"' % (self.position )
    
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls) .all();
        
    def to_json(self):
        return {"id_member_user": self.id_member_user, "user_id": self.user_id, "id_voter": self.id_voter
                , "create_date": self.create_date
                , "update_date": self.update_date };
    def to_dict(self):
        return {"id_member_user": self.id_member_user, "user_id": self.user_id, "id_voter": self.id_voter
                , "create_date": self.create_date
                , "update_date": self.update_date };


class Respondents(DeclarativeBase):

    __tablename__ = 'sur_respondents'

    id_respondents =  Column(BigInteger, autoincrement=True, primary_key=True)
    
    id_voter = Column(   BigInteger,ForeignKey('sur_voter.id_voter'), nullable=False, index=True) ;
    voter = relation('Voter', backref='sur_respondents_id_voter');
    
    response_ip = Column(String(255) ) 
    respondent_data =  Column(DateTime, nullable=False, default=datetime.now); 
    
    id_question_project = Column(   BigInteger,ForeignKey('sur_question_project.id_question_project'), nullable=False, index=True) ;
    question_project = relation('QuestionProject', backref='sur_respondents_id_question_project');
    
    id_question_option = Column(   BigInteger,ForeignKey('sur_question_option.id_question_option'), nullable=False, index=True) ;
    question_option = relation('QuestionOption', backref='sur_respondents_id_question_option');
    
    finished  = Column(BIT, nullable=True, default=0);
    finished_date =  Column(DateTime, nullable=True );
    score_exam =   Column(Integer, nullable=True, default=0);
    create_date =  Column(DateTime, nullable=False, default=datetime.now); 
    
    
    def __init__(self):
        pass;
        
    def __str__(self):
        return '"%s"' % (self.position )
    def save(self):
        try:
            DBSession.add(self); 
            DBSession.flush() ;
            print "save Respondents"
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
    
    @classmethod
    def getId(cls,act):
        return DBSession.query(cls).get(act);     
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls) .all();
         
    def to_json(self,moreData = False):
        if not moreData :
            return {"id_respondents": self.id_respondents, "id_voter": self.id_voter, "response_ip": self.response_ip, "id_question_project": self.id_question_project , "id_question_option": self.id_question_option
                , "create_date": self.create_date };
        else:
            return {"id_respondents": self.id_respondents, "email": self.voter.email, "name": str(self.voter.prefix+' '+self.voter.firstname+' '+self.voter.lastname) , "response_ip": self.response_ip, "id_question_project": self.id_question_project , "id_question_option": self.id_question_option
                , "create_date": self.create_date, 'status' : self.finished, 'respondent_data': self.respondent_data };
    def to_dict(self):
        return {"id_respondents": self.id_respondents, "id_voter": self.id_voter, "response_ip": self.response_ip, "id_question_project": self.id_question_project , "id_question_option": self.id_question_option
                , "create_date": self.create_date };
    @classmethod
    def getByVoterIdAndPublicId(cls,idvoter,idpublic):
        return DBSession.query(cls).filter(cls.id_voter == str(idvoter), cls.id_question_option == str(idpublic) ).first();
    
    @classmethod
    def getByVoterAndPublicId(cls,idvoter,idpublic):
        
        return DBSession.query(cls).outerjoin(Voter, Voter.id_voter == cls.id_voter).filter( cls.id_voter == str(idvoter), cls.id_question_option == str(idpublic) ).first();
    
    @classmethod
    def updateScoreByIdRespondents(cls, id_respondents):
        sql = """ update sur_respondents a_respondents
                    set a_respondents.score_exam =  ( 
                    
                     select 
                    SUM(sur_basic_question.answer)  as sum_answer 
                    from   sur_resp_reply  
                      INNER JOIN sur_reply_basic_question on sur_resp_reply.id_resp_reply = sur_reply_basic_question.id_resp_reply
                      INNER JOIN sur_basic_question on (sur_basic_question.id_question = sur_resp_reply.id_question and sur_basic_question.id_basic_data = sur_reply_basic_question.id_basic_data )
                    where sur_resp_reply.id_respondents = a_respondents.id_respondents
                    
                    
                    )
                    where a_respondents.id_respondents = '""" + str(id_respondents) + """'  """;
                    
        result = DBSession.execute(sql);
        DBSession.flush() ;  
        
    @classmethod
    def getListByPublicId(cls,idpublic,page=0, page_size=None):
         
        try:
            query = DBSession.query(cls).outerjoin(Voter, Voter.id_voter == cls.id_voter).filter(   cls.id_question_option == str(idpublic) );
            query_total = query;
            
            if page_size:
                query = query.limit(page_size)
            if page: 
                page = 0 if page < 0 else page;
                query = query.offset(page*page_size)
            
            values = query.all();  
            total = query_total.count();
              
            data = [];
            for v in values:
                data.append(v.to_json(moreData= True));
                             
            return True,data,total;
        except Exception as  e:
            print e;  
            return False, [], 0;#e.__str__();
        
        
         
           
class RespondentReply(DeclarativeBase):

    __tablename__ = 'sur_resp_reply'

    id_resp_reply =  Column(BigInteger, autoincrement=True, primary_key=True)
    
    id_respondents = Column(   BigInteger,ForeignKey('sur_respondents.id_respondents'), nullable=False, index=True) ;
    respondents = relation('Respondents', backref='sur_resp_reply_id_respondents');
    
    id_question = Column(   BigInteger,ForeignKey('sur_question.id_question'), nullable=False, index=True) ;
    question = relation('Question', backref='sur_resp_reply_id_question');
    response_date =  Column(DateTime, nullable=False, default=datetime.now); 
    
    childenAnswer = relation('ReplyBasicQuestion')  ; 
    
    def __init__(self):
        pass;
        
    def __str__(self):
        return '"%s"' % (self.position )
    
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls) .all();
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
            
    def to_json(self):
        return {"id_resp_reply": self.id_resp_reply, "id_respondents": self.id_respondents, "id_question": self.id_question, "response_date": self.response_date  };
    def to_dict(self):
        return {"id_resp_reply": self.id_resp_reply, "id_respondents": self.id_respondents, "id_question": self.id_question, "response_date": self.response_date  };
    
    @classmethod
    def listQuestionForUser(cls,idRespondent): 
        
        return DBSession.query(cls).filter( cls.id_respondents == str(idRespondent)  ).all();

    
    @classmethod
    def createQuestionForUser(cls,listQuestion,idRespondent):
        
        for question in listQuestion:
            res =   RespondentReply();
            res.id_respondents = idRespondent;
            res.id_question = question['id'];
            res.save();
        
    
    @classmethod
    def getByRespondentAndQuestion(cls,idResp,idQuestion):
        return DBSession.query(cls).filter(cls.id_respondents == str(idResp), cls.id_question == str(idQuestion) ).first();
    
    @classmethod
    def getResultByRespondemtAndQuestion(cls,idResp,idQuestion):
        return  DBSession.query(cls.id_question,ReplyBasicQuestion.id_basic_data,BasicQuestion.answer).\
            join(ReplyBasicQuestion).join(BasicQuestion,ReplyBasicQuestion.id_basic_data == BasicQuestion.id_basic_data ).\
            filter(cls.id_respondents ==  str(idResp).decode('utf-8'), cls.id_question ==  str(idQuestion).decode('utf-8') ).first();
                
class ReplyBasicQuestion(DeclarativeBase):

    __tablename__ = 'sur_reply_basic_question'

    id_resp_reply =  Column(BigInteger,ForeignKey('sur_resp_reply.id_resp_reply'), index=True, primary_key=True);
    respondentreply = relation('RespondentReply', backref='sur_reply_basic_question_id_resp_reply');
    
    id_basic_data = Column(   BigInteger,ForeignKey('sur_basic_data.id_basic_data') , index=True, primary_key=True) ;
    question_project_type = relation('BasicData', backref='sur_reply_basic_question_id_basic_data');
     
    answer_text =  Column(String(255) )  
    
    
    def __init__(self):
        pass;
        
    def __str__(self):
        return '"%s"' % (self.position )
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
         
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls) .all();
        
    def to_json(self):
        return {"id_resp_reply": self.id_resp_reply, "id_basic_data": self.id_basic_data, "answer_text": self.answer_text  };
    def to_dict(self):
        return {"id_resp_reply": self.id_resp_reply, "id_basic_data": self.id_basic_data, "answer_text": self.answer_text  };
                
    
      