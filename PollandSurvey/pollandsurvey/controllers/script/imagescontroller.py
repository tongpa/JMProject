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
from pollandsurvey.controllers.utility import Utility;

import sys;
from datetime import datetime

from tg import tmpl_context
from tg.configuration import AppConfig, config
import os;
import sys;
import json;  

import logging;
log = logging.getLogger(__name__);
from  logsurvey import LogDBHandler;
__all__ = ['ImagesController']


class ImagesController(BaseController):
   
    def __init__(self):
        self.utility = Utility();
        self.target_file_name = self.utility.getDefaultImagePath();
        
        dh = LogDBHandler( config=config,request=request);        
        log.addHandler(dh)
        
        pass;
    
    @expose(content_type='image/png')
    def getImageScore(self,**kw):
        reload(sys).setdefaultencoding("utf-8");
        
        image_file = os.path.join('C:/temp/upload/track_feedback/images/27/issue_27.png' );
        imageId = kw.get('id');
        
        trackImage = model.Respondents.getId(imageId);
        
        return trackImage.image_file;
        
    
    @expose(content_type='image/png')
    def getImage(self,**kw):
        reload(sys).setdefaultencoding("utf-8");
        image_file = os.path.join('C:/temp/upload/track_feedback/images/27/issue_27.png' );
        imageId = kw.get('id');
        
        trackImage = model.QuestionMedia.getId(imageId);
        
     
        
       
        
        if trackImage:
            log.info( trackImage.media_path_file);
            image_file = os.path.join(trackImage.media_path_file );
            log.info( image_file);
            if not os.path.exists(image_file):
                log.info( "Found no %s" % image_file)
            else:
                
                return  file(image_file, "rb").read()
        
        
        
        return file(self.target_file_name, "rb").read()
    
    @expose(content_type='image/png')
    def getSubImage(self,**kw):
        reload(sys).setdefaultencoding("utf-8");
        image_file = os.path.join('C:/temp/upload/track_feedback/images/27/issue_27.png' );
        imageId = kw.get('id');
        
        trackImage = model.BasicMultimediaData.getByBasicDataId(imageId);
        log.info( "orig file path");
        log.info( os.path.abspath(__file__));
        if trackImage:
            log.info( trackImage.media_path_file);
            image_file = os.path.join(trackImage.media_path_file );
            log.info( image_file);
            if not os.path.exists(image_file):
                log.info( "Found no %s" % image_file)
            else:
                
                return  file(image_file, "rb").read()
           
        
        return file(self.target_file_name, "rb").read()
     
    
    
    
    