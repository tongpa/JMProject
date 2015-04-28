# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context,validate
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from tg.decorators import override_template;
from pollandsurvey import model
from pollandsurvey.controllers.secure import SecureController
from pollandsurvey.model import DBSession, metadata
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from pollandsurvey.lib.base import BaseController
from pollandsurvey.controllers.error import ErrorController
from pollandsurvey.widget.register.registerwidget import RegisterForm ,passwordValidator
from pollandsurvey.controllers.utility import Utility
from pollandsurvey.controllers.service import SendMailService,RegisterService,UserObject

from tg import tmpl_context 

import tw2.core
import logging;
from datetime import datetime ;
log = logging.getLogger(__name__);

__all__ = ['AccountController']


class AccountController(BaseController):
    """
    The root controller for the PollandSurvey application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    
    def __init__(self):
        self.utility = Utility();  
        self.sendMailService = SendMailService();
        self.registerService = RegisterService();
    

    def _before(self, *args, **kw):
        tmpl_context.project_name = "pollandsurvey"

    @expose('pollandsurvey.templates.account.index')
    @require(predicates.not_anonymous())
    def index(self, *args, **kw):
        """Handle the front-page."""
        return dict(page='index')
    
    @expose('pollandsurvey.templates.account.changepassword')
    @require(predicates.not_anonymous())
    def changepass(self, *args, **kw):
        """Handle the front-page."""
        return dict(page='changepassword')
    
    @expose('pollandsurvey.templates.account.socialmedia')
    @require(predicates.not_anonymous())
    def socialmedia(self, *args, **kw):
        """Handle the front-page."""
        return dict(page='socialmedia')
    
    @expose('pollandsurvey.templates.account.cancellation')
    @require(predicates.not_anonymous())
    def cancellation(self, *args, **kw):
        """Handle the front-page."""
        return dict(page='cancellation')
    
    @expose('json')
    @require(predicates.not_anonymous())
    def rechangepass(self, *args, **kw):
        
        self.success = True;
        self.message= '';
        if request.identity:
            log.warning("user cannot login, redirect to login");
            
            self.current_password = kw.get('password');
            self.new_password = kw.get('newpassword');
            self.re_new_password = kw.get('rnewpassword');
            user =  request.identity['user'];
            print str(self.new_password) == str(self.re_new_password);
            if( user.validate_password(self.current_password)):
                if(str(self.new_password) == str(self.re_new_password)):
                    user._set_password(self.new_password);
                    self.success = True;
                    self.message = "password changed";
                else:
                    self.message = "password not same";
            else:
                log.warning("user %s password not match : %s",user.user_name,self.current_password );
                self.message= 'password not match';
                
            
            
        else:
            self.message = 'user is not login.';
        print self.message;
        dict(success=self.success, message = self.message);
    
    
     