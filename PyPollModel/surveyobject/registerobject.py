# -*- coding: utf-8 -*-
from surveymodel.auth import User
from surveymodel.authuser import UserService 
class RegisterObject(object):
    
    def __init__(self, fullname = None, fulllastname = None , email= None,city=None, country=None, address=None, password=None, rpassword=None, tnc=None, gender=None, id_gender=None):
        self.fullname = fullname;
        self.fulllastname = fulllastname;
        self.email = email;
        self.city = city;
        self.country = country;
        self.address = address;
        self.password = password;
        self.rpassword = rpassword;
        self.tnc = tnc;
        self.id_gender = id_gender;

    def getUser(self):
        
        return User(user_id=None, user_name=self.email,email_address=self.email, display_name=(self.fullname + ' ' + self.fulllastname) ,active=1, password = self.password)    
    
    def getUserService(self):
        
        return UserService(
                           first_name=self.fullname, last_name=self.fulllastname, address=self.address, city=self.city, country=self.country, accept_tnc=self.tnc, id_gender=self.id_gender
                           )