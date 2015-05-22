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


#from sqlalchemy.sql import func; 
from sqlalchemy import Table, ForeignKey, Column,and_ ,sql
from sqlalchemy.types import Unicode,   DateTime, Date, Integer, String, Text,Boolean,BigInteger,SmallInteger,CHAR,TIMESTAMP

from sqlalchemy.util import KeyedTuple;
from sqlalchemy.orm import relation, synonym, Bundle
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.mysql import BIT
from pollandsurvey.model import DeclarativeBase, metadata, DBSession
import transaction
__all__ = ['SysConfig','EmailTemplate','EmailTemplateType','GroupVariables', 'QuestionType', 'QuestionProjectType' ,'BasicDataType', 'QuestionProject','LanguageLabel','Variables','BasicData','BasicQuestion','BasicTextData' 
           ,'Question', 'QuestionOption', 'BasicMultimediaData','QuestionMedia','QuestionTheme' , 'Invitation','DifficultyLevel' , 'RandomType']





class SysConfig(DeclarativeBase):
    __tablename__ = 'sur_sys_config'

    id_sys_config =  Column(Integer, autoincrement=True, primary_key=True);
    default_code = Column(String(255), nullable=True);
    default_value = Column(String(255), nullable=True);
    default_type_value = Column(String(255), nullable=True);
    code_country =Column(String(3), nullable=True);
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(DateTime, default=datetime.now);
    update_date = Column(DateTime ,onupdate=sql.func.utc_timestamp());
    
    def __init__(self):
        self.active = 1;
        self.create_date =  datetime.now();
    
    @classmethod
    def defaultSystemByCountry(cls,codeCountry='th'):
        return DBSession.query(cls).filter(cls.active == str('1').decode('utf-8'),cls.code_country == str(codeCountry).decode('utf-8')).first();
    
    @classmethod
    def defaultExpireByCountry(cls,codeCountry):
        #expired_activate_code
        pass;
        
class DifficultyLevel(DeclarativeBase):
    __tablename__ = 'sur_fix_difficulty_level';
    
    id_fix_difficulty_level =  Column(Integer, autoincrement=True, primary_key=True);
    description = Column(String(255), nullable=True);
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(DateTime, default=datetime.now);
    update_date = Column(DateTime ,onupdate=sql.func.utc_timestamp());
    
    def __init__(self):
        self.active = 1;
        self.create_date =  datetime.now();
        
    @classmethod
    def getAll(cls,active):
        return DBSession.query(cls).filter(cls.active == str(active).decode('utf-8')).all();
    
class RandomType(DeclarativeBase):
    __tablename__ = 'sur_fix_random_type';
    
    id_fix_random_type =  Column(Integer, autoincrement=True, primary_key=True);
    description = Column(String(255), nullable=True);
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(DateTime, default=datetime.now);
    update_date = Column(DateTime ,onupdate=sql.func.utc_timestamp());
    
    def __init__(self):
        self.active = 1;
        self.create_date =  datetime.now();
        
    @classmethod
    def getAll(cls,active):
        return DBSession.query(cls).filter(cls.active == str(active).decode('utf-8')).all();

class EmailTemplate(DeclarativeBase):
    __tablename__ = 'sur_m_email_template';

    id_email_template =  Column(Integer, autoincrement=True, primary_key=True);
    id_email_template_type =   Column( Integer,ForeignKey('sur_fix_email_template_type.id_email_template_type'), nullable=False, index=True) ;
    email_template_type = relation('EmailTemplateType', backref='sur_m_email_template_id_email_template_type');
    
    sender = Column(String(255), nullable=True);
    subject = Column(String(255), nullable=True);
    content_template = Column(Text, nullable=True);
    language = Column(String(2), nullable=True);
    
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(DateTime, default=datetime.now);
    update_date = Column(DateTime,onupdate=sql.func.utc_timestamp() );
    
    def __init__(self):
        self.active = 1;
        self.create_date =  datetime.now();
        
    @classmethod
    def getTemplateBy(cls,idTemplate):
        return DBSession.query(cls).filter(cls.active == str('1').decode('utf-8'),cls.id_email_template_type == str(idTemplate).decode('utf-8')).first();

class EmailTemplateType(DeclarativeBase):
    __tablename__ = 'sur_fix_email_template_type'

    id_email_template_type =  Column(Integer, autoincrement=True, primary_key=True);
    description = Column(String(255), nullable=True);
    active  = Column(BIT, nullable=True, default=1);
    create_date = Column(DateTime, default=datetime.now);
    update_date = Column(DateTime,onupdate=sql.func.utc_timestamp() );
    
    def __init__(self):
        self.active = 1;
        self.create_date =  datetime.now();
    
    def delete(self):
        DBSession.delete(self); 
        DBSession.flush() ;
        
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
        
    def insertValue(self):
        template = EmailTemplateType();
        template.id_email_template_type = 1;
        template.description = 'forgot password';
        template.active = 1;
        template.create_date = datetime.now();



