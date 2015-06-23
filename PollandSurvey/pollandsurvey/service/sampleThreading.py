import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class SampleThreading(threading.Thread):

    def run(self):
        logging.debug('running')
        
       #use page 
        
        self.line_in_page = 100000;
        self.page_size = 1000
        num = 1;
        # total size 
        size = 100000 #model.EmailTemp.getSizeForExport();
        import math;
        self.numPage = int( math.ceil(size/self.line_in_page));
        print  self.numPage ; 
        
        self.totalPage =  (size/self.page_size) + 1;
        
        for nPage in range(0,self.numPage):
            print "page : ", nPage;
            for num in range(0,self.totalPage):
                print ( "%s to %s" ,num , (num*self.page_size));
                #print ( "%s to %s" ,num , (self.page_size));
        
        from datetime import datetime
        
        startTime  = datetime.now();
        
        print startTime.strftime("%Y-%m-%d-%H-%M-%S")
        """
        for i in range(5):
            t = SampleThreading1()
            t.start()
        """

class SampleThreading1(threading.Thread):

    def run(self):
        logging.debug('running')
        return
    

for i in range(1):
    t = SampleThreading()
    t.start()