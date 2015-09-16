# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context,validate
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from tg.decorators import override_template;
from pollandsurvey.model import UserService

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

from tgext.crud import EasyCrudRestController

import tw2.core
import logging;
from datetime import datetime ;
log = logging.getLogger(__name__);
from  survey import LogDBHandler;
__all__ = ['AccountSysController']


class AccountSysController(EasyCrudRestController):
    model = UserService
    title = "My admin title"
    