class Languages(DeclarativeBase):
    __tablename__ = 'sur_m_language'

    id_language =  Column(BigInteger, autoincrement=True, primary_key=True);
    
    seq = Column(SmallInteger, nullable=True);
    code2 = Column(CHAR(2), nullable=True);
    code3 = Column(CHAR(3), nullable=True);
    
    
    
    name = Column(String(255) , nullable=True);
    name_local =  Column(String(255) , nullable=True);
    status =  Column(CHAR(1) , nullable=True, default='A'); 
    create_date  = Column( TIMESTAMP(timezone=True), nullable=True ,default=sql.func.utc_timestamp());
    create_user = Column(String(255) , nullable=True, default='SYSTEM');
    
    update_date = Column(TIMESTAMP(timezone=True), nullable=True,onupdate=sql.func.utc_timestamp() );
    update_user = Column(String(255) , nullable=True );
    
    
    def __init__(self):
        self.active = 1;
    def __str__(self):
        return '"%s"' % (self.default_label )
    
    @classmethod
    def getAll(cls):
        return DBSession.query(cls).filter(cls.status == str('A').decode('utf-8')).all();

class LanguageLabel(DeclarativeBase):
    __tablename__ = 'sur_m_language_label'

    id_language_label =  Column(BigInteger, autoincrement=True, primary_key=True);
    module = Column(String(255), nullable=True);
    default_label = Column(String(255) , nullable=True);
    message_en =  Column(String(255) , nullable=True);
    message_th =  Column(String(255) , nullable=True); 
    active  = Column(BIT, nullable=True, default=1);
    
    def __init__(self):
        self.active = 1;
    def __str__(self):
        return '"%s"' % (self.default_label )
    
    def getLang (self,lang):
        if 'th' == lang:
            return str(self.message_th)  ;
        else:
            return str(self.message_en)  ;
    
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls) .all();
     

class GroupVariables(DeclarativeBase):       
    __tablename__ = 'sur_m_group_variables'

    id_group_variables =  Column(BigInteger, autoincrement=True, primary_key=True)
    name = Column(String(255),unique=True, nullable=False)
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
        
class QuestionType(DeclarativeBase):

    __tablename__ = 'sur_m_question_type'

    id_question_type =  Column(BigInteger, autoincrement=True, primary_key=True)
    description = Column(String(255),unique=True, nullable=False)
    type = Column(String(255),unique=True, nullable=False)
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
    
class QuestionTheme(DeclarativeBase):
    __tablename__ = 'sur_m_question_theme'

    id_question_theme =  Column(BigInteger, autoincrement=True, primary_key=True)
    description = Column(String(255),unique=True, nullable=False)
    template = Column(String(255),unique=True, nullable=False)
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
        return {"id_question_theme": self.id_question_theme, "description": self.description, "active": self.active, "template" : self.template };
    
    def to_dict(self):
        return {"id_question_theme": self.id_question_theme, "description": self.description, "active": self.active, "template" : self.template };
    
class QuestionProjectType(DeclarativeBase):

    __tablename__ = 'sur_m_question_project_type'

    id_question_project_type =  Column(BigInteger, autoincrement=True, primary_key=True)
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
        return {"id_question_project_type": self.id_question_project_type, "description": self.description, "active": self.active };
    def to_dict(self):
        return {"id_question_project_type": self.id_question_project_type, "description": self.description, "active": self.active };
        
class BasicDataType(DeclarativeBase):

    __tablename__ = 'sur_m_basic_data_type'

    id_basic_data_type =  Column(BigInteger, autoincrement=True, primary_key=True)
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
            return DBSession.query(cls).all();
        
    @classmethod
    def getByQuestionId(cls):
        DBSession.query(cls) .join(Member).filter(cls.active == str(act).decode('utf-8')).all();
        pass;
     

     

        
