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

__all__ = ['ListSurveyController']


class ListSurveyController(BaseController):
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

    @expose('pollandsurvey.templates.listsurvey.index')
    def index(self, came_from=lurl('/')):
        groups = request.identity['groups'] ;
        if ('creator' in groups):
            log.info("redirect to create survey page");
            groups = None;
            redirect('/survey');
                
        return dict(page='metronic') 
    
    #def index(self, came_from=lurl('/'), *args, **kw):
        """Handle the front-page."""
    #    return dict(page='index')

     
    