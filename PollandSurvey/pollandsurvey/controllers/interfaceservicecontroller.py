from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context,validate ,RestController ,response
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates,controllers;
from tg.decorators import override_template,with_trailing_slash; 
from pollandsurvey import model
from pollandsurvey.controllers.secure import SecureController
from pollandsurvey.model import DBSession, metadata
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController
from tg.configuration import AppConfig, config

  
from pollandsurvey.controllers.error import ErrorController
from  survey import LogDBHandler;
from datetime import datetime,timedelta
#from dateutil.relativedelta import relativedelta

from pollandsurvey.controllers.utility import Utility

import time
import sys
import json 
from collections import namedtuple
 
from  survey import LogDBHandler;
import logging;
from _mysql import NULL
log = logging.getLogger(__name__);
__all__ = ['InterfaceServiceController']


class InterfaceServiceController(RestController):
    
    def __init__(self):
        dh = LogDBHandler( config=config,request=request);        
        log.addHandler(dh)
        self.utility = Utility();
        
    @with_trailing_slash
    @expose('json')
    #@require(predicates.in_any_group('voter','managers', msg=l_('Only for voter')))
    def get_all(self,*args,**kw):
        log.info( "get_all");
        log.info( "args : %s ", args);
        log.info( "kw : %s", kw);
        
        #print len(request.headers);
        
        #for h in request.headers:
        #    print h ,  request.headers[h];
         
        try:
         
            #print "body : " ,request.body;
            if( request.body):
                self.df = json.loads(request.body, encoding=request.charset);
                #print self.df;
                #set keyAuthorize
                self.df['keyAuthorize'] = "#987654321";
                samples = self.df;
            else:
                samples = {u'userName': u'tong', u'keyAuthorize': None, u'password': u'tong', u'dataTestSurfvey': None, u'passKey': u'#13456789'};
        
        except Exception as e:
            log.error(e);
            if kw:
                samples = kw;
                samples['keyAuthorize'] = "#987654321";
            
            #samples = {u'userName': u'tong', u'keyAuthorize': None, u'password': u'tong', u'dataTestSurfvey': None, u'passKey': u'#13456789'};
             
        return samples;#dict(surfveyAuthorize=samples);
    
    @with_trailing_slash
    @expose('json')
    def createTest(self,*args,**kw):
       
        print "args  "  ,args;
        print "kw  " ,kw;
        
        for h in request.headers:
            print "%s , %s "  %(h,request.headers[h]);
            
        self.Keyauthorize = request.headers['Keyauthorize'];
        
        samples = kw;
        if self.Keyauthorize == "#987654321" :
            
            self.userExtenal = model.UseExtenalLink();
            self.userExtenal.id_user =  kw.get("idUser");
            self.userExtenal.user_type =kw.get("userType");
            self.userExtenal.id_test  = kw.get("idTest");
            self.userExtenal.id_theme  = kw.get("idTheme");
            self.userExtenal.no_test  =  kw.get("noTest");
            self.userExtenal.user_name  =  kw.get("userName");
            self.userExtenal.save();
            
            #x = json.loads(kw, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            
            
            #1 create public
            self.defaultOption = model.QuestionOption.getByProjectDefault(self.userExtenal.id_test,'1');
            if(self.defaultOption is None):
                print "defaultOption is null"
                self.defaultOption = model.QuestionOption();  
            
            self.option = model.QuestionOption();   
            
                 
            self.option.id_question_project = self.defaultOption.id_question_project;        
            self.option.id_question_theme = self.defaultOption.id_question_theme; 
            
            self.option.name_publication = str(self.defaultOption.name_publication) + "-" + str(self.userExtenal.user_name);
            
            
            self.option.id_fix_random_type = self.defaultOption.id_fix_random_type;
            
            self.option.activate_date = self.utility.getStartDate(); 
            
            self.option.expire_date = self.utility.plusDate(self.option.activate_date,365);
           
            
            self.option.id_question_invitation =  self.defaultOption.id_question_invitation;
            self.option.header_message =self.defaultOption.header_message;
            self.option.footer_message = self.defaultOption.footer_message;
            self.option.welcome_message = self.defaultOption.welcome_message;
            self.option.end_message = self.defaultOption.end_message;
            self.option.use_question_no = self.defaultOption.use_question_no;
            self.option.duration_time   = self.defaultOption.duration_time;
            self.option.random_answer = self.defaultOption.random_answer;
            
            self.option.show_navigator = self.defaultOption.show_navigator;      
            self.option.redirect_url = self.defaultOption.redirect_url;
            
            self.option.no_use = self.userExtenal.no_test;
            self.option.save();
            
            self.userExtenal.id_question_option = self.option.id_question_option;
            #2 
            
            samples['idPublic'] = self.option.id_question_option;
            samples['status'] = True;
            samples['message'] = "create suvvess";
            samples['urlTest'] = "create suvvess";
            samples['createDate'] =  self.option.activate_date ;#datetime.now() ; #"2015-06-23 12:02:57" ;#
            samples['expireDate'] = self.option.expire_date;#datetime.now() +   timedelta(days=30 ) ; #"2015-07-23 12:02:57";#
        else : 
            log.warning("Keyauthorize %s is expired" %self.Keyauthorize);
            
            
            samples['status'] = False;
            samples['message'] = "Keyauthorize %s is expired" %self.Keyauthorize;
        
        
        response.headers['KeyAuthorize'] = self.Keyauthorize
            
        return samples;
    
    @with_trailing_slash
    @expose('json')
    def evaluate(self,*args,**kw):
        log.info("evaluate")
        
         
        log.info( "args = %s"  ,args);
        log.info( "kw = %s  " ,kw);
        samples = kw;
        if('Keyauthorize' in request.headers):
            self.Keyauthorize = request.headers['Keyauthorize'];
        else:
            self.Keyauthorize = '0000000000';
            
        print "key authorize : " , self.Keyauthorize;
        if self.Keyauthorize == "#987654321" :
            
            log.info( "idOwnerTest : %s , idTest : %s , idPublic : %s", kw.get("idOwnerTest") , kw.get("idTest"),kw.get("idPublic"));
            
            self.userExtenal = model.UseExtenalLink.getUserLinkBy( kw.get("idOwnerTest"),kw.get("idTest"),kw.get("idPublic"));
            
            if self.userExtenal :
                #create sur_voter
                self.mapExtenal = model.MapVoterExtenalLink.getUserLinkVoterBy(self.userExtenal.id_use_external_link, kw.get("idUser"));
                 
                self.voter = model.Voter;
                if( self.mapExtenal is None or self.mapExtenal.voter is None):
                    log.info("user external is not voter %s",kw.get("email"));
                    self.voter = model.Voter();
                    self.voter.email = kw.get("email");
                    self.voter.prefix = kw.get("idPrefix");
                    self.voter.firstname = kw.get("firstname");
                    self.voter.lastname = kw.get("lastname");
                    self.voter.user_id_owner  = 3 ;
                    self.voter.id_marriage_status =  kw.get("idMarriageStatus");
                    self.voter.birthdate =   kw.get("birthdate");
                    self.voter.id_gender = kw.get("idGender");
                    self.voter.save();
                    
                    self.mapExternalLink = model.MapVoterExtenalLink();
                    self.mapExternalLink.id_use_external_link =  self.userExtenal.id_use_external_link;
                    self.mapExternalLink.id_voter= self.voter.id_voter;
                    self.mapExternalLink. id_user_ref= kw.get("idUser");
                    self.mapExternalLink.save();
                    #self.userExtenal.id_voter = self.voter.id_voter; 
                #create sur_respondents
                
                    self.respondents = model.Respondents();
                    self.respondents.id_voter = self.voter.id_voter;
                    self.respondents.id_question_project = kw.get("idTest");
                    self.respondents.id_question_option  = kw.get("idPublic");
        
                    self.respondents.finished =0;
                    self.respondents.score_exam =0;
                    
                    self.respondents.save();
                #create link
                else:
                    self.voter =  self.mapExtenal.voter;
                print "id voter : %s"  %self.voter.id_voter;
                
                samples['urlTest'] = ("{0}/ans/reply/{1}.{2}.{3}.0.html").format(request.application_url,str(kw.get("idTest")) ,str(kw.get("idPublic")) , str(self.voter.id_voter))  ;

                samples['status'] = True;
                samples['errorCode'] = 'S0001';            
                samples['message'] = "Create Success ";
            else:
                samples['status'] = False;
                samples['errorCode'] = 'E0002';            
                samples['message'] = "Find not found ";
                
        
        else:
            log.error( "Keyauthorize : is not same "  );
        
        response.headers['KeyAuthorize'] = self.Keyauthorize;
        
        return samples;
    
            