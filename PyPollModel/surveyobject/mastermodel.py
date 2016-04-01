
class MasterBase(object):
    
    def __init__(self,dbSession):
        self.DBSession = dbSession
        
    
    def save(self):
        #self.id_user =None;
        print "save"
        self.DBSession.add(self);
        self.DBSession.flush()
    
    def updateall(self):
        print "update"
        self.DBSession.merge(self,load=True)
        #DBSession.update(self);
        
    def remove(self):
        self.DBSession.delete(self); 
        self.DBSession.flush() ;
