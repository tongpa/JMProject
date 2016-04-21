import json
from datetime import datetime
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
        
    @property
    def json(self):
        return self.to_json( self.__class__)
        
    def to_json(self, cls):
        """
        Jsonify the sql alchemy query result.
        """
        convert = dict()
        # add your coversions for things like datetime's 
        # and what-not that aren't serializable.
        d = dict()
        for c in cls.__table__.columns:
            v = getattr(self, c.name)
           
            if c.type in convert.keys() and v is not None:
               
                try:
                    d[c.name] = convert[c.type](v)
                except:
                    d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
            elif v is None:
                
                d[c.name] = str()
            else:
                if isinstance(v, datetime):
                   
                    d[c.name] =   v.isoformat()
                else:
                    d[c.name] = v
           
                
        #return json.dumps(d )
        return d 
