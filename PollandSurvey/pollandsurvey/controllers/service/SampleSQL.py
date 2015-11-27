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
__all__ = ['DoCheckin'] 

Base = declarative_base()
import sys

 
   
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s',
                    )
  
    
#handler = logging.StreamHandler(sys.stdout)
#handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s'))

 
 

class DoCheckin(threading.Thread):
    
    def __init__(self,limit=1,offset=0, group=None, target=None, name=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name,verbose=verbose);
        
         
        self.urlDatabase = config['sqlalchemy.url'] ;
        self.__getConnection();
        
        self.SMTP_SERVER = config['smtp_server'] # "smtp.gmail.com" ;
        self.SMTP_PORT= config['smtp_port'] ;
        self.SMTP_USER = config['smtp_user'] ;
        self.SMTP_PASSWORD = config['smtp_password'] ;
        
        self.LIMIT = limit;
        self.OFFSET = offset;
        self.setLoop = True;
         
        
    def __getConnection(self):
        self.some_engine =create_engine(self.urlDatabase , echo=False ); 
        #create_engine("mysql://sa:sa@localhost:3306/pollandsurvey?charset=utf8&use_unicode=0" , echo=False );
        # create a configured "Session" class
        ##self.Session = sessionmaker(bind=self.some_engine)
        Session = sessionmaker( )
        Session.configure(bind=self.some_engine, autocommit=True)
        Base.metadata.create_all(self.some_engine)
        # create a Session
        self.session = Session();
        
        logging.info("getconnection");
    
    
    
    def query (self,limit,offset):
        sql = "select * from sur_send_mail where status = 'W' limit " + str(limit) + " OFFSET "+ str(offset)+  "; ";
        result = self.session.execute(sql)#.fetchall();
        
        logging.info( result);
        
        row = result.fetchall();
        result.close();
         
        
        
        if row:
            for d in row:
                result = self.__sendEmailTo2(d[6], d[5], d[7], d[4]);    
             
                self.update(d[0]);
                logging.info( d[0]);
            
        #self.session.commit();
        
        
        #self.session.flush() ; 
    def update(self,id):
        sql = "update sur_send_mail set status = 'F', sended_date= '" + str(datetime.now()) + "' where id_send_mail = " + str(id);
        result = self.session.execute(sql);
        #result.close();
        self.session.flush() ;
    
    
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
            logging.error(e)
            
            return False;
        
            
    def run(self):
        count =0
        self.limit = 100;
        row =0
        while (self.setLoop):
            logging.info('running with %s and %s', self.LIMIT, self.OFFSET)
            logging.info(self.isAlive());
            self.query(self.LIMIT,self.OFFSET);
            print row
            row = row +1;
            
            time.sleep(30) 
        
         
         
    
    
            
"""        
for i in [1,2]:
    print i;    
    dd = DoCheckin(1,(i-1));
    #dd.query()
    dd.start();
"""  