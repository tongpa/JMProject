# -*- coding: utf-8 -*-
"""Survey Controller"""


from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context,validate,response 
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg.configuration import AppConfig, config
from tg import predicates,RestController
from tg.decorators import override_template;
from pollandsurvey import model
from pollandsurvey.controllers.secure import SecureController
from pollandsurvey.model import DBSession, metadata
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from pollandsurvey.lib.base import BaseController
from pollandsurvey.controllers.error import ErrorController
from pollandsurvey.controllers.utility import Utility

import sys
import json 
import types
from datetime import datetime
from tg import tmpl_context
from webhelpers.markdown import Markdown;  
from posixpath import basename;
import logging;
import random; 
log = logging.getLogger(__name__);

from  survey import LogDBHandler;

__all__ = ['AnswerController']


class AnswerController(BaseController):#RestController): #
    
    def __init__(self):
        self.utility = Utility();
        self.URL_GETDATAQUESTION = '/ans/getDataPreview?idProject={0}';
        self.URL_EXPIRED = '/expired';
        self.URL_THANKYOU = '/thankyou';
        self.URL_HOME = '/';
        self.URL_WELCOME = '/ans/welcome/{0}.html';
        self.URL_REPLY = '/ans/reply/{0}.html';
        self.URL_GOODBYE = '/ans/thankyou/{0}.html';
        self.UPLOAD_DIR = config['path_upload_file'] ;
        
        dh = LogDBHandler( config=config,request=request);        
        log.addHandler(dh)
    
    @expose()
    def _default(self, *args, **kw):
        return 'This page is not ready'
    
    def _before(self, *args, **kw):
        tmpl_context.project_name = 'pollandsurvey'
    
    @expose('pollandsurvey.templates.view.multiquestion')
    def reply(self,id=0,ready='no', **kw):
        reload(sys).setdefaultencoding('utf8')
         
        log.info("id = %s", id);
        log.info("kw = %s", kw);
         
        self.header = '';
        self.footer = '';
        self.nextQuestion ='';
        self.template ='';
        #check link expire
        self.idProject,self.idPublic,self.idVoter,self.redirect = self.__checkExpire(id);
       
        self.respondent,self.redirect = self.__checkRespondentFinished(self.idVoter,self.idPublic,idResp=None);

        self.questionOption,self.redirect = self.__checkOptionExpired(self.idPublic);
        
        
        log.info( "after redirect");
     
        log.info( self.questionOption.id_question_option);
            
        if str(ready).lower() == 'no':    
            #check have welcome page
            if( not self.utility.isEmpty(self.questionOption.welcome_message) ) :
                #redirect('/ans' + '/welcome?id='+ str(self.questionOption.id_question_option) );
                redirect( self.URL_WELCOME.format(str(id))  );
            else:
                self.template = self.questionOption.theme.template;
                override_template(AnswerController.reply, self.template) ;    
                
        elif str(ready).lower() == 'yes':
            self.header = self.questionOption.header_message;
            self.footer = self.questionOption.footer_message;
            self.urlName = self.utility.spritValue(request.path_info,'/');
            self.template = self.questionOption.theme.template
            if(len(self.urlName) >= 1 ) :
                self.nextQuestion = '/' + self.urlName[0] + '/saveQuestion' + '?id='+ str(self.questionOption.id_question_option);
            
            
            if(self.template is not None and len(self.template) > 0):    
                log.info("template used : %s",  self.template );     
                
                override_template(AnswerController.reply, self.template) 
                
            self.ip=request.environ.get("X_FORWARDED_FOR", request.environ["REMOTE_ADDR"]);
            self.browser = request.environ.get('HTTP_USER_AGENT');
            #save reply
            if(self.respondent is None):
                self.respondent = model.Respondents();
                self.respondent.id_voter = self.idVoter;
                self.respondent.response_ip = self.ip ;
                self.respondent.id_question_project = self.idProject;
                self.respondent.id_question_option = self.idPublic;
                self.respondent.finished = 0;
                self.respondent.save();
                 
                 
        return dict(page='view',header = Markdown(self.header).convert() , 
                    footer = Markdown(self.footer).convert()  , 
                    action = self.nextQuestion,template= self.template,
                    #urldata = self.URL_GETDATAQUESTION.format(self.idPublic),
                    urldata = self.URL_GETDATAQUESTION.format(id), 
                    idproject = self.idPublic ,
                    idresp = self.respondent.id_respondents,
                    shownavigator = bool(self.questionOption.show_navigator) ); 
            
    @expose('pollandsurvey.templates.view.welcome')
    def welcome(self,id=0,came_from=lurl('/')):
        reload(sys).setdefaultencoding("utf-8");
         
        
        log.info('preview id : ' + str(id));
        
        self.idProject,self.idPublic,self.idVoter,self.redirect = self.__checkExpire(id);
        
        
        self.welcome_message = '';
        
        self.questionOption,self.redirect = self.__checkOptionExpired(self.idPublic);
                
        self.welcome_message= self.questionOption.welcome_message;
        self.nextQuestion  = '';
         
        self.urlName = self.utility.spritValue(request.path_info,'/');
         
        if(len(self.urlName) >= 1 ) :
            #self.nextQuestion = '/' + self.urlName[0]+ '?id='+ str(self.questionOption.id_question_option);
            #self.nextQuestion = '/' + 'ans/reply/'+  str(self.questionOption.id_question_option);
            self.nextQuestion = self.URL_REPLY.format(id)
            
               
            
        #self.welcome_message
        return dict(page='view', ready = 'yes',welcome_message = Markdown(self.welcome_message).convert(), nextQuestion= self.nextQuestion);
    
    @expose('pollandsurvey.templates.view.goodbye')
    def thankyou(self,id=0,came_from=lurl('/')):
        reload(sys).setdefaultencoding("utf-8");
        
        log.info('preview id : ' + str(id));
        
        self.idProject,self.idPublic,self.idVoter,self.redirect = self.__checkExpire(id);
        
        
        self.goodbye = '';
        
        self.questionOption,self.redirect = self.__checkOptionExpired(self.idPublic);
                
        self.goodbye= self.questionOption.end_message;
        self.nextQuestion  = '';
        self.urlRedirect = ''; 
        self.urlName = self.utility.spritValue(request.path_info,'/');
         
        if(len(self.urlName) >= 1 ) :
          
            self.urlRedirect = self.questionOption.redirect_url
            
    
        return dict(page='goodbye', ready = 'yes',goodbye = Markdown(self.goodbye).convert(),nextQuestion = self.nextQuestion ,urlRedirect= self.nextQuestion);
    
    @expose('json')
    def getDataPreview(self, came_from=lurl('/'),   *args, **kw): 
        reload(sys).setdefaultencoding("utf-8");
        log.info("function getDataPreview");
        
        log.info("args = %s", args);
        log.info("kw = %s ", kw) ;
        
        idProject = kw.get('idProject');
        
        self.idProject=None;
        self.idPublic=None;
        self.idVoter=None;
        self.redirect=None;
        
        self.idProject,self.idPublic,self.idVoter,self.redirect = self.__checkExpire(idProject);
        
        log.info("idProject : %s ", self.idProject);    
        log.info("idPublic : %s ", self.idPublic);
        log.info("idVoter : %s ", self.idVoter);
        log.info("redirect : %s ", self.redirect);
        
        self.respondents  = model.Respondents.getByVoterIdAndPublicId(self.idVoter,self.idPublic);    
        self.questionOption = model.QuestionOption.getId(self.idPublic);
        
        #get old question
        self.listReply = model.RespondentReply.listQuestionForUser(self.respondents.id_respondents);
        
        question = [];
        if( len(self.listReply) >0 ):
            question = self.__getQuestionFromReply(self.listReply,self.questionOption);
             
        else:
            question = self.__getQuestion(self.idPublic,self.questionOption);
            model.RespondentReply.createQuestionForUser(question,self.respondents.id_respondents);
        
        question = self.__randomQuestionAndAnswer(question,self.questionOption);    
        
        self.__setSequenceQuestion(question); 
        
        questions = [];
        questions.append({'id': idProject, 'question' : question});
        
        return dict(questions = questions,timer = self.questionOption.duration_time);
    
    @expose('json')
    def saveQuestion(self, *args, **kw):
        reload(sys).setdefaultencoding("utf-8");
        log.info( "body data");
        log.info( request.body);
        self.df = json.loads(request.body, encoding=request.charset);
        
        self.listAnswer = self.df.get('value');
        
         
        
        self.finished =self.df.get('finished');
        self.redirect = '';
        
         
        
        #from urlparse import urlparse;
        #parsed = urlparse(request.environ.get("HTTP_REFERER" ))
        #print 'path url : ', parsed.path
        if (len(self.listAnswer) >0):
            for value in self.listAnswer:
                 
                if(value):
                    self.idPublic =  value.get('idproject');
                    self.idResp =  value.get('idresp');
                    self.idQuestion = value.get('id');
                    self.values = value.get('value');
                    
                    self.questionOption,self.redirect = self.__checkOptionExpired(self.idPublic,False);
            
                    self.respondent,self.redirect = self.__checkRespondentFinished( None,  None,self.idResp,False);
                    
                    if(self.respondent):
                        self.question = model.Question.getById(self.idQuestion);
                        
                        self.respondent.finished = self.finished;
                        if(self.question):
                            self.respondentreply = model.RespondentReply.getByRespondentAndQuestion(self.idResp,self.idQuestion);
                            if (self.respondentreply is None):
                                #save
                                self.respondentreply = model.RespondentReply();
                                self.respondentreply.id_respondents = self.idResp;
                                self.respondentreply.id_question = self.idQuestion;
                                #self.respondentreply.save();
                                
                                for v in self.values:
                                    self.replyquestion = model.ReplyBasicQuestion(); 
                                    self.replyquestion.id_resp_reply = self.respondentreply.id_resp_reply;
                                    self.replyquestion.id_basic_data = v;
                                #    self.replyquestion.save();
                                
                                
                            else:
                                log.info('user %s do this question : %s',self.idResp,self.idQuestion);
                        else:
                            log.info('find not found question id : : %s',self.idQuestion);
                            
                    else:
                        log.info('find not found respondent id : : %s',self.idResp);
                    
                    
            if(self.finished):     
                self.redirect = self.URL_GOODBYE.format(   self.utility.splitNameWithOutExtention(basename(request.environ.get("HTTP_REFERER" )))  );
               
                    
                    
                    
                    
        """       
            
         
        if(self.value):
            self.idPublic =  self.value.get('idproject');
            self.idResp =  self.value.get('idresp');
            self.idQuestion = self.value.get('id');
            self.values = self.value.get('value');
            print self.values;
            
            #check 
            self.questionOption,self.redirect = self.__checkOptionExpired(self.idPublic,False);
            
            self.respondent,self.redirect = self.__checkRespondentFinished( None,  None,self.idResp,False);
            
            if(self.respondent):
                self.question = model.Question.getById(self.idQuestion);
                
                self.respondent.finished = self.finished;
                if(self.question):
                    self.respondentreply = model.RespondentReply.getByRespondentAndQuestion(self.idResp,self.idQuestion);
                    if (self.respondentreply is None):
                        #save
                        self.respondentreply = model.RespondentReply();
                        self.respondentreply.id_respondents = self.idResp;
                        self.respondentreply.id_question = self.idQuestion;
                        self.respondentreply.save();
                        
                        for v in self.values:
                            self.replyquestion = model.ReplyBasicQuestion(); 
                            self.replyquestion.id_resp_reply = self.respondentreply.id_resp_reply;
                            self.replyquestion.id_basic_data = v;
                            self.replyquestion.save();
                        
                        
                    else:
                        log.info('user %s do this question : %s',self.idResp,self.idQuestion);
                else:
                    log.info('find not found question id : : %s',self.idQuestion);
                    
            else:
                log.info('find not found respondent id : : %s',self.idResp);
            
            if(self.finished):     
                self.redirect = self.URL_GOODBYE.format(   self.utility.splitNameWithOutExtention(basename(request.environ.get("HTTP_REFERER" )))  );
        """        
        return dict(success = True,redirect = self.redirect, finished = self.finished  );
    
    
    def __checkExpire(self,id):
        #sprint 10.2.1.0.html     idproject.idpublic.idvoter.
        self.value = self.utility.spritValue(id,'.');
         
        self.idProject =0;
        self.idPublic = 0;
        self.idVoter = 0;
        
        self.redirect = '';
        
        
        
        if(len(self.value)  == 4):
            self.idProject =self.value[0];
            self.idPublic = self.value[1];
            self.idVoter = self.value[2];
        else:
            self.idProject =None;
            self.idPublic = None;
            self.idVoter = None;
            
            log.info('parameter not have 4 parameter : %s', ','.join(self.value));
            self.redirect = self.URL_EXPIRED;
            redirect(self.URL_EXPIRED) ;
        
        self.voter = model.Voter.getId(self.idVoter);
        if(self.voter is None):
            log.info('find not voter in id : %s',self.idVoter);
            self.redirect = self.URL_HOME;
            redirect(self.URL_HOME) ;
        
        self.project = model.QuestionProject.getId(self.idProject);
        if(self.project is None):
            log.info('find not project in id project : %s',self.idProject);
            self.redirect = self.URL_HOME;
            redirect(self.URL_HOME) ;
            
        return self.idProject,self.idPublic,self.idVoter, self.redirect;
            
    def __checkOptionExpired(self,idPublic,isRedirect = True):
        #print 'public option id ',idPublic;
        self.questionOption = model.QuestionOption.getId( idPublic);           
        self.redirect = '';
        if  self.questionOption is None or ( not self.utility.isActiveFromDate(None,self.questionOption.activate_date,self.questionOption.expire_date) ):
            self.redirect = self.URL_EXPIRED;
            if (isRedirect):
                #print 'redirect ',self.URL_EXPIRED; 
                redirect(self.URL_EXPIRED) ;
      
                
        #print 'id option : ', self.questionOption.welcome_message;
        
        return self.questionOption,self.redirect;    
            
    def __checkRespondentFinished(self,idVoter,idPublic,idResp,isRedirect = True):
        self.respondent = None;
        self.redirect = '';
        if(idVoter and idPublic):
            self.respondent = model.Respondents.getByVoterAndPublicId(idVoter,idPublic);
        elif (idResp):
            self.respondent = model.Respondents.getId(idResp);
            
        if(self.respondent  is not None and self.respondent.finished == 1):
            log.info('voter finished in id public : %s',self.idPublic);
            self.redirect = self.URL_THANKYOU;
            if (isRedirect):
                redirect(self.URL_THANKYOU) ;
            
        return self.respondent,self.redirect;
    
    def __getQuestion(self,idPublic,questionOption):
        
        question = [];
        #get Project Option
        
        if self.questionOption :
            #get Question 
            self.listQuestions = model.Question.getByProjectId(questionOption.id_question_project);
            
            
            #get to object json
            for self.question in self.listQuestions:
                question.append(self.question.to_json(randomAnswer = questionOption.random_answer));
            
            
            
            #clear sequence 
               
        return question ;
    
    def __getQuestionFromReply(self,reply,questionOption):
        question = [];
        for re in reply:
            re.question
            question.append(re.question.to_json(randomAnswer= questionOption.random_answer));
        
        return question;
    
    def __randomQuestionAndAnswer(self,question,questionOption):
        #option Randon Question
        if( questionOption.id_fix_random_type == 2):
            question = random.sample(question,len(question));#,self.questionOption.use_question_no );
        
        
        question = question[0:questionOption.use_question_no];
            
        return question;
    
    def __setSequenceQuestion(self,question):
        row = 1;
        for q in question:
            q['seq'] = row;
            row = row +1; 
        row =None;
        
        return question;
        
   