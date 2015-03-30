import os
import os.path
import sys
from validate_email import validate_email
class Utility(object):

    def checkPathFile(self,path):
        #print os.path.exists(path) ;
         
        
        
        if not os.path.exists(path):
            os.makedirs(path)
             
        #print os.path.exists(path) ;
        
    def checkFileExist(self,pathFile):
        return os.path.isfile(pathFile) ;
    
    def readDataFile(self,pathFile ):
        
        file = open(pathFile,'rb');
        return file.read();
   
    
    def getDic(self):
        value =  dict(test= 'test1',
                    data = 'data1');
                    
        print value.get('test');
        print value['test'];
         
     
    def write(self, string):
        if isinstance(string, unicode):
            string = string.encode(sys.__stdout__.encoding)
        sys.__stdout__.write(string)
    
    def lastReplace(self,string , value):
        if(string):
            string = string.strip() ;
            self.last = (string).rfind(value);
            self.leng = len(string) 
            if (self.leng - self.last) == 1 :
                string =  string[0:self.last];
        
        return string;
            
    def checkEmail(self,emails):
        self.isEmail = False;
        if emails:
            try:
                mail = emails.split(",")  ;
                
                for m in mail:
                    
                    #if (self.validEmail(str(m).strip())):
                    if(validate_email( self.lastReplace(str(m).strip(), '.')     )):
                    #if(validate_email(str(m).strip())):
                        self.isEmail = True;
                        break;
                    
                    #self.isEmail  = self.isEmail  and self.validEmail(str(m).strip());
                    #print  m , self.validEmail(str(m).strip());
                    
            except Exception as e:
                print 'error : ' + str(emails)   ;
            finally:
                pass;     
        
        return self.isEmail;
        
         
    def validEmail(self,email):
        import re

        if re.match(r"^[a-zA-Z0-9._]+\@[a-zA-Z0-9._]+\.[a-zA-Z]{3,}$", email)!=None:
        
            return True;
        
        return False; 
        

u = Utility();

is_valid = validate_email('...')
print is_valid;
print u.checkEmail('Bkrentgroup@hotmail.com,service@bkrent.com, webmaster@bkrent.com');
print u.checkEmail('555');
print u.checkEmail('maanon@supersports.co.th');
print u.checkEmail('wenxing17@yahoo.com.sg. ');

email = ('wenxing17@yahoo.com.sg. ') ;
print u.lastReplace(email,'.');
email = 'Bkrentgroup@hotmail.com,service@bkrent.com, webmaster@bkrent.com';

print str(None);
print u.lastReplace(email,'.');

import datetime

today = datetime.datetime.now()
print today

#print u.checkPathFile('c:/temp/test1');
#print u.checkFileExist('C:/Temp/upload/14/Data2.xlsx');  
#u.checkFileExist('c:/temp/upload/Data2.xlsx');  
#u.getDic();
 
#print os.path.dirname('c:/temp/upload/Data2.xlsx');

"""class A(object):
    nameA='A call';
    def __init__(self):
        print "Constructor A was called"
        
    def printValue(self):
        print self.nameA;
        

class B(A):
    def __init__(self):
        super(B,self).__init__()
        print "Constructor B was called"

class C(B):
    def __init__(self):
        super(C,self).__init__()
        print "Constructor C was called"

b =B();
b.nameA = '5555';
c = C()

b.printValue();
c.printValue();"""




class A(object):
    nameA='A call';
    def __init__(self):
        print "Constructor A was called"
    def printValue(self):
        print self.nameA;

class B(A):

    def __init__(self):
        A.__init__(self)
        # A.__init__(self,<parameters>) if you want to call with parameters
        print "Constructor B was called"

class C(B):

    def __init__(self):
        # A.__init__(self) # if you want to call most super class...
        B.__init__(self)
        print "Constructor C was called"
  
     