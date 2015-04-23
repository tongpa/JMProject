# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context,validate  
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates,controllers;
from tg.decorators import override_template; 
from pollandsurvey import model
from pollandsurvey.controllers.secure import SecureController
from pollandsurvey.model import DBSession, metadata
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from pollandsurvey.lib.base import BaseController
from pollandsurvey.controllers.error import ErrorController


from pollandsurvey.controllers.service import SendMailService,RegisterService
from pollandsurvey.controllers.utility import Utility

from pollandsurvey.controllers.register.registercontrol import RegisterController;
from pollandsurvey.controllers.surveycontroller import SurveyController;
from pollandsurvey.controllers.script.loadscriptcontroller import  ScriptController;
from pollandsurvey.controllers.script.loadmodelcontroller import  ScriptModelController;
from pollandsurvey.controllers.script.previewcontroller import  PreviewController;
from pollandsurvey.controllers.script.imagescontroller import ImagesController;
from pollandsurvey.controllers.angularcontroller import AngularController;
from pollandsurvey.controllers.answercontroller import AnswerController;

from tg import tmpl_context
from pollandsurvey.widget.movie_form import create_movie_form 
import time
import sys

import logging;
log = logging.getLogger(__name__);
__all__ = ['RootController']


class RootController(BaseController):
    """
    The root controller for the PollandSurvey application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    secc = SecureController()
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)

    error = ErrorController()
    
    register = RegisterController();
    survey = SurveyController();
    script = ScriptController();
    model = ScriptModelController();
    
    images = ImagesController();
    preview =PreviewController();
    
    ans = AnswerController();
    
    ang = AngularController();
    
    def __init__(self):
        self.sendMailService = SendMailService();
        self.registerService = RegisterService();
        self.utility = Utility();
    def _before(self, *args, **kw):
        tmpl_context.project_name = "pollandsurvey"
    
    @expose('pollandsurvey.templates.metronic')
    def index(self, came_from=lurl('/')):
        return dict(page='metronic') 
    
    
    @expose('pollandsurvey.templates.metronic')
    def home(self, came_from=lurl('/')):
        return dict(page='metronic') 
    
    @expose('pollandsurvey.templates.loginform')
    def login(self, came_from=lurl('/')):
        login_counter = request.environ.get('repoze.who.logins', 0)
         
        if login_counter > 0:
            flash(_('Wrong credentials'), 'warning')
        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from)
        
   
    
    @expose('pollandsurvey.templates.about')
    def about(self, came_from=lurl('/')):
        return dict(page='about', login_counter=str(1),
                    came_from=came_from) 
        
    

    
 

    @expose('pollandsurvey.templates.environ')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(page='environ', environment=request.environ)

     
    
    @expose('pollandsurvey.templates.index')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def manage_permission_only(self, **kw):
        """Illustrate how a page for managers only works."""
        return dict(page='managers stuff')


    @expose('pollandsurvey.templates.index')
    @require(predicates.is_user('editor', msg=l_('Only for the editor')))
    def editor_user_only(self, **kw):
        """Illustrate how a page exclusive for the editor works."""
        return dict(page='editor stuff')

    
    @expose()
    def post_login(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        
        
        if not request.identity:
            log.warning("user cannot login, redirect to login");
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login', params=dict(came_from=came_from, __logins=login_counter))
            
        userid = request.identity['repoze.who.userid'];
        user =  request.identity['user'];
        groups = request.identity['groups'] 
        print groups;
        
        userActive = model.UserGenCode.getUserActivated(user.user_id);
        
        
    
        if(userActive is None and ('managers' not in groups  )):
            log.warning("user cannot login, redirect to login");
            flash(_('Please activate in your email'), 'warning') 
            #request.identity.current.logout();
            login_counter = request.environ.get('repoze.who.logins', 0) ;
            redirect('/logout_handler')#, params=dict(came_from=came_from, __logins=login_counter))
            
        #flash(_('Welcome back, %s!') % userid)
        
        
        
        
        print "login success redirect to %s ", came_from;
        if('/' == came_from):
            if ('voter' in groups):
                redirect('/home');
            if ('creator' in groups):
                redirect('/survey');
        #identity = request.environ.get('repoze.who.identity') 
        
        
        #for key in request.environ:
        #    print key 
        #    print request.environ[key];
        #    print '-------'
        #print "----------------------------------------------------------------";
        #for key in request.identity:
        #    print key 
        #    print request.identity[key];
        #    print '-------'
        #print "----------------------------------------------------------------";
        
        #print "User id "  ;
        #user =  request.identity['user'];
        #print user.user_id;
        
        """
        
        if 'voter' in groups:
            print "voter";
            log.info('voter');
            return HTTPFound(location='/survey')
        
        print "other";
        
        """
        
        
        
        # Do not use tg.redirect with tg.url as it will add the mountpoint
        # of the application twice.
        return HTTPFound(location=came_from)

    @expose()
    def post_logout(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        return HTTPFound(location=came_from)
    
    
    @expose('pollandsurvey.templates.expired')
    def expired(self,*args,**kw):
        return dict(page='expired');
    
    @expose('pollandsurvey.templates.thankyou')
    def thankyou(self,*args,**kw):
        return dict(page='thankyou');
     
    @expose('pollandsurvey.templates.new_form')
    def new(self, **kw):
        
         
        
        tmpl_context.form = create_movie_form
        return dict(modelname='Movie', value=kw)
    
    
    @validate(create_movie_form, error_handler=new)
    @expose()
    def create(self, **kw):
        """Create a movie object and save it to the database."""
        redirect("/register")
        
        
    @expose('pollandsurvey.templates.sanpleuploadfile')
    def sampleupload(self,*args,**kw):
    
        return dict(view="sample");
    
    @expose('json',content_type="text/plain"  )
    def addQuestion(self, came_from=lurl('/'), *args, **kw):
        reload(sys).setdefaultencoding('utf8')
        self.success = True;
        self.message = "success";
        log.info('---------1--------------');
         
     
        print kw;
        print args;
        
        return dict(success=self.success, message = self.message);
    
    @expose(content_type='application/json')
    def stream_list(self):
        def output_pause1():
            num = 0
            yield '['
            while num < 9:
                num += 1
                yield '%s, ' % num
                time.sleep(1)
            yield '10]'
        return output_pause1()
    
    @expose(content_type='text/css')
    def stream(self):
        def output_pause():
            num = 0
            while num < 10:
                num += 1
                yield '%s/%s\n' % (request.path_info, num)
                time.sleep(1)
        return output_pause()
    
    @expose('pollandsurvey.templates.register.register_success')
    def sample(self):
        from webob.exc import HTTPFound, HTTPUnauthorized
         
        app = request.environ['repoze.who.api'];# = HTTPUnauthorized()
         
        
        del request.environ['repoze.who.identity']
        #identify = request.environ['repoze.who.plugins']['main_identifier'].identify(request.environ);
        #print request.environ['repoze.who.plugins']['main_identifier'].forget(request.environ,identify);  
        #repoze_api.logout();
        #for key in request.environ:   print "%s --- %s"   %(  key, request.environ[key]);
        return dict(page='register_success')
    
    @expose('pollandsurvey.templates.register.register_success')
    def reactivate(self,*args,**kw):
        print kw;
        if(kw.get('activate_code')):
            self.userGenCode =  model.UserGenCode.getByActivateCode(kw.get('activate_code'));
            self.user = model.UserService.getByUserId(self.userGenCode.user_id);
            
            self.userGenCode = self.registerService.reActivateUserGenCode(self.userGenCode,self.user);
            
            self.emailValues={};
            self.emailValues['user_name'] = self.user.display_name;
            self.emailValues['email'] = self.user.email_address;
            # self.emailValues['password'] = self.password;
            self.emailValues['activate_url'] = request.application_url + "/activate/" + str(self.userGenCode.code);
           
            self.sendMailService.sendActivate(self.emailValues);
            self.sendMailService.start();
            
        
        return dict(page='register_success')
    
    @expose('genshi:pollandsurvey.templates.register.activate_success')
    def activate(self,*args, **kw):
        
        self.activate_code = args;
        if(len(self.activate_code) > 0): 
            self.userGenCode =  model.UserGenCode.getByActivateCode(self.activate_code[0]);
            self.message = "";
            
            if (self.userGenCode ):
                if ( not self.utility.convertToBool(self.userGenCode.success) ):
                    
                    if (self.utility.isActiveFromDate(self.utility.getCurrentDate() , self.userGenCode.create_date ,self.userGenCode.expire_date   ) ):
                        self.userGenCode.success = 1;
                        self.message = "Thank you. activate success.";
                        
                    else : 
                        self.message = "link activate expired ";
                          
                        override_template(RootController.activate, 'genshi:pollandsurvey.templates.register.reactivate') ;
                         
                else:
                    self.message = "activate already";
                    
            
            else:
                self.message = "Find not found activate code.";
                log.warning("Find not found activate code  %s", self.activate_code );
        else:
            #self.message = "Thank you!";
            log.warning("User income is wrong,have not activate code");
            redirect("/");
         
        
        #for key in request.environ:   print "%s --- %s"   %(  key, request.environ[key]);
         
        return dict(page='activate_success',message = self.message) 
    
    
    
    @expose('json'  )
    def fogotPassword(self,**kw):
        
        self.email = kw.get('email');
        
        self.user = model.User.by_email_address(self.email);
        if(self.user):
            newPassword = self.utility.id_generator(8);
            self.user._set_password(newPassword);
            
            self.emailValues={};
            self.emailValues['user_name'] = self.user.user_name;
            self.emailValues['email'] = self.user.email_address;
            self.emailValues['password'] = newPassword;
             
            
            self.sendMailService.sendForgotPassword(self.emailValues);
            self.sendMailService.start();
             
        else:
            log.info('forget password email : %s can not access',self.email);
        redirect("/")
        
    
    """
    @expose('pollandsurvey.templates.login')
    def login_old(self, came_from=lurl('/')):
        #Start the user login. 
        login_counter = request.environ.get('repoze.who.logins', 0)
        if login_counter > 0:
            flash(_('Wrong credentials'), 'warning')
        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from)
    
    @expose('pollandsurvey.templates.index')
    def index_old(self, came_from=lurl('/')):
        #Handle the front-page. 
        
        
        
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login', params=dict(came_from=came_from, __logins=login_counter))
        
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)
        
        groups = request.identity['groups'] 
        
        self.location = '/about';
        if 'voter' in groups:            
            log.info('voter');
            self.location = '/survey';
        log.info('other');
        
        return  HTTPFound(location=self.location)
        #return dict(page='index') 
    """ 
    