class QuestionProject(DeclarativeBase):

    __tablename__ = 'sur_question_project'

    id_question_project =  Column(BigInteger, autoincrement=True, primary_key=True)
    name = Column(String(255) , nullable=False)
    description = Column(String(255) , nullable=False)
    
    user_id = Column(   BigInteger,ForeignKey('tg_user.user_id'), nullable=False, index=True) ;
    user = relation('User', backref='sur_question_project_user_id');
    
    id_question_project_type = Column(   BigInteger,ForeignKey('sur_m_question_project_type.id_question_project_type'), nullable=False, index=True) ;
    question_project_type = relation('QuestionProjectType', backref='sur_question_project_id_question_project_type');
    
    
    header_message = Column(String(255),  nullable=True) 
    footer_message = Column(String(255),  nullable=True) 
    welcome_text = Column(String(255),  nullable=True) 
    end_text = Column(String(255),  nullable=True) 
    start_date =  Column(DateTime, nullable=False, default=datetime.now);
    end_date =  Column(DateTime, nullable=False, default=datetime.now);
    
    active  = Column(BIT, nullable=True, default=1)
    
    def __init__(self):
        self.active = 1;
        
    def __str__(self):
        return '"%s"' % (self.description )
    
    def save(self):
        try:
            DBSession.add(self); 
            DBSession.flush() ;
            print "save project"
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
    
    @classmethod
    def getId(cls,act):
        return DBSession.query(cls).get(act); 
           
    @classmethod
    def getAllByUser(cls,act=1,userid=0):
        list =[];
        if act is not None:
            list =  DBSession.query(cls).filter(cls.active == str(act).decode('utf-8'),cls.user_id == str(userid).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            list =  DBSession.query(cls).all();
        
        for i in list:
            i.question_project_type;
        return list;
    @classmethod
    def getAll(cls,act):
        list =[];
        if act is not None:
            list =  DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            list =  DBSession.query(cls).all();
        
        for i in list:
            i.question_project_type;
        return list;
   
    @classmethod
    def deleteById(cls,id):
        quest = DBSession.query(cls).filter(cls.id_question_project == str(id) ).delete();
        #DBSession.delete(quest); 
        DBSession.flush() ;
    


    
class Question(DeclarativeBase):

    __tablename__ = 'sur_question'

    id_question =  Column(BigInteger, autoincrement=True, primary_key=True)
    
    id_question_type = Column(   BigInteger,ForeignKey('sur_m_question_type.id_question_type'), nullable=False, index=True) ;
    question_type = relation('QuestionType', backref='sur_question_id_question_type');
    
    id_question_project = Column(   BigInteger,ForeignKey('sur_question_project.id_question_project'), nullable=False, index=True) ;
    project = relation('QuestionProject', backref='sur_question_id_question_project');
    
    user_id = Column(   Integer,ForeignKey('tg_user.user_id'), nullable=False, index=True) ;
    user = relation('User', backref='sur_question_user_id');
    
    id_fix_difficulty_level = Column(   BigInteger,ForeignKey('sur_fix_difficulty_level.id_fix_difficulty_level'), nullable=False, index=True) ;
    difficultylevel = relation('DifficultyLevel', backref='sur_question_id_fix_difficulty_level');
    
    
    question = Column(String(255),  nullable=False);
    help_message = Column(String(255),  nullable=False);
    text_label = Column(String(255),  nullable=False);
    order =  Column(Integer  );
    
    """ relation   """
    child = relation('BasicQuestion');
    validate = relation('QuestionValidation');
    media = relation('QuestionMedia');
    
    active  = Column(BIT, nullable=True, default=1);
    
    def __init__(self):
        self.active = 1;
        
    def __str__(self):
        return '"%s"' % (self.question )
    
    
    def to_json(self):
        
        #{'id':1 ,'seq':1,'question': 'What do you like a color?','type': 'radio', 'answer': answer};
        checkMedia = 0;
        if( self.media):
            checkMedia = 1;
        
        dict  = {"id": self.id_question, 
                 "question": self.question,
                 "help_message": self.help_message,
                 "text_label": self.text_label,
                "seq": self.order ,
                'type': self.question_type.type,
                "answer": [],
                "image" : checkMedia,
                "active": self.active,
                "id_fix_difficulty_level" : self.id_fix_difficulty_level };
                
        child =[];
        if len( self.child ) >0 : 
            for answer in self.child:
                for basicText in  answer.basicData.childenText:                    
                    child.append(basicText.to_json());
                for basicMedia in  answer.basicData.childenMedia:                    
                    child.append(basicMedia.to_json());
        
        dict['answer'] = child;
         
        return dict;
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    @classmethod
    def updateOrderById(cls,order,id):
        try:
            DBSession.query(cls).filter(cls.id_question == id).update({"order": order}) ; # , synchronize_session='evaluate' 
            return True, 'success';
        except IntegrityError as  e:
            print e;  
            return False, 'Cannot delete.';#e.__str__();
        
    @classmethod
    def deleteQuestoin(cls,idQuestion):
        
        
        listBasicQuestion = BasicQuestion.getByQuestionId(idQuestion);
         
        
        try:
            BasicQuestion.deleteByQuestion(idQuestion);
            for basicQuestion in listBasicQuestion:
                idBasicData = basicQuestion.id_basic_data;
                BasicQuestion.deleteData(idBasicData,deleteBasicQuestion=False);
                idBasicData =None;
                
                
            
            QuestionValidation.deleteByQuestion(idQuestion);
            QuestionMedia.deleteByQuestion(idQuestion);
            #delete last
            Question.deleteByQuestion(idQuestion);
            
            return True, 'success';
        except IntegrityError as  e:
            print e;  
            return False, 'Cannot delete.';#e.__str__();
        
    
    
    
    @classmethod
    def deleteByQuestion(cls,idQuestion):
        quest = DBSession.query(cls).filter(cls.id_question == str(idQuestion) ).delete();
        #DBSession.delete(quest); 
        DBSession.flush() ;
        
        #sql = "delete from sur_question where id_question = '" +str(idQuestion) + "'" ;
        #DBSession.execute(sql);
        #DBSession.flush() ;
    
    def delete(self):
       
        for basicq in self.child:
            
            #for childen in basicq.basicData.childenText:
            #    print "delete : BasicTextData : " + str(childen.id_basic_data);                
            #    BasicTextData.deleteById(str(childen.id_basic_data));
                 
            print "delete : BasicQuestion : " + str(basicq.id_question) + " , " +  str(basicq.id_basic_data);
            basicq.delete();
            
            #print "delete : BasicData : " + str(basicq.basicData.id_basic_data);
            #basicq.basicData.delete();
        
        for val in self.validate:
            val.delete();
            
        #DBSession.delete(self); 
        #DBSession.flush() ;
        
        
    
    @classmethod
    def deleteBy(cls,question):    
        id_question = question.id_question;
        basicQuestion = BasicQuestion.getByQuestionId(question.id_question);
        
        sql = """ delete sur_text_data.* from 
                    sur_text_data    LEFT JOIN sur_basic_question on sur_text_data.id_basic_data = sur_basic_question.id_basic_data
                    where 
                         sur_basic_question.id_question = '"""  + str(id_question) + """' """;
        result = DBSession.execute(sql);
        DBSession.flush() ;
        
        sql = """ delete sur_basic_question.* from 
                    sur_basic_question     
                    where 
                 sur_basic_question.id_question = '"""  + str(id_question) + """'   """;
        result = DBSession.execute(sql);
        DBSession.flush() ;
        
        """
        sql = "DELETE FROM sur_basic_question WHERE sur_basic_question.id_question = '"+str(id_question)  + "'"; # AND sur_basic_question.id_basic_data = '"+ str(bq.id_basic_data) + "'" ;
        result = DBSession.execute(sql);
        DBSession.flush() ;
            
        for bq in basicQuestion:
            sql = "delete from sur_text_data where id_basic_data =" +str(bq.id_basic_data) ;
            DBSession.execute(sql);
            DBSession.flush() ;
            
            sql = "DELETE FROM sur_basic_data WHERE sur_basic_data.id_basic_data = '"+ str(bq.id_basic_data)  + "'" ;
            result = DBSession.execute(sql);
            DBSession.flush() ;
            
            transaction.commit();
        sql = "DELETE FROM sur_question_validation WHERE sur_question_validation.id_question = '"+ str(id_question) + "'" ;
        result = DBSession.execute(sql);
        DBSession.flush() ;
        
        sql = "DELETE FROM sur_question WHERE sur_question.id_question = '"+ str(id_question) + "'" ;
        result = DBSession.execute(sql);
        DBSession.flush() ;
        transaction.commit();
        """
        """"
        for basicq in question.child:
            for childen in basicq.basicData.childenText:
                sql = "delete from sur_text_data where id_basic_data =" +str(childen.id_basic_data) ;
                result = DBSession.execute(sql);
            DBSession.flush() ;
            sql = "DELETE FROM sur_basic_question WHERE sur_basic_question.id_question = '"+str(basicq.id_question) + "' AND sur_basic_question.id_basic_data = '"+ str(basicq.id_basic_data) + "'" ;
            result = DBSession.execute(sql);
            DBSession.flush() ;
            
            sql = "DELETE FROM sur_basic_data WHERE sur_basic_data.id_basic_data = '"+ str(basicq.basicData.id_basic_data) + "'" ;
            result = DBSession.execute(sql);
            DBSession.flush() ;
            
            sql = "DELETE FROM sur_question_validation WHERE sur_question_validation.id_question = '"+ str(question.id_question) + "'" ;
            result = DBSession.execute(sql);
            DBSession.flush() ;
            
            sql = "DELETE FROM sur_question WHERE sur_question.id_question = '"+ str(question.id_question) + "'" ;
            result = DBSession.execute(sql);
            DBSession.flush() ;
        """
        
    @classmethod
    def getById(cls,id):
        return DBSession.query(cls).get(id); 
    
    @classmethod
    def getByProjectId(cls,id):
        return DBSession.query(cls).filter(cls.id_question_project == str(id).decode('utf-8')).order_by(cls.order).all(); 
    
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
            #return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls).all();
        
    @classmethod
    def loadJson(cls,parsed_dict):
        question = Question();
         
        question.id_question = parsed_dict.get('id_question');
        question.id_question_type = parsed_dict.get('id_question_type');
        question.id_question_project = parsed_dict.get('id_question_project');
        question.user_id = parsed_dict.get('user_id');
        question.question = parsed_dict.get('question');
        question.help_message = parsed_dict.get('help_message');
        question.text_label = parsed_dict.get('text_label');
        question.order = parsed_dict.get('order');
        question.active = parsed_dict.get('active');
        return question;
        
    @classmethod
    def getQuestionByProjectId(cls,pid):
        datas = [];
        if pid is not None:
            data =  DBSession.query(cls,QuestionType).join(QuestionType).filter(cls.id_question_project == str(pid).decode('utf-8')).order_by(cls.order).all();
            for d,e in data:
                d.question_type_name = e.description;
                datas.append(d); 
        
        return datas;
    
    
    @classmethod
    def updateQuestion(cls):
        pass;
    
    @classmethod
    def createQuestion(cls, values,user_id):
        
        question = Question();
         
        question.question = values.get('question');
        question.help_message = values.get('help_message');
        question.id_question_project = values.get('id_project');
        question.id_question_type = values.get('id_question_type');
        question.text_label = '';
        question.user_id = user_id;
        question.order = 3;
        #question.save();
        
        
        for basic_datas in values.get('datagrid'):
            print basic_datas;
            """"
            basicData = BasicData();
            basicData.id_basic_data_type = 1;
            basicData.save();
            
            basicText = BasicTextData();
            basicText.id_basic_data = basicData.id_basic_data;
            basicText.value = basic_datas.get('value');
            basicText.save();
            
            basicQuestion = BasicQuestion();
            basicQuestion.id_question = question.id_question;
            basicQuestion.id_basic_data = basicData.id_basic_data;
            basicQuestion.answer =    ({True: True, False: False}[ basic_datas.get('value') in 'true']);
            basicQuestion.order = basic_datas.get('seq');
            
            basicQuestion.save();
            """
            
        print "save object";
        
        
        

class Variables(DeclarativeBase):
    __tablename__ = 'sur_m_variables'
    
    
    id_variables =  Column(BigInteger, autoincrement=True, primary_key=True)
    name = Column(String(255) , nullable=False)
    description = Column(String(255) , nullable=True)
    
    id_group_variables = Column(   BigInteger,ForeignKey('sur_m_group_variables.id_group_variables'), nullable=False, index=True) ;
    group_variables = relation('GroupVariables', backref='sur_variables_id_group_variables');
     
    table_jm_ref = Column(String(255) , nullable=True)
    field_jm_ref = Column(String(255) , nullable=True)
    
    
    id_parent = Column(   BigInteger,ForeignKey('sur_m_variables.id_variables'), nullable=True, index=True) ;
    #parrent = relation('Variables', backref='sur_variables_id_variables' , remote_side=['sur_variables.id_variables']); #,
    childen = relation('Variables')  
    
    active  = Column(BIT, nullable=True, default=1)
    
    
    def __init__(self):
        self.active = 1;
        
    def __str__(self):
        return '"%s"' % (self.name )
    
    @classmethod
    def getId(cls,act):
        if act is not None:
            return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls).all();   
        
    @classmethod
    def getAll(cls,act):
        if act is not None:
            return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all(); 
        else:
            return DBSession.query(cls).all();
    
    @classmethod
    def getAllParent(cls,act):
        if act is not None:
            return DBSession.query(cls).filter( and_ (cls.active == str(act).decode('utf-8'),cls.id_parent  == None )  ).all(); 
        else:
            return DBSession.query(cls).all();
        
    def to_json(self):
        
        dict  = {"id_variables": self.id_variables, "name": self.name,"description": self.description,"id_group_variables": self.id_group_variables,
                "group_variables": self.group_variables.name, 
                "table_jm_ref": self.table_jm_ref, 
                "field_jm_ref": self.field_jm_ref, 
                "group_variables": self.group_variables.name,
                "childen": [],
                "active": self.active };
        child =[];
        if len( self.childen ) >0 : 
            for obj in  self.childen:
                child.append(obj.to_json());
        
        dict['childen'] = child;
         
        return dict;

