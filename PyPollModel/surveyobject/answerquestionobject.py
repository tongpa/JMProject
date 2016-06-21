# -*- coding: utf-8 -*-
import json
class AnswerquestionObject(json.JSONDecoder):
    finished = False
    value = {}
    
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)
    
    def dict_to_object(self, d):
        print d
        return {}

class objvalue(object):
    def __init__(self, d):
         
        for a, b in d.items():
            
            if isinstance(b, (list, tuple)):
                setattr(self, a, [objvalue(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, objvalue(b) if isinstance(b, dict) else b)
                
            """
            if isinstance(b, (list, tuple)):
                setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, obj(b) if isinstance(b, dict) else b)
            """   
data = """{"value":[
{"id":59982,"idproject":"6099","idresp":"","value":[{"id":120231,"value":"120231"}],"type":"radio"},
{"id":59983,"idproject":"6099","idresp":"","value":[{"id":120234,"value":"120234"}],"type":"radio"},
{"id":59984,"idproject":"6099","idresp":"","value":[{"id":120237,"value":"120237"}],"type":"radio"},
{"id":59985,"idproject":"6099","idresp":"","value":[{"id":120242,"value":"120242"}],"type":"radio"},
{"id":59986,"idproject":"6099","idresp":"","value":[{"id":120243,"value":"120243"}],"type":"radio"},
{"id":59987,"idproject":"6099","idresp":"","value":[{"id":120248,"value":"120248"}],"type":"radio"},
{"id":59988,"idproject":"6099","idresp":"","value":[{"id":120249,"value":"120249"}],"type":"radio"},
{"id":59989,"idproject":"6099","idresp":"","value":[{"id":120254,"value":"120254"}],"type":"radio"}
],"finished":false} """
print data

obj = json.loads(data)

#print(type(obj))
#print obj

x = objvalue(obj)
print x.finished

for v in x.value:
    print v.id