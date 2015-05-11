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

import sys
import json 
import types
from datetime import datetime
from tg import tmpl_context
from pollandsurvey.widget.movie_form import create_movie_form

import logging;
log = logging.getLogger(__name__);

__all__ = ['VoterController']


class VoterController(BaseController):
    
    def __init__(self):
        self.utility = Utility();
        self.UPLOAD_DIR = config['path_upload_file'] ;
    
    def _before(self, *args, **kw):
        tmpl_context.project_name = "pollandsurvey"
    
    @expose('json')
    @require(predicates.in_any_group('voter','managers', msg=l_('Only for voter')))
    def createVoter(self,*args,**kw):
        
        print kw;
       
        
        
        self.success = True;
        self.result = False;
        self.message = 'Create Success'; 
        
        user =  request.identity['user'];
        
        self.voter = model.Voter.getVoterByOwnerAndEmail(user.user_id,kw.get('email'));
        if(self.voter ):
            self.success = True;
            
            self.message = "email same";
        else:
            
            self.voter = model.Voter();
            self.voter.email = kw.get('email');
            self.voter.prefix = kw.get('prefix');
            self.voter.firstname = kw.get('first_name');
            self.voter.lastname = kw.get('last_name');
            #self.voter.timezone = ;
    
            self.voter.user_id_owner  =  user.user_id;
            self.voter.id_gender =  kw.get('gender'); 
            self.voter.id_voter_type = 1;
            self.voter.id_marriage_status = 1;
            
            
            print self.voter.id_marriage_status ;
            self.voter.save();
     
            
            self.success = True;
            self.result = True;
            self.message = "create voter sucess";
            
            
        
        
        
        
        
        return dict(success=self.success, result = self.result , message = self.message);
        
    