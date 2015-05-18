 
import logging;
import threading;
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText 
import smtplib
from tg.configuration import AppConfig, config
from pollandsurvey import model

log = logging.getLogger(__name__);
__all__ = ['SendMailService'] 
class SendMailService(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self);
        self.sendType =0;
        self.SMTP_SERVER = config['smtp_server'] ;
        self.SMTP_USER = config['smtp_user'] ;
        self.SMTP_PASSWORD = config['smtp_password'] ;
    
    
    def run(self):
        if self.sendType == 1:
            self._forgotPassword();
        if self.sendType == 2:
            self._activateEmail();
        pass;
    
    def sendActivate(self,email):
        self.email = email;
        self.sendType =2; 
        
    def sendForgotPassword(self,email):
        self.email = email;
        self.sendType =1;
       
       
    def _activateEmail(self):
        self.__sendEmailByTemplate();
               
    def _forgotPassword(self):
        self.__sendEmailByTemplate();
    
    
    def sentEmail(self,email,template):
        try:
            print "send email";
             
            msg = MIMEMultipart('alternative')
            msg['Subject'] = email.get('subject');
            msg['From'] = email.get('from');
            msg['To'] = email.get('email');
            
            
            part1 = MIMEText(template, 'html');
            msg.attach(part1)
            
            
            server = smtplib.SMTP(self.SMTP_SERVER) 
            server.ehlo()
            server.starttls()
            server.login(self.SMTP_USER, self.SMTP_PASSWORD)
            server.sendmail(self.SMTP_USER, [email.get('email')], msg.as_string())
            server.close();
        except Exception as e:
            log.exception(str(e)); 
    
    def __sendEmailByTemplate(self):
        try:
            print "send email";
            self.forgot_template = model.EmailTemplate.getTemplateBy(self.sendType);
            template = self.forgot_template.content_template;
            for k,v in  self.email.iteritems():
                template = template.replace('[%s]' % k,v)
            
            msg = MIMEMultipart('alternative')
            msg['Subject'] = self.forgot_template.subject;
            msg['From'] = self.forgot_template.sender;
            msg['To'] = self.email.get('email');
            
            part1 = MIMEText(template, 'html');
            msg.attach(part1)
            
            
            server = smtplib.SMTP(self.SMTP_SERVER) 
            server.ehlo()
            server.starttls()
            server.login(self.SMTP_USER, self.SMTP_PASSWORD)
            server.sendmail(self.SMTP_USER, [self.email.get('email')], msg.as_string())
            server.close();
        except Exception as e:
            log.exception(e.value); 
    
        
        
        