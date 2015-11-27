# -*- coding: utf-8 -*-
"""Survey Controller"""


from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context,validate,response 
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg.configuration import AppConfig, config
from tg import predicates
from pollandsurvey import model
from pollandsurvey.controllers.secure import SecureController
from pollandsurvey.model import DBSession, metadata
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from pollandsurvey.lib.base import BaseController
from pollandsurvey.controllers.error import ErrorController
from pollandsurvey.controllers.utility import Utility
from pollandsurvey.controllers.service import DoCheckin;

import sys
import json 
import types
from datetime import datetime
from tg import tmpl_context
from pollandsurvey.widget.movie_form import create_movie_form
from pollandsurvey.util import URLUtility
 
import logging;
log = logging.getLogger(__name__);
from logsurvey import LogDBHandler
__all__ = ['SendMailController']

 

class SendMailController(BaseController):
    
    def __init__(self):
        self.utility = Utility();
        self.urlUtility = URLUtility();
        dh = LogDBHandler( config=config,request=request);
        log.addHandler(dh)
        
         
        self.thread1 = DoCheckin(limit=100,offset=0 );
    
    @expose('json')    
    def send(self):
        
        reload(sys).setdefaultencoding("utf-8");
        
        print ("Start send Mail");
        
        print "isAlive : " + str(self.thread1.isAlive());
        if (not self.thread1.isAlive() ):
            print "start thread"
            self.thread1 = DoCheckin(limit=100,offset=0 );
            self.thread1.start()
        
        #time.sleep(15)
        #thread1.setLoop = False
        dict(message="thread send volunteer is started");
        
    @expose('json')
    def stop (self):
        self.thread1.setLoop = False
        print "exit"
        dict(message="thread send volunteer is stop");