 
import logging;
import threading;
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText 
import smtplib
from tg.configuration import AppConfig, config
from tg import request
from pollandsurvey import model
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import update

log = logging.getLogger(__name__);
from  survey import LogDBHandler;
__all__ = ['SendSurveyService'] 
class SendSurveyService(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self);
        
        self.__getConnection();
        
        dh = LogDBHandler( config=config,request=request);        
        log.addHandler(dh)
        
        pass;
    
    def __getConnection(self):
        self.some_engine = create_engine(config['sqlalchemy.first.url'] );
        # create a configured "Session" class
        self.Session = sessionmaker(bind=self.some_engine)
        # create a Session
        self.session = self.Session();
    
    def setEmailToVoter(self,model,option,emailtemplate):
        self.model = model;
        self.optionQuestion = option;
        self.emailtemplate = emailtemplate;
        self.id_question_project = self.optionQuestion.id_question_project;
        self.id_question_option= self.optionQuestion.id_question_option;
        
        
    def run(self):
        self.sendToVoter();
        pass;
    
    
    def sendToVoter(self):
        print 'sent to voter'
        self.voters = self.model.Voter.getAll();
        
        
        for v in self.voters:
            #print v;
            self.resp = model.Respondents();
            self.resp.id_voter = v.id_voter;
            self.resp.id_question_project = self.id_question_project;
            self.resp.id_question_option=self.id_question_option;
            
            self.resp.save();
             
        
    