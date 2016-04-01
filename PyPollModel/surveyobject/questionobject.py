
from surveymodel.survey import Question
class QuestionObject(object):
    
    question = None
    
    def __init__(self, id_question_type=None, image_upload=None, id_question=None, id_question_project=None, question=None,
                 id_fix_difficulty_level=None, datagrid=None, order=None, help_message=None):
        
        self.id_question_type=id_question_type        
        self.image_upload=image_upload        
        self.id_question=id_question        
        self.id_question_project=id_question_project        
        self.question=question        
        self.id_fix_difficulty_level=id_fix_difficulty_level        
        self.datagrid=datagrid        
        self.order=order        
        self.help_message=help_message
        
        self.question = Question(id_question = self.id_question, id_question_type= self.id_question_type,id_question_project= self.id_question_project,  
                                 id_fix_difficulty_level= self.id_fix_difficulty_level, question= self.question, help_message = self.help_message, order= self.order) 