class QuestionValidation(DeclarativeBase):

    __tablename__ = 'sur_question_validation'

    id_question =  Column(BigInteger,ForeignKey('sur_question.id_question'), index=True, primary_key=True);
    quest = relation('Question', backref='sur_question_validation_id_question');
    
    enable_validation  = Column(BIT, nullable=True, default=1);
    message = Column(String(255),  nullable=True);
     
    
    
    #active  = Column(BIT, nullable=True, default=1);
    
    
    def __init__(self):
        pass;
        
    def __str__(self):
        return '"%s"' % (self.message )
    
    @classmethod
    def getId(cls,act):
        if act is not None:
            return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls).all();       
    
    @classmethod
    def deleteByQuestion(cls,idQuestion):
        DBSession.query(cls).filter(cls.id_question == str(idQuestion) ).delete();
        #sql = "delete from sur_question_validation where id_question =" +str(idQuestion) ;
        #DBSession.execute(sql);
        DBSession.flush() ;    
    
    def delete(self):
        DBSession.delete(self); 
        DBSession.flush() ;
        

class QuestionMedia(DeclarativeBase):

    __tablename__ = 'sur_question_media'

    id_question =  Column(BigInteger,ForeignKey('sur_question.id_question'), index=True, primary_key=True);
    quest = relation('Question', backref='sur_question_media_id_question');
    
    value = Column(String(255),  nullable=False);
    media_type  = Column(String(255),  nullable=False);
    media_path_file = Column(String(255),  nullable=False);
     
     
    
    def __init__(self):
        pass;
        
    def __str__(self):
        return '"%s"' % (self.message )
    
    @classmethod
    def getId(cls,act):
        if act is not None:
            return DBSession.query(cls).get(act); 
        else:
            return DBSession.query(cls).all();       
    
    @classmethod
    def deleteByQuestion(cls,idQuestion):
        DBSession.query(cls).filter(cls.id_question == str(idQuestion) ).delete();
        #sql = "delete from sur_question_validation where id_question =" +str(idQuestion) ;
        #DBSession.execute(sql);
        DBSession.flush() ;    
    
    def delete(self):
        DBSession.delete(self); 
        DBSession.flush() ;
        
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
        
