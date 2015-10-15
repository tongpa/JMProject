# -*- coding: utf-8 -*-
"""Survey Controller"""

from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context,validate
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from pollandsurvey import model
from pollandsurvey.controllers.secure import SecureController
from pollandsurvey.model import DBSession, metadata
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from pollandsurvey.lib.base import BaseController
from pollandsurvey.controllers.error import ErrorController

import sys;

from tg.configuration import AppConfig, config
from tg import tmpl_context
from pollandsurvey.widget.movie_form import create_movie_form

import logging;
#from model.survey import BasicQuestion
log = logging.getLogger(__name__);
from  logsurvey import LogDBHandler;
__all__ = ['ScriptModelController']


class ScriptModelController(BaseController):
    
    def __init__(self):
        
        dh = LogDBHandler( config=config,request=request);        
        log.addHandler(dh)
        
    @expose()
    def index(self, came_from=lurl('/')):
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login',
                params=dict(came_from=came_from, __logins=login_counter))
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)

        # Do not use tg.redirect with tg.url as it will add the mountpoint
        # of the application twice.
        return HTTPFound(location=came_from)
    
    @expose('json')
    def getVariable (self, *args, **kw):
        variables = model.Variables.getAllParent(1);
        for q in variables:
            for sub in q.childen:
                print "\t\t" +  sub.name;
        #return dict(page ="test",quest = question) ;
        log.info("getVariable");
        return dict(survey=variables , total = len(variables));
    
    @expose('json')
    def getQuestionType(self, *args, **kw):
        questiontype = model.QuestionType.getAll(1);
        
        return dict(survey=questiontype , total = len(questiontype));
    
    @expose('json')
    def getBasicData(self, *args, **kw):
         
        BasicQuestion = model.BasicQuestion.getBasicTextById(kw.get('questionid'));
        BasicQuestion= model.BasicQuestion.convertBasicTextToJson(BasicQuestion);
       
        
        return dict(survey=BasicQuestion , total = len(BasicQuestion));
    
    @expose('json')
    def getBasicMediaData(self, *args, **kw):
        
        BasicQuestion = model.BasicQuestion.getBasicMediaById(kw.get('questionid'));
        BasicQuestion= model.BasicQuestion.convertBasicTextToJson(BasicQuestion);
       
        
        return dict(survey=BasicQuestion , total = len(BasicQuestion));
        
    @expose('json')
    def getQuestionsData(self, *args, **kw):
        pid = kw.get('projectid');
        #print pid;
        question = model.Question.getQuestionByProjectId(pid);
        
        return dict(survey=question , total = len(question));
     
            
    @expose('json')
    def getOptionsProject(self, *args, **kw):
        pid = kw.get('projectid');
        
        self.page = kw.get('page');
        self.start = kw.get('start');
        self.limit = kw.get('limit');    
        
        
        question,total = model.QuestionOption.getByProject(pid,page=int(self.page)-1, page_size=int(self.limit))
        
        #print total;
        return dict(survey=question , total = total);
    
    @expose('json')
    def getOptionTheme(self, *args, **kw):
         
        question = model.QuestionTheme.getAll(1);
        
        return dict(survey=question , total = len(question));
    
    @expose('json')
    def getDefficultyLevel(self, *args, **kw):
         
        question = model.DifficultyLevel.getAll(1);
        
        return dict(survey=question , total = len(question));
    
    @expose('json')
    def getCloseType(self, *args, **kw):
         
        question = model.CloseType.getAll(1);
        
        return dict(survey=question , total = len(question));
    
    @expose('json')
    def getRandomType(self, *args, **kw):
         
        question = model.RandomType.getAll(1);
        
        return dict(survey=question , total = len(question));
    
    
    @expose('json')
    def getLanguages(self,*args, **kw):
        languages = model.Languages.getAll();
        return dict(survey=languages,total=len(languages));
    
    @expose('json')
    @require(predicates.in_any_group('voter','managers', msg=l_('Only for voter')))
    def getVotersData(self, *args, **kw):
        reload(sys).setdefaultencoding("utf-8");
        user =  request.identity['user'];
        
        self.page = kw.get('page');
        self.start = kw.get('start');
        self.limit = kw.get('limit');        
        #print args;
        #print kw;
        
        question,total = model.Voter.getListVoterByOwner(user.user_id,page=int(self.page)-1 ,  page_size=int(self.limit));
   
        
        return dict(survey=question , total = total);
    
    @expose('json')
    @require(predicates.in_any_group('voter','managers', msg=l_('Only for voter')))
    def getInvitationData(self, *args, **kw):
        reload(sys).setdefaultencoding("utf-8");
       
        
        self.page = kw.get('page');
        self.start = kw.get('start');
        self.limit = kw.get('limit');   
        self.projectid = kw.get('projectid');
             
        #print args;
        #print kw;
        
        question,total = model.Invitation.getByidProject(self.projectid,page=int(self.page)-1 ,  page_size=int(self.limit));
   
        
        return dict(survey=question , total = total);
    
    @expose('json')
    @require(predicates.in_any_group('voter','managers', msg=l_('Only for voter')))
    def getVariableTemplateData(self, *args, **kw):
        reload(sys).setdefaultencoding("utf-8");
        question = [];
        question.append({'id':1,'name': 'age'});
        question.append({'id':2,'name': 'gender'});
        
        return dict(survey=question , total = len(question)); 
    
    
    @expose('json')
    @require(predicates.in_any_group('voter','managers', msg=l_('Only for voter')))
    def getInvitationNumberData(self, *args, **kw):
        reload(sys).setdefaultencoding("utf-8");
        user =  request.identity['user'];
        self.idOption = kw.get('idOption');
        self.page = kw.get('page');
        self.start = kw.get('start');
        self.limit = kw.get('limit');        
        #print args;
        #print kw;
        
        result,question,total = model.SendMail.getInvitationNumberByPublicId(self.idOption ,page=int(self.page)-1 ,  page_size=int(self.limit));
        
        
        return dict(survey=question , total = total);
    
    
    @expose('json')
    @require(predicates.in_any_group('voter','managers', msg=l_('Only for voter')))
    def getListTrackVosterData(self, *args, **kw):
        reload(sys).setdefaultencoding("utf-8");
        user =  request.identity['user'];
        self.idOption = kw.get('idOption');
        self.page = kw.get('page');
        self.start = kw.get('start');
        self.limit = kw.get('limit');        
        #print args;
        #print kw;
        
        result,question,total = model.Respondents.getListByPublicId(self.idOption ,page=int(self.page)-1 ,  page_size=int(self.limit));
        
        
        return dict(survey=question , total = total);
    
     
    @expose('json')
    @require(predicates.in_any_group('voter','managers', msg=l_('Only for voter')))
    def getProjectByUser(self,  *args, **kw):
        reload(sys).setdefaultencoding("utf-8");
        
        self.page = kw.get('page');
        self.start = kw.get('start');
        self.limit = kw.get('limit'); 
        
        
        if request.identity:
            user =  request.identity['user']; 
            quest_project,total = model.QuestionProject.getAllByUser(1,user.user_id, page= int(self.page)-1, page_size = int(self.limit));
        else:
            quest_project = [];
            total = 0;  
        log.info("getProjectByUser");
        
         
        
        #for p in quest_project:
        #    print p;
        
        return dict(survey=quest_project , total = total);
    
    
    