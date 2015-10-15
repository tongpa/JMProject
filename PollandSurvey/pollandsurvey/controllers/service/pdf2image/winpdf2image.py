# -*- coding: utf-8 -*- 
import subprocess
import os
import traceback
import sys

class WinPDF2Image(object):
    
    GHOSTSCRIPTCMD = "C:/Program Files/gs/gs9.18/bin/gswin64.exe" 
    RESOLUTION = '200x200'
    def __init__(self):
        #filepath = "test.pdf"
        #self.gs_pdf_to_png(os.path.join(os.getcwd(), filepath), self.resolution)
        pass;
   
   
    def convert2Image(self,pdfFilePath,destinationPath):
        self.result = False;
        if not os.path.isfile(pdfFilePath):
            print "'%s' is not a file. Skip." % pdfFilePath
        #pdffiledir = os.path.dirname(pdfFilePath)
        #pdffilename = os.path.basename(pdfFilePath)
        #pdfname, ext = os.path.splitext(pdfFilePath)
     
        try:    
            # Change the "-rXXX" option to set the PNG's resolution.
            # http://ghostscript.com/doc/current/Devices.htm#File_formats
            # For other commandline options see
            # http://ghostscript.com/doc/current/Use.htm#Options
            arglist = [self.GHOSTSCRIPTCMD,
                      "-dBATCH",
                      "-dNOPAUSE",
                      #"-sOutputFile=%s.png" % destinationPath,
                      "-sOutputFile=%s" % destinationPath,
                      "-sDEVICE=png16m",
                      "-sPAPERSIZE=a6",
                      "-r%s" % self.RESOLUTION,
                      pdfFilePath]
            print "Running command:\n%s" % ' '.join(arglist)
            sp = subprocess.Popen(
                args=arglist,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            self.result = True
        except OSError:
            sys.exit("Error executing Ghostscript ('%s'). Is it in your PATH?" % self.GHOSTSCRIPTCMD)            
        except:
            print "Error while running Ghostscript subprocess. Traceback:"
            print "Traceback:\n%s"%traceback.format_exc()
     
        stdout, stderr = sp.communicate()
        print "Ghostscript stdout:\n'%s'" % stdout
        if stderr:
            print "Ghostscript stderr:\n'%s'" % stderr
        return self.result
            
#pdf = WinPDF2Image();
#pdfFilePath = "d:\Tong\Code/code_python/file_python/test.pdf";
#destinationPath = "d:/Tong/Code/code_python/file_python/test12334";
#pdf.convert2Image(pdfFilePath, destinationPath);
 
        