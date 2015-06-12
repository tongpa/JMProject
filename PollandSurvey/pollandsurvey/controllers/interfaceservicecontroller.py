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
        
        print "args : ", args;
        print "kw : ", kw;
        
        print len(request.headers);
        
        for h in request.headers:
            print h ,  request.headers[h];
         
        try:
         
            print "body : " ,request.body;
            if( request.body):
                self.df = json.loads(request.body, encoding=request.charset);
                print self.df;
            
                self.df['keyAuthorize'] = "#987654321";
                samples = self.df;
            else:
                samples = {u'userName': u'tong', u'keyAuthorize': None, u'password': u'tong', u'dataTestSurfvey': None, u'passKey': u'#13456789'};
        
        except Exception as e:
            
            if kw:
                samples = kw;
                samples['keyAuthorize'] = "#987654321";
            
            #samples = {u'userName': u'tong', u'keyAuthorize': None, u'password': u'tong', u'dataTestSurfvey': None, u'passKey': u'#13456789'};
             
        return samples;#dict(surfveyAuthorize=samples);