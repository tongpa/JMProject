from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context,validate ,RestController 
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates,controllers;
from tg.decorators import override_template,with_trailing_slash; 
from pollandsurvey import model
from pollandsurvey.controllers.secure import SecureController
from pollandsurvey.model import DBSession, metadata
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController


  
from pollandsurvey.controllers.error import ErrorController


import time
import sys
import json 
 

import logging;
log = logging.getLogger(__name__);
__all__ = ['InterfaceServiceController']


class InterfaceServiceController(RestController):
    
    @with_trailing_slash
    @expose('json')
    #@require(predicates.in_any_group('voter','managers', msg=l_('Only for voter')))
    def get_all(self,*args,**kw):
        
     
        
        print len(request.headers);
        
        for h in request.headers:
            print h ,  request.headers[h];
         
        
         
        
        
        #self.df = json.loads(request.body, encoding=request.charset);
        #print self.df;
        
        samples = [];
        samples.append({'id':1,'name': 'test1'});
        samples.append({'id':2,'name': 'test2'});
        return dict(sample=samples);