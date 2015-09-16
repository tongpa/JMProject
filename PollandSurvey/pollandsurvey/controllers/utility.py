import os
import os.path
import base64 
import json 
import logging;
import types;
import datetime;
import os.path
import string
import random
import uuid
import hashlib
log = logging.getLogger(__name__); 
class Utility(object):

    def __init__(self):
        pass;
    
    def my_random_string(self,string_length=10):
        """Returns a random string of length string_length."""
        random = str(uuid.uuid4()) # Convert UUID format to a Python string.
        random = random.upper() # Make all characters uppercase.
        random = random.replace("-","") # Remove the UUID '-'.
        return random[0:string_length] # Return the random string.

    def id_generator(self, size=8, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size));
    
    def getDefaultImagePath(self):
        path = os.getcwd();
        self.target_file_name = os.path.join(os.getcwd(), path , 'pollandsurvey', 'public','img','survey','not_available.png');
        return self.target_file_name;
        
    def joinPathFileAndCreatePath(self,orig_path,subpath,filename):
        self.target_file_name = os.path.join(os.getcwd(), orig_path , subpath, filename);
        print self.target_file_name;
        self.createPathFile(self.target_file_name);        
        return self.target_file_name;
    
    def getCurrentDate(self):
        return datetime.datetime.strptime(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")  , "%Y-%m-%d %H:%M:%S");
        
    def getStartDate(self):
        return datetime.datetime.strptime(datetime.datetime.today().strftime("%Y-%m-%d")  , "%Y-%m-%d");
        #stop = self.plusDate(start, numberDay);
       # return start,stop;
    
    def plusDate(self,currentDate,numberDay=0):
        if(currentDate is None or ( type(currentDate) is not datetime.datetime )     ):
            currentDate = datetime.datetime.today();
             
        self.temp =currentDate + datetime.timedelta(days=numberDay);
        return datetime.datetime.strptime(self.temp.strftime("%Y-%m-%d") + " 23:59:59", "%Y-%m-%d %H:%M:%S");
    
    def plusTime(self,currentDate,numberMinute=0):
        if(currentDate is None or ( type(currentDate) is not datetime.datetime )     ):
            currentDate = datetime.datetime.today();
        
        self.temp =currentDate + datetime.timedelta(minutes=numberMinute);
        
        return datetime.datetime.strptime(self.temp.strftime("%Y-%m-%d %H:%M:%S")  , "%Y-%m-%d %H:%M:%S"); 
    
    def createPathFile(self,path):         
        if os.path.exists(path):
            return True;
        else:
            path = os.path.dirname(path);
            if(not self.createPathFile(path)):
                os.makedirs(path);
            return False;
    
    def convertToBit(self,data):
        if ( data is not None and ( data == u'1' or str(data).lower() == u'on') ):
            return 1;
        else:
            return 0;
    def convertToBool(self,data):
        if ( data is not None and ( str(data) == u'1' or str(data).lower() == u'on') ):
            return True;
        else:
            return False;
    
    def isNumber(self,data):
        try:
            float(data)
            return True
        except ValueError:
            pass
     
        try:
            import unicodedata
            unicodedata.numeric(data)
            return True
        except (TypeError, ValueError):
            pass
     
        return False    
    
    def saveFile(self,filePath,data):
        fp = open(filePath, 'wb' );
        fp.write(data);
        fp.close();
    
    def removeFile(self,filePath):
        os.remove( filePath );
        
    def isEmpty(self,data):
        if data is not None:
            
            if data == '':
                return True;
            elif len(str(data).strip()) == 0:
                return True;
            else:
                return False;
        else:
            return True;
        
        
    def convertToDateTime(self,data,format):
        pass;
    
    def spritValue(self,data,value):
         
 
        if not self.isEmpty(data) and  ( type(data) == types.StringType  or type(data) == types.UnicodeType  )   :
            
            return data.lstrip(value).split(value);
        return data;
    
    def isPartOf(self,first,second):
        if first is not None and second is not None:
            first = str(first).lower();
            second = str(second).lower();
            self.index = second.rfind(first);
            #print first + " is path of " + second + "  : " + str(self.index);
            if(self.index >=0):
                return True;
            else:
                return False;
        
        return False;
    
    def isActiveFromDate(self,data,start,stop):
        
        if self.isEmpty(start):
            return False;
        
        if self.isEmpty(data):
            data = datetime.datetime.today();
            
        #print 'start : ' , start;    
        #print 'data : ' , data;
        #print 'stop : ' , stop;
        
        
        if self.isEmpty(stop):
            #print 'start < date ', start <= data; 
            return start <= data;
        elif start < data <= stop:
            #print 'start < data <= stop :', start < data <= stop;
            return start < data <= stop;
        
        return False;
            
    def splitNameWithOutExtention(self,value):
        if (not self.isEmpty(value)):
            fileName, fileExtension = os.path.splitext(value);
            fileExtension = None;
            return fileName;
        
        return value;
            
    def decryptMD5(self,testHash):
        
        hash_object = hashlib.md5(b'Hello World')
        print(hash_object.hexdigest())
        
        hash_object = hashlib.md5(hash_object.hexdigest().encode())
        print(hash_object.hexdigest())
                        
         
            
            
#import ast
#print ast.literal_eval('True')
#print bool('true')
#print bool('false')

#answer = 'false'

#print ({True: True, False: False}[ answer in 'true'])

#u = Utility();
#print u.getCurrentDate();
#print u.decryptMD5('40c906c22eaf938f902b2fa85efff1d5');
#print u.plusDate(datetime.datetime.today(),0);

#print u.plusTime(datetime.datetime.today() , 10);

#print u.plusDate(datetime.datetime.today(),30);
#print u.my_random_string(15);

#u.isPartOf('answer_1.png',"""C:\\fakepath\\answer_1.png""");
#d2 = datetime.datetime.today() - datetime.timedelta(days=2);
#d3 = datetime.datetime.today() + datetime.timedelta(days=15);
#u.isActiveFromDate(None,d2,d3);

#sp =  u.spritValue('/preview/welcome','/');
#print sp[0];
#print u.isNumber('20');
#import types
#print type(u'') is types.UnicodeType;
#sp = u.spritValue("10.2.1", ".");
#print sp;
#u.splitNameWithOutExtention('10.2.1.html');
#from datetime import datetime
#dt_str = '01/02/2015'  + ' 00:00:00' ;
#dt_obj = datetime.strptime(dt_str, '%d/%m/%Y %H:%M:%S')
#print dt_obj;
 

#from decimal import Decimal
#import math
#d = 173623;
#r = 500;
#print math.floor  (d/Decimal(r));
#print   (d/Decimal(r));
 
#print bool(1);
#print bool(0);
 
 
#datetime.strptime(  kw.get('activate_date')  + ' 00:00:00' , '%d/%m/%Y %H:%M:%S') ;
