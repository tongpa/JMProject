# -*- coding: utf-8 -*-

import logging;
from xhtml2pdf import pisa
from tg.configuration import AppConfig, config
from tg import request

log = logging.getLogger(__name__); 
from logsurvey import LogDBHandler

class ConvertHtml2Pdf(object):
    


    def __init__(self):
        dh = LogDBHandler( config=config,request=request);        
        log.addHandler(dh)
        
    def convertHtmlToPdf(self,values,sourceHtml,outputFilename):
        
        for k,v in  values.iteritems():             
            sourceHtml = sourceHtml.replace('[%s]' % k,v)
        
        if(outputFilename):
            
             
            resultFile = open(outputFilename, "w+b")    
            
        
            pisaStatus = pisa.CreatePDF(
                sourceHtml,                # the HTML to convert
                dest=resultFile)           # file handle to recieve result
    
            # close output file
            resultFile.close()                 # close output file
        
            # return True on success and False on errors
            return pisaStatus.err
        
        return 1;
        
    
    
    def convert(self,values):
        sourceHtml='';
        
        #values = {};
        #values['name'] = 'Mr. Tong Tong';
        #values['score'] = '90';
        
        with open('D:/Tong/Code/code_python/file_python/sample1.html','r') as f:
        #with open('D:/setup/Python/lib/xhtml2pdf-master/xhtml2pdf-master/test/test-helloworld.html','r') as f:
            sourceHtml = f.read();
        
         
        for k,v in  values.iteritems():
             
            sourceHtml = sourceHtml.replace('[%s]' % k,v)
        
        outputFilename = "D:/Tong/Code/code_python/file_python/test.pdf"
        
        resultFile = open(outputFilename, "w+b")    
        print sourceHtml     
        
        pisaStatus = pisa.CreatePDF(
            sourceHtml,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

        # close output file
        resultFile.close()                 # close output file
    
        # return True on success and False on errors
        return pisaStatus.err

        pass;