class BasicQuestion(DeclarativeBase):   
    __tablename__ = 'sur_basic_question';

    id_question =  Column(BigInteger,ForeignKey('sur_question.id_question'), index=True, primary_key=True);
    question = relation('Question', backref='sur_basic_question_id_question');
    
    id_basic_data = Column(   BigInteger,ForeignKey('sur_basic_data.id_basic_data') , index=True, primary_key=True) ;
    question_project_type = relation('BasicData', backref='sur_basic_data_id_basic_data');
    
    answer   = Column(BIT, nullable=True, default=0);
    order =  Column(BigInteger   ); 
    score =  Column(Integer  , default=0 );
    basicData  = relation('BasicData')  ;  
    
    
    def __init__(self):
        pass;
        
    def __str__(self):
        return '"%s"' % str(self.id_question )
    
    @classmethod
    def getId(cls,act):
        return DBSession.query(cls).get(act);
    
    @classmethod
    def getByQuestionAndBasic(cls,idQuestion,idBasicData):
        return DBSession.query(cls).filter(cls.id_question == str(idQuestion), cls.id_basic_data == str(idBasicData) ).first();
    
    @classmethod
    def deleteByQuestion(cls,idQuestion,idBasicData=None):
        if(idBasicData is not None):
            DBSession.query(cls).filter(cls.id_question == str(idQuestion) , cls.id_basic_data == str(idBasicData)).delete();
        else:
            DBSession.query(cls).filter(cls.id_question == str(idQuestion)  ).delete();
        #sql = "delete from sur_basic_question where id_question =" +str(idQuestion) ;
        #DBSession.execute(sql);
        DBSession.flush() ;
    
    @classmethod
    def deleteData(cls,idBasicData=None,deleteBasicQuestion=True):
        
        try:
            if(deleteBasicQuestion):
                DBSession.query(cls).filter(  cls.id_basic_data == str(idBasicData)).delete();
            
            BasicTextData.deleteById(idBasicData);       
            BasicMultimediaData.deleteById(idBasicData); 
            #delete last
            BasicData.deleteById(idBasicData);
            
            return True, 'success';
        except IntegrityError as  e:
            print e;  
            return False, 'Cannot delete.';#e.__str__();
        
    def delete(self):
        DBSession.delete(self); 
        DBSession.flush() ;
        
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
    

            
    @classmethod
    def getByQuestionId(cls,idQuestion):
        return DBSession.query(cls).filter(cls.id_question == str(idQuestion)  ).all();
    @classmethod
    def getBasicTextById(cls,id):
        data = [];
        if id is not None:
            
            #bn = Bundle("mybundle",BasicTextData.id_basic_data,BasicTextData.value,BasicTextData.multi_line,BasicDataType.description,BasicDataType.id_basic_data_type);
            #data = DBSession.query(bn).join(BasicData).join(BasicDataType).join(BasicTextData).filter(cls.id_question == str(id)).all(); 
            
            #data = DBSession.query(BasicTextData.id_basic_data,BasicTextData.value,BasicTextData.multi_line,BasicDataType.description,BasicDataType.id_basic_data_type).join(BasicData).join(BasicDataType).join(BasicTextData).filter(cls.id_question == str(id)).all(); 
            
            data =  DBSession.query(cls.id_question,cls.score,cls.answer,BasicTextData.id_basic_data,BasicTextData.value,BasicTextData.multi_line,BasicDataType.description,BasicDataType.id_basic_data_type ).join(BasicData).join(BasicTextData).join(BasicDataType).filter(cls.id_question == str(id)).all();
            
            
            #datad = BasicQuestion()._convertBasicTextToJson( data);
             
        return data;
    
    @classmethod
    def getBasicMediaById(cls,id):
        data = [];
        if id is not None:
             
            data =  DBSession.query(cls.id_question,cls.score,cls.answer,BasicMultimediaData.id_basic_data,BasicMultimediaData.value,BasicMultimediaData.media_type,BasicDataType.description,BasicDataType.id_basic_data_type ).join(BasicData).join(BasicMultimediaData).join(BasicDataType).filter(cls.id_question == str(id)).all();
          
           
        return data;
    
    @classmethod
    def convertBasicTextToJson(self,data):
        value = [];
        row =1;
        for d in data:
            i=0;
            v = {};
            for e in d.keys():
                v[ str(e)] = d[i];
                i = i+1;
                
            if (len (v) >0):                
                v['seq'] = str(row) ; 
                value.append(v);   
                row = row +1; 
                
        return value;
             
    
     


