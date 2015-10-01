# -*- coding: utf-8 -*-
from tgext.mailer import Message, get_mailer, Attachment
from tgext.mailer.mailer import Mailer
import logging;
import threading;
from tg.configuration import AppConfig, config
from tg import request
from pollandsurvey import model
from sqlalchemy import create_engine#, BoundMetaData,Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import update
log = logging.getLogger(__name__);
from logsurvey import LogDBHandler 

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText 
import smtplib

import time
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
__all__ = ['SendMail'] 

Base = declarative_base()

 

class SendMail(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self);
        
        #self.__getConnection();
        
        self.SMTP_SERVER = config['smtp_server'] ;
        self.SMTP_USER = config['smtp_user'] ;
        self.SMTP_PASSWORD = config['smtp_password'] ;
        self.SMTP_PORT= config['smtp_port'] ;
        dh = LogDBHandler( config=config,request=request);        
        log.addHandler(dh)
        
        log.info("Protocol problem: %s", "connection reset" )
        pass;
    
    def __getConnection(self):
        self.some_engine = create_engine(config['sqlalchemy.url'] );
        # create a configured "Session" class
        ##self.Session = sessionmaker(bind=self.some_engine)
        self.Session = sessionmaker( )
        self.Session.configure(bind=self.some_engine)
        Base.metadata.create_all(self.some_engine)
        # create a Session
        self.session = self.Session();
        
        #self.some_engine.echo = True
        #self.metadata = BoundMetaData(self.some_engine)
        
        #self.Emails = Table('sur_send_mail', self.metadata, autoload=True);
    
    def __querySendMail(self):
        valueEmail = model.SendMail.querySendMail(page=0,page_size=50);
        
        return valueEmail
    
    def __updateSendedMail(self,valueEmail):
        #self.session.query(model.SendMail).filter(model.SendMail.id_send_mail == valueEmail.id_send_mail).update({"status": 'F',"sended_date" : datetime.now() }) ;
        
        model.SendMail.updateStatusSended(valueEmail.id_send_mail);
         
        
    def __sendEmailTo(self,receipt,subject,content,senderName):
        
        print "send mail to user ", receipt
        #body = Attachment(data="hello, arthur",transfer_encoding="quoted-printable")
        try:
            html = Attachment(data=content,
                      transfer_encoding="quoted-printable")
            
            message = Message(subject=subject,
                      sender="Poll Surfvey (padungsandy@gmail.com)",
                      recipients=[receipt],
                       
                      html=content)
            
            #mailer = get_mailer(request)
            
            print self.SMTP_SERVER , " " , self.SMTP_USER, " " , self.SMTP_PASSWORD
            
            time.sleep(1);
            mailer = Mailer(host=self.SMTP_SERVER ,
                     port= self.SMTP_PORT, 
                     username= self.SMTP_USER,
                     password=self.SMTP_PASSWORD,
                     tls=True )
             
            mailer.send_immediately(message)
        except Exception as e:
            print e
        print "send mail success"
    
    def __sendEmailTo2(self,receipt,subject,content,senderName):
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject;
            msg['From'] = senderName;
            msg['To'] = receipt;
             
            
            part1 = MIMEText(content, 'html');
            msg.attach(part1)
            
            
            server = smtplib.SMTP(self.SMTP_SERVER,self.SMTP_PORT) 
            server.ehlo()
            server.starttls()
            server.login(self.SMTP_USER, self.SMTP_PASSWORD)
            server.sendmail(self.SMTP_USER, [receipt], msg.as_string())
            
             
            server.quit() 
            
            msg = None;
            server = None;
            part1 = None;
            return True;
        
        except Exception as e:
            print e
            return False;
        #server.close();    
        
    def executeMail(self):
        valueEmail = self.__querySendMail();
        log.info("Protocol problem: %s", "connection reset" ) 
        for email in valueEmail:
            
            result = self.__sendEmailTo2(email.receive, email.subject, email.content, email.sender_name);    
            print email.id_send_mail;
            #email.status = "F";
            #email.sended_date =  datetime.now();
            if result:
                self.__updateSendedMail(email);
                
    def run(self):
        self.executeMail();
                
        
         
    