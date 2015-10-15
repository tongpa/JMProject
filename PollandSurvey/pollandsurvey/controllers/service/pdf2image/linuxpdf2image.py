# -*- coding: utf-8 -*- 
import subprocess
import os
import traceback
import sys
try:
    import gfx
except:
    pass


class LinuxPDF2Image(object):
    
    
    def __init__(self):
        #filepath = "test.pdf"
        #self.gs_pdf_to_png(os.path.join(os.getcwd(), filepath), self.resolution)
        pass;
   
   
    def convert2Image(self,pdfFilePath,destinationPath):
        self.result = False;
        try:
            doc = gfx.open("pdf", pdfFilePath)
            img = gfx.ImageList()
            img.setparameter("antialise", "1") # turn on antialising
            page1 = doc.getPage(1)
            img.startpage(page1.width,page1.height)
            page1.render(img)
            img.endpage()
            img.save(destinationPath)
            self.result = True;
        
        except:
            pass;
        
        return self.result;
            
#pdf = WinPDF2Image();
#pdfFilePath = "d:\Tong\Code/code_python/file_python/test.pdf";
#destinationPath = "d:/Tong/Code/code_python/file_python/test12334";
#pdf.convert2Image(pdfFilePath, destinationPath);
 
        