class BasicData(DeclarativeBase):

    __tablename__ = 'sur_basic_data'

    id_basic_data =  Column(BigInteger, autoincrement=True, primary_key=True)
    
    id_basic_data_type = Column(   BigInteger,ForeignKey('sur_m_basic_data_type.id_basic_data_type'), nullable=False, index=True) ;
    basic_data_type = relation('BasicDataType', backref='sur_basic_data_id_basic_data_type');
    
    """list childen link """
    childenText = relation('BasicTextData')  ; 
    childenMedia = relation('BasicMultimediaData');
    
    def __init__(self):
        pass;
        
    def __str__(self):
        return '"%s"' % str(self.id_basic_data )
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
        
    def delete(self):
        DBSession.delete(self); 
        DBSession.flush() ;
    
    @classmethod
    def deleteById(cls,idBasicData):
        
        DBSession.query(cls).filter(  cls.id_basic_data == str(idBasicData) ).delete();        
        DBSession.flush() ;
        #DBSession.query(BasicTextData).join(cls).join(BasicQuestion).filter(BasicQuestion.id_question == str(idQuestion) ).delete();
        
        
        #DBSession.query(BasicTextData).filter(  BasicTextData.id_basic_data == str(idQuestion) ).delete();
        
        #DBSession.query(cls).join(BasicData).filter(cls.id_question == str(idQuestion) ).delete();
        #sql = "delete from sur_basic_question where id_question =" +str(idQuestion) ;
        #DBSession.execute(sql);
        #DBSession.flush() ; 
             
