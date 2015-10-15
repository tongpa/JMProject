import subprocess
import os
import traceback
import sys
from pollandsurvey.controllers.utility import Utility
from pdf2image import WinPDF2Image,LinuxPDF2Image;

 
class ConvertPdf2image(object):
 

    def __init__(self):      
        self.util = Utility();
        self.convertPDF2Image =None;
        if self.util.isWindows():
            self.convertPDF2Image = WinPDF2Image();
        else:
            self.convertPDF2Image = LinuxPDF2Image();
            
        
    def convert(self,pdfFilePath,destinationPath):
        return self.convertPDF2Image.convert2Image(pdfFilePath, destinationPath)
        
    
    