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
from tg.configuration import AppConfig, config
from tg import tmpl_context 

import tw2.core
import logging;
from datetime import datetime ;
log = logging.getLogger(__name__);
from  survey import LogDBHandler;
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
        dh = LogDBHandler( config=config,request=request);        
        log.addHandler(dh)
        

    def _before(self, *args, **kw):
        tmpl_context.project_name = "pollandsurvey"

    @expose('pollandsurvey.templates.account.generalsetting')
    @require(predicates.not_anonymous())
    def index(self, *args, **kw):
        """Handle the front-page."""
        
        if request.identity:
            user =  request.identity['user'];
            userService = model.UserService.getByUserId(user.user_id);
        
        listConutry = [];
        
        listConutry.append({'code':'AF', 'description':'Afghanistan', 'result':''});
        listConutry.append({'code':'AL', 'description':'Albania', 'result':''});
        listConutry.append({'code':'DZ', 'description':'Algeria', 'result':''});
        listConutry.append({'code':'AS', 'description':'American Samoa', 'result':''});
        listConutry.append({'code':'AD', 'description':'Andorra', 'result':''});
        listConutry.append({'code':'AO', 'description':'Angola', 'result':''});
        listConutry.append({'code':'AI', 'description':'Anguilla', 'result':''});
        listConutry.append({'code':'AQ', 'description':'Antarctica', 'result':''});
        listConutry.append({'code':'AR', 'description':'Argentina', 'result':''});
        listConutry.append({'code':'AM', 'description':'Armenia', 'result':''});
        listConutry.append({'code':'AW', 'description':'Aruba', 'result':''});
        listConutry.append({'code':'AU', 'description':'Australia', 'result':''});
        listConutry.append({'code':'AT', 'description':'Austria', 'result':''});
        listConutry.append({'code':'AZ', 'description':'Azerbaijan', 'result':''});
        listConutry.append({'code':'BS', 'description':'Bahamas', 'result':''});
        listConutry.append({'code':'BH', 'description':'Bahrain', 'result':''});
        listConutry.append({'code':'BD', 'description':'Bangladesh', 'result':''});
        listConutry.append({'code':'BB', 'description':'Barbados', 'result':''});
        listConutry.append({'code':'BY', 'description':'Belarus', 'result':''});
        listConutry.append({'code':'BE', 'description':'Belgium', 'result':''});
        listConutry.append({'code':'BZ', 'description':'Belize', 'result':''});
        listConutry.append({'code':'BJ', 'description':'Benin', 'result':''});
        listConutry.append({'code':'BM', 'description':'Bermuda', 'result':''});
        listConutry.append({'code':'BT', 'description':'Bhutan', 'result':''});
        listConutry.append({'code':'BO', 'description':'Bolivia', 'result':''});
        listConutry.append({'code':'BA', 'description':'Bosnia and Herzegowina', 'result':''});
        listConutry.append({'code':'BW', 'description':'Botswana', 'result':''});
        listConutry.append({'code':'BV', 'description':'Bouvet Island', 'result':''});
        listConutry.append({'code':'BR', 'description':'Brazil', 'result':''});
        listConutry.append({'code':'IO', 'description':'British Indian Ocean Territory', 'result':''});
        listConutry.append({'code':'BN', 'description':'Brunei Darussalam', 'result':''});
        listConutry.append({'code':'BG', 'description':'Bulgaria', 'result':''});
        listConutry.append({'code':'BF', 'description':'Burkina Faso', 'result':''});
        listConutry.append({'code':'BI', 'description':'Burundi', 'result':''});
        listConutry.append({'code':'KH', 'description':'Cambodia', 'result':''});
        listConutry.append({'code':'CM', 'description':'Cameroon', 'result':''});
        listConutry.append({'code':'CA', 'description':'Canada', 'result':''});
        listConutry.append({'code':'CV', 'description':'Cape Verde', 'result':''});
        listConutry.append({'code':'KY', 'description':'Cayman Islands', 'result':''});
        listConutry.append({'code':'CF', 'description':'Central African Republic', 'result':''});
        listConutry.append({'code':'TD', 'description':'Chad', 'result':''});
        listConutry.append({'code':'CL', 'description':'Chile', 'result':''});
        listConutry.append({'code':'CN', 'description':'China', 'result':''});
        listConutry.append({'code':'CX', 'description':'Christmas Island', 'result':''});
        listConutry.append({'code':'CC', 'description':'Cocos (Keeling) Islands', 'result':''});
        listConutry.append({'code':'CO', 'description':'Colombia', 'result':''});
        listConutry.append({'code':'KM', 'description':'Comoros', 'result':''});
        listConutry.append({'code':'CG', 'description':'Congo', 'result':''});
        listConutry.append({'code':'CD', 'description':'Congo, the Democratic Republic of the', 'result':''});
        listConutry.append({'code':'CK', 'description':'Cook Islands', 'result':''});
        listConutry.append({'code':'CR', 'description':'Costa Rica', 'result':''});
        listConutry.append({'code':'CI', 'description':'Cote d\'Ivoire', 'result':''});
        listConutry.append({'code':'HR', 'description':'Croatia (Hrvatska)', 'result':''});
        listConutry.append({'code':'CU', 'description':'Cuba', 'result':''});
        listConutry.append({'code':'CY', 'description':'Cyprus', 'result':''});
        listConutry.append({'code':'CZ', 'description':'Czech Republic', 'result':''});
        listConutry.append({'code':'DK', 'description':'Denmark', 'result':''});
        listConutry.append({'code':'DJ', 'description':'Djibouti', 'result':''});
        listConutry.append({'code':'DM', 'description':'Dominica', 'result':''});
        listConutry.append({'code':'DO', 'description':'Dominican Republic', 'result':''});
        listConutry.append({'code':'EC', 'description':'Ecuador', 'result':''});
        listConutry.append({'code':'EG', 'description':'Egypt', 'result':''});
        listConutry.append({'code':'SV', 'description':'El Salvador', 'result':''});
        listConutry.append({'code':'GQ', 'description':'Equatorial Guinea', 'result':''});
        listConutry.append({'code':'ER', 'description':'Eritrea', 'result':''});
        listConutry.append({'code':'EE', 'description':'Estonia', 'result':''});
        listConutry.append({'code':'ET', 'description':'Ethiopia', 'result':''});
        listConutry.append({'code':'FK', 'description':'Falkland Islands (Malvinas)', 'result':''});
        listConutry.append({'code':'FO', 'description':'Faroe Islands', 'result':''});
        listConutry.append({'code':'FJ', 'description':'Fiji', 'result':''});
        listConutry.append({'code':'FI', 'description':'Finland', 'result':''});
        listConutry.append({'code':'FR', 'description':'France', 'result':''});
        listConutry.append({'code':'GF', 'description':'French Guiana', 'result':''});
        listConutry.append({'code':'PF', 'description':'French Polynesia', 'result':''});
        listConutry.append({'code':'TF', 'description':'French Southern Territories', 'result':''});
        listConutry.append({'code':'GA', 'description':'Gabon', 'result':''});
        listConutry.append({'code':'GM', 'description':'Gambia', 'result':''});
        listConutry.append({'code':'GE', 'description':'Georgia', 'result':''});
        listConutry.append({'code':'DE', 'description':'Germany', 'result':''});
        listConutry.append({'code':'GH', 'description':'Ghana', 'result':''});
        listConutry.append({'code':'GI', 'description':'Gibraltar', 'result':''});
        listConutry.append({'code':'GR', 'description':'Greece', 'result':''});
        listConutry.append({'code':'GL', 'description':'Greenland', 'result':''});
        listConutry.append({'code':'GD', 'description':'Grenada', 'result':''});
        listConutry.append({'code':'GP', 'description':'Guadeloupe', 'result':''});
        listConutry.append({'code':'GU', 'description':'Guam', 'result':''});
        listConutry.append({'code':'GT', 'description':'Guatemala', 'result':''});
        listConutry.append({'code':'GN', 'description':'Guinea', 'result':''});
        listConutry.append({'code':'GW', 'description':'Guinea-Bissau', 'result':''});
        listConutry.append({'code':'GY', 'description':'Guyana', 'result':''});
        listConutry.append({'code':'HT', 'description':'Haiti', 'result':''});
        listConutry.append({'code':'HM', 'description':'Heard and Mc Donald Islands', 'result':''});
        listConutry.append({'code':'VA', 'description':'Holy See (Vatican City State)', 'result':''});
        listConutry.append({'code':'HN', 'description':'Honduras', 'result':''});
        listConutry.append({'code':'HK', 'description':'Hong Kong', 'result':''});
        listConutry.append({'code':'HU', 'description':'Hungary', 'result':''});
        listConutry.append({'code':'IS', 'description':'Iceland', 'result':''});
        listConutry.append({'code':'IN', 'description':'India', 'result':''});
        listConutry.append({'code':'ID', 'description':'Indonesia', 'result':''});
        listConutry.append({'code':'IR', 'description':'Iran (Islamic Republic of)', 'result':''});
        listConutry.append({'code':'IQ', 'description':'Iraq', 'result':''});
        listConutry.append({'code':'IE', 'description':'Ireland', 'result':''});
        listConutry.append({'code':'IL', 'description':'Israel', 'result':''});
        listConutry.append({'code':'IT', 'description':'Italy', 'result':''});
        listConutry.append({'code':'JM', 'description':'Jamaica', 'result':''});
        listConutry.append({'code':'JP', 'description':'Japan', 'result':''});
        listConutry.append({'code':'JO', 'description':'Jordan', 'result':''});
        listConutry.append({'code':'KZ', 'description':'Kazakhstan', 'result':''});
        listConutry.append({'code':'KE', 'description':'Kenya', 'result':''});
        listConutry.append({'code':'KI', 'description':'Kiribati', 'result':''});
        listConutry.append({'code':'KP', 'description':'Korea, Democratic People\'s Republic of', 'result':''});
        listConutry.append({'code':'KR', 'description':'Korea, Republic of', 'result':''});
        listConutry.append({'code':'KW', 'description':'Kuwait', 'result':''});
        listConutry.append({'code':'KG', 'description':'Kyrgyzstan', 'result':''});
        listConutry.append({'code':'LA', 'description':'Lao People\'s Democratic Republic', 'result':''});
        listConutry.append({'code':'LV', 'description':'Latvia', 'result':''});
        listConutry.append({'code':'LB', 'description':'Lebanon', 'result':''});
        listConutry.append({'code':'LS', 'description':'Lesotho', 'result':''});
        listConutry.append({'code':'LR', 'description':'Liberia', 'result':''});
        listConutry.append({'code':'LY', 'description':'Libyan Arab Jamahiriya', 'result':''});
        listConutry.append({'code':'LI', 'description':'Liechtenstein', 'result':''});
        listConutry.append({'code':'LT', 'description':'Lithuania', 'result':''});
        listConutry.append({'code':'LU', 'description':'Luxembourg', 'result':''});
        listConutry.append({'code':'MO', 'description':'Macau', 'result':''});
        listConutry.append({'code':'MK', 'description':'Macedonia, The Former Yugoslav Republic of', 'result':''});
        listConutry.append({'code':'MG', 'description':'Madagascar', 'result':''});
        listConutry.append({'code':'MW', 'description':'Malawi', 'result':''});
        listConutry.append({'code':'MY', 'description':'Malaysia', 'result':''});
        listConutry.append({'code':'MV', 'description':'Maldives', 'result':''});
        listConutry.append({'code':'ML', 'description':'Mali', 'result':''});
        listConutry.append({'code':'MT', 'description':'Malta', 'result':''});
        listConutry.append({'code':'MH', 'description':'Marshall Islands', 'result':''});
        listConutry.append({'code':'MQ', 'description':'Martinique', 'result':''});
        listConutry.append({'code':'MR', 'description':'Mauritania', 'result':''});
        listConutry.append({'code':'MU', 'description':'Mauritius', 'result':''});
        listConutry.append({'code':'YT', 'description':'Mayotte', 'result':''});
        listConutry.append({'code':'MX', 'description':'Mexico', 'result':''});
        listConutry.append({'code':'FM', 'description':'Micronesia, Federated States of', 'result':''});
        listConutry.append({'code':'MD', 'description':'Moldova, Republic of', 'result':''});
        listConutry.append({'code':'MC', 'description':'Monaco', 'result':''});
        listConutry.append({'code':'MN', 'description':'Mongolia', 'result':''});
        listConutry.append({'code':'MS', 'description':'Montserrat', 'result':''});
        listConutry.append({'code':'MA', 'description':'Morocco', 'result':''});
        listConutry.append({'code':'MZ', 'description':'Mozambique', 'result':''});
        listConutry.append({'code':'MM', 'description':'Myanmar', 'result':''});
        listConutry.append({'code':'NA', 'description':'Namibia', 'result':''});
        listConutry.append({'code':'NR', 'description':'Nauru', 'result':''});
        listConutry.append({'code':'NP', 'description':'Nepal', 'result':''});
        listConutry.append({'code':'NL', 'description':'Netherlands', 'result':''});
        listConutry.append({'code':'AN', 'description':'Netherlands Antilles', 'result':''});
        listConutry.append({'code':'NC', 'description':'New Caledonia', 'result':''});
        listConutry.append({'code':'NZ', 'description':'New Zealand', 'result':''});
        listConutry.append({'code':'NI', 'description':'Nicaragua', 'result':''});
        listConutry.append({'code':'NE', 'description':'Niger', 'result':''});
        listConutry.append({'code':'NG', 'description':'Nigeria', 'result':''});
        listConutry.append({'code':'NU', 'description':'Niue', 'result':''});
        listConutry.append({'code':'NF', 'description':'Norfolk Island', 'result':''});
        listConutry.append({'code':'MP', 'description':'Northern Mariana Islands', 'result':''});
        listConutry.append({'code':'NO', 'description':'Norway', 'result':''});
        listConutry.append({'code':'OM', 'description':'Oman', 'result':''});
        listConutry.append({'code':'PK', 'description':'Pakistan', 'result':''});
        listConutry.append({'code':'PW', 'description':'Palau', 'result':''});
        listConutry.append({'code':'PA', 'description':'Panama', 'result':''});
        listConutry.append({'code':'PG', 'description':'Papua New Guinea', 'result':''});
        listConutry.append({'code':'PY', 'description':'Paraguay', 'result':''});
        listConutry.append({'code':'PE', 'description':'Peru', 'result':''});
        listConutry.append({'code':'PH', 'description':'Philippines', 'result':''});
        listConutry.append({'code':'PN', 'description':'Pitcairn', 'result':''});
        listConutry.append({'code':'PL', 'description':'Poland', 'result':''});
        listConutry.append({'code':'PT', 'description':'Portugal', 'result':''});
        listConutry.append({'code':'PR', 'description':'Puerto Rico', 'result':''});
        listConutry.append({'code':'QA', 'description':'Qatar', 'result':''});
        listConutry.append({'code':'RE', 'description':'Reunion', 'result':''});
        listConutry.append({'code':'RO', 'description':'Romania', 'result':''});
        listConutry.append({'code':'RU', 'description':'Russian Federation', 'result':''});
        listConutry.append({'code':'RW', 'description':'Rwanda', 'result':''});
        listConutry.append({'code':'KN', 'description':'Saint Kitts and Nevis', 'result':''});
        listConutry.append({'code':'LC', 'description':'Saint LUCIA', 'result':''});
        listConutry.append({'code':'VC', 'description':'Saint Vincent and the Grenadines', 'result':''});
        listConutry.append({'code':'WS', 'description':'Samoa', 'result':''});
        listConutry.append({'code':'SM', 'description':'San Marino', 'result':''});
        listConutry.append({'code':'ST', 'description':'Sao Tome and Principe', 'result':''});
        listConutry.append({'code':'SA', 'description':'Saudi Arabia', 'result':''});
        listConutry.append({'code':'SN', 'description':'Senegal', 'result':''});
        listConutry.append({'code':'SC', 'description':'Seychelles', 'result':''});
        listConutry.append({'code':'SL', 'description':'Sierra Leone', 'result':''});
        listConutry.append({'code':'SG', 'description':'Singapore', 'result':''});
        listConutry.append({'code':'SK', 'description':'Slovakia (Slovak Republic)', 'result':''});
        listConutry.append({'code':'SI', 'description':'Slovenia', 'result':''});
        listConutry.append({'code':'SB', 'description':'Solomon Islands', 'result':''});
        listConutry.append({'code':'SO', 'description':'Somalia', 'result':''});
        listConutry.append({'code':'ZA', 'description':'South Africa', 'result':''});
        listConutry.append({'code':'GS', 'description':'South Georgia and the South Sandwich Islands', 'result':''});
        listConutry.append({'code':'ES', 'description':'Spain', 'result':''});
        listConutry.append({'code':'LK', 'description':'Sri Lanka', 'result':''});
        listConutry.append({'code':'SH', 'description':'St. Helena', 'result':''});
        listConutry.append({'code':'PM', 'description':'St. Pierre and Miquelon', 'result':''});
        listConutry.append({'code':'SD', 'description':'Sudan', 'result':''});
        listConutry.append({'code':'SR', 'description':'Suriname', 'result':''});
        listConutry.append({'code':'SJ', 'description':'Svalbard and Jan Mayen Islands', 'result':''});
        listConutry.append({'code':'SZ', 'description':'Swaziland', 'result':''});
        listConutry.append({'code':'SE', 'description':'Sweden', 'result':''});
        listConutry.append({'code':'CH', 'description':'Switzerland', 'result':''});
        listConutry.append({'code':'SY', 'description':'Syrian Arab Republic', 'result':''});
        listConutry.append({'code':'TW', 'description':'Taiwan, Province of China', 'result':''});
        listConutry.append({'code':'TJ', 'description':'Tajikistan', 'result':''});
        listConutry.append({'code':'TZ', 'description':'Tanzania, United Republic of', 'result':''});
        listConutry.append({'code':'TH',  'description':'Thailand', 'result':''});
        listConutry.append({'code':'TG', 'description':'Togo', 'result':''});
        listConutry.append({'code':'TK', 'description':'Tokelau', 'result':''});
        listConutry.append({'code':'TO', 'description':'Tonga', 'result':''});
        listConutry.append({'code':'TT', 'description':'Trinidad and Tobago', 'result':''});
        listConutry.append({'code':'TN', 'description':'Tunisia', 'result':''});
        listConutry.append({'code':'TR', 'description':'Turkey', 'result':''});
        listConutry.append({'code':'TM', 'description':'Turkmenistan', 'result':''});
        listConutry.append({'code':'TC', 'description':'Turks and Caicos Islands', 'result':''});
        listConutry.append({'code':'TV', 'description':'Tuvalu', 'result':''});
        listConutry.append({'code':'UG', 'description':'Uganda', 'result':''});
        listConutry.append({'code':'UA', 'description':'Ukraine', 'result':''});
        listConutry.append({'code':'AE', 'description':'United Arab Emirates', 'result':''});
        listConutry.append({'code':'GB', 'description':'United Kingdom', 'result':''});
        listConutry.append({'code':'US', 'description':'United States', 'result':''});
        listConutry.append({'code':'UM', 'description':'United States Minor Outlying Islands', 'result':''});
        listConutry.append({'code':'UY', 'description':'Uruguay', 'result':''});
        listConutry.append({'code':'UZ', 'description':'Uzbekistan', 'result':''});
        listConutry.append({'code':'VU', 'description':'Vanuatu', 'result':''});
        listConutry.append({'code':'VE', 'description':'Venezuela', 'result':''});
        listConutry.append({'code':'VN', 'description':'Viet Nam', 'result':''});
        listConutry.append({'code':'VG', 'description':'Virgin Islands (British)', 'result':''});
        listConutry.append({'code':'VI', 'description':'Virgin Islands (U.S.)', 'result':''});
        listConutry.append({'code':'WF', 'description':'Wallis and Futuna Islands', 'result':''});
        listConutry.append({'code':'EH', 'description':'Western Sahara', 'result':''});
        listConutry.append({'code':'YE', 'description':'Yemen', 'result':''});
        listConutry.append({'code':'ZM', 'description':'Zambia', 'result':''});
        listConutry.append({'code':'ZW', 'description':'Zimbabwe', 'result':''});
        
        
        listGender = [];
        listGender.append({'code': '1', 'description' : 'Male'});
        listGender.append({'code': '2', 'description' : 'Female'});
        
        #for country in listConutry:
        #    print "%s , %s , %s ", (userService.country , country['code'], (userService.country == country['code']))
        #    if userService.country == country['code'] :
        #        country['selected'] = 'selected';
        
        return dict(page='index', userService = userService, listConutry=listConutry, listGender=listGender)
    
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
    #@expose('json',content_type="text/plain"  )
    
    @require(predicates.not_anonymous())
    def rechangepass(self, *args, **kw):
        
        self.success = False;
        self.message= '';
        if request.identity:
            log.warning("user cannot login, redirect to login");
            
            self.current_password = kw.get('password');
            self.new_password = kw.get('newpassword');
            self.re_new_password = kw.get('rnewpassword');
            user =  request.identity['user'];
            
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
         
        
        return dict(success=self.success, message = self.message);
    
    
     