class BasicTextData(DeclarativeBase):   
    __tablename__ = 'sur_text_data';

    id_basic_data =  Column(BigInteger,ForeignKey('sur_basic_data.id_basic_data'), index=True, primary_key=True);
    basic_data = relation('BasicData', backref='sur_text_data_id_basic_data');
    
    value = Column(String(255),  nullable=False);
    multi_line  = Column(BIT, nullable=True, default=1) 
    
    
    
    def __init__(self):
        self.multi_line = 0;
        
    def __str__(self):
        return '"%s"' % str(self.id_basic_data )
    
    def to_json(self):
        
        dict  = {"id": self.id_basic_data, 
                 "label": self.value,
                 "multi_line": self.multi_line
                 };
                 
        return dict;
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
        
    def remove(self):
        DBSession.delete(self); 
        DBSession.flush() ;
    
    @classmethod
    def getByBasicDataId(cls,idBasicData):
        return DBSession.query(cls).filter(cls.id_basic_data == str(idBasicData)  ).first();#all();
    
    @classmethod
    def deleteById(cls,idBasicData):
        
        DBSession.query(cls).filter(  cls.id_basic_data == str(idBasicData) ).delete();        
        DBSession.flush() ;
    
     
        
    @classmethod
    def getId(cls,act):
        return DBSession.query(cls).get(act); 
    
    
class QuestionOption(DeclarativeBase):   
    __tablename__ = 'sur_question_option';

    id_question_option =  Column(BigInteger, autoincrement=True, primary_key=True);    
    
    
    id_question_project = Column(   BigInteger,ForeignKey('sur_question_project.id_question_project'), nullable=False, index=True) ;
    project = relation('QuestionProject', backref='sur_question_option_id_question_project');
    
    id_question_theme =   Column(   BigInteger,ForeignKey('sur_m_question_theme.id_question_theme'), nullable=False, index=True) ;
    theme = relation('QuestionTheme', backref='sur_question_option_id_question_theme');
    
    id_question_invitation=   Column(   BigInteger,ForeignKey('sur_question_invitation.id_question_invitation'), nullable=False, index=True) ;
    emailTemplate = relation('Invitation', backref='sur_question_option_id_question_invitation');
    
    id_fix_random_type=   Column(   BigInteger,ForeignKey('sur_fix_random_type.id_fix_random_type'), nullable=False, index=True) ;
    randomType = relation('RandomType', backref='sur_question_option_id_fix_random_type');
    
    
    
    
    name_publication  = Column(String(255),  nullable=True);
    activate_date =  Column(DateTime, nullable=True );
    expire_date =  Column(DateTime, nullable=True );
    
    header_message  =  Column(Text, nullable=True );
    footer_message  =  Column(Text, nullable=True );
    welcome_message  =  Column(Text, nullable=True );
    end_message  =  Column(Text, nullable=True );
    
    send_status = Column(BIT, nullable=True, default=0);
    show_score = Column(BIT, nullable=True, default=0);
    random_answer = Column(BIT, nullable=True, default=1);
    
    redirect_url =   Column(String(255) );
    gen_code =   Column(String(20)   );
    show_navigator = Column(BIT, nullable=True, default=0);
    limit_time  = Column(Integer, nullable=True, default=0);
    create_date =  Column(DateTime, nullable=False, default=datetime.now);
    
    
    def __init__(self):
        #self.create_date  =datetime.now;
        pass;
        
    def __str__(self):
        return "question option"; #'"%s"' % str(self.id_question_option )
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
        
    def remove(self):
        DBSession.delete(self); 
        DBSession.flush() ;
    
    def to_json(self):
        
        dict  = {"id_question_option": self.id_question_option, 
                 "id_question_project": self.id_question_project,
                 "id_question_theme": self.id_question_theme,
                 "theme": self.theme.description ,
                 "template": self.theme.template ,
                 "activate_date": self.activate_date.strftime('%d/%m/%Y') ,
                 "expire_date": self.expire_date.strftime('%d/%m/%Y') ,
                 "header_message": self.header_message ,
                 "footer_message": self.footer_message ,
                 "welcome_message": self.welcome_message ,
                 "end_message": self.end_message ,
                 "redirect_url": self.redirect_url ,
                 "name_publication": self.name_publication,
                 "show_navigator" : self.show_navigator,
                 "id_question_invitation" : self.id_question_invitation,
                 "send_status":self.send_status,
                 "id_fix_random_type":self.id_fix_random_type,
                 "show_score" : self.show_score,
                 "random_answer" : self.random_answer
                 };
                 
        return dict;
    
    
    
    @classmethod
    def updateSendStatus(cls,status,id):
        try:
            DBSession.query(cls).filter(cls.id_question_option == id).update({"send_status": status}) ; # , synchronize_session='evaluate' 
            return True, 'success';
        except IntegrityError as  e:
            print e;  
            return False, 'Cannot delete.';#e.__str__();
    
    @classmethod
    def checkSendStatus(cls,idOption):
        option = DBSession.query(cls).get(idOption);
        
        if option.send_status == 1:
            
            return True;
        
        return False;
    
    @classmethod
    def getByProject(cls,idProject):
        
        option =DBSession.query(cls).filter(cls.id_question_project == str(idProject)  ).all();
        value = [];
        for op in option:
            value.append(op.to_json()); 
        return value;
    
    @classmethod
    def deleteById(cls,id):
        
        
        try:
            print 'id : ' + str(id);
            DBSession.query(cls).filter(  cls.id_question_option == str(id) ).delete();
                    
            DBSession.flush() ;
            
            return True, 'success';
        except AttributeError as e:
            print e;
            return False, 'Cannot delete.';
        except IntegrityError as  e:
            print e;  
            return False, 'Cannot delete.';#e.__str__();
        
     
        
        
    @classmethod
    def getId(cls,act):
        return DBSession.query(cls).get(act); 
     
 
    
    
        
class BasicMultimediaData(DeclarativeBase):   
    __tablename__ = 'sur_multimedia_data';

    id_basic_data =  Column(BigInteger,ForeignKey('sur_basic_data.id_basic_data'), index=True, primary_key=True);
    basic_data = relation('BasicData', backref='sur_multimedia_data_id_basic_data');
    
    value = Column(String(255),  nullable=False);
    media_type  = Column(String(255),  nullable=False);
    media_path_file = Column(String(255),  nullable=False);
    
    
    
    def __init__(self):
        self.multi_line = 0;
        
    def __str__(self):
        return '"%s"' % str(self.value )
    
    def to_json(self):
        
        dict  = {"id": self.id_basic_data, 
                 "label": self.value 
                # , "media_type": self.media_type 
                # ,"media_path_file": self.media_path_file
                 };
                 
        return dict;
    
    def save (self):
        DBSession.add(self); 
        DBSession.flush() ;
        
    def remove(self):
        DBSession.delete(self); 
        DBSession.flush() ;
    
    @classmethod
    def getByBasicDataId(cls,idBasicData):
        return DBSession.query(cls).filter(cls.id_basic_data == str(idBasicData)  ).first();
    
    @classmethod
    def deleteById(cls,idBasicData):
        
        DBSession.query(cls).filter(  cls.id_basic_data == str(idBasicData) ).delete();        
        DBSession.flush() ;   
        
class Invitation(DeclarativeBase):

    __tablename__ = 'sur_question_invitation'

    id_question_invitation =  Column(BigInteger, autoincrement=True, primary_key=True)
    name_content = Column(String(255) )
    from_name = Column(String(255) )
    subject = Column(String(255) )
    id_question_project = Column(   BigInteger,ForeignKey('sur_question_project.id_question_project'), nullable=False, index=True) ;
    question_project = relation('QuestionProject', backref='sur_invitation_id_question_project');
    
    content = Column(Text )
 
    create_date =  Column(DateTime, nullable=False, default=datetime.now); 
    update_date =  Column(DateTime, nullable=False );
    
    def __init__(self):
        pass;
        
    def __str__(self):
        return '"%s"' % (self.position )
    def save(self):
        try:
            DBSession.add(self); 
            DBSession.flush() ;
            print "save project"
            return None;
        except  IntegrityError:
            print "Duplicate entry" 
            return "Duplicate entry"
    
    @classmethod
    def getId(cls,act):
        return DBSession.query(cls).get(act);    
    
    def delete(self):
        DBSession.delete(self); 
        DBSession.flush() ;
    @classmethod
    def deleteById(cls,id):
        #not work , it not delete now
        
        try:
            DBSession.query(cls).filter(  cls.id_question_invitation == str(id) ).delete();
            return True;
            #value = DBSession.query(cls).filter(  cls.id_question_invitation == str(id) ).first();
            #print value;
        except Exception as e:
            print e;
            return False;
        #DBSession.delete(value);
        
          
        #DBSession.flush() ;   
    
    @classmethod
    def getByidProject(cls,idProject,page=0, page_size=None):
         
        
        query = DBSession.query(cls).filter(cls.id_question_project == str(idProject)  );
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
                         
        return data,total;
    
    def to_json(self):
        return {"id_question_invitation": self.id_question_invitation, "from_name": self.from_name, "subject": self.subject, "id_question_project": self.id_question_project, "content": self.content, "create_date": self.create_date,"name_content": self.name_content   };
    def to_dict(self):
        return {"id_question_invitation": self.id_question_invitation, "from_name": self.from_name, "subject": self.subject, "id_question_project": self.id_question_project, "content": self.content, "create_date": self.create_date,"name_content": self.name_content   };
       
          
    