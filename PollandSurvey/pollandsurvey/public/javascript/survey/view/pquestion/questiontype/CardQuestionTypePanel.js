 

Ext.define('survey.view.pquestion.questiontype.CardQuestionTypePanel',{
	extend : 'Ext.panel.Panel',
	alias: ['widget.CardPanel'],
	width : '100%',
   	height : '100%',
   	frame: false,
	//fieldLabel :'', 
	frame: false,
	bodyPadding: 10,
	showClose : true,
	url:'',
    defaults: {
        anchor: '100%',
        labelWidth: 120
    },
    isCreate : true,
    parentForm : null,
    requires: [
               'Ext.layout.container.Card',
               'survey.view.pquestion.questiontype.QuestionImageAnswerPanel',
               'survey.view.pquestion.questiontype.QuestionListAnswerPanel',
               'survey.view.pquestion.questiontype.QuestionTextAnswerPanel',
               'survey.view.pquestion.questiontype.QuestionTextAreaAnswerPanel',
               'survey.view.pquestion.questiontype.QuestionTextNumberAnswerPanel'
               
    ],
    setLoadData : function(projectrecord,questionrecord,questiontyperecord){
   	
    	 
    	
    	
    	
    	
	   	if(( questiontyperecord != null &&  questiontyperecord.data.type.toLowerCase().search("image") >=0) || 
	   		(questionrecord!=null && questionrecord.data.question_type_name.toLowerCase().search("image") >=0)  ){
	   		this.layoutpanel.getLayout().setActiveItem(0);
	   	}    
	   	else{
		   	if(( questiontyperecord != null &&  questiontyperecord.data.type.toLowerCase().search("text") >=0) || 
		   		(questionrecord!=null && questionrecord.data.question_type_name.toLowerCase().search("text") >=0)  ){
		   		this.layoutpanel.getLayout().setActiveItem(2);
		   	}
		   	else{
			   	if(( questiontyperecord != null &&  questiontyperecord.data.type.toLowerCase().search("textarea") >=0) || 
			   		(questionrecord!=null && questionrecord.data.question_type_name.toLowerCase().search("textarea") >=0)  ){
			   		this.layoutpanel.getLayout().setActiveItem(3);
			   	}
			   	else{
				   	if(( questiontyperecord != null &&  questiontyperecord.data.type.toLowerCase().search("textnumber") >=0) || 
					   		(questionrecord!=null && questionrecord.data.question_type_name.toLowerCase().search("textnumber") >=0)  ){
					   		this.layoutpanel.getLayout().setActiveItem(4);
					   	}
				   	else
				   	{	//radio, check  
				   		this.layoutpanel.getLayout().setActiveItem(1);
				   	}
			   	}
		   	}
		   	
	   	}
	   	
	   	this.choose.setLoadData(projectrecord,questionrecord);
	   	 
	   	this.images.setLoadData(projectrecord,questionrecord);
	   	
	   	this.text.setLoadData(projectrecord,questionrecord);
	   	this.textArea.setLoadData(projectrecord,questionrecord);
	    this.textNumber.setLoadData(projectrecord,questionrecord);
   },
   	
   	initComponent: function() {
       	
       	var main = this;
       	
       	main.images =  Ext.create('survey.view.pquestion.questiontype.QuestionImageAnswerPanel',{visiableColumns : [true,true,true,true,true]});
       	main.choose = Ext.create('survey.view.pquestion.questiontype.QuestionListAnswerPanel');  
       	main.text = Ext.create('survey.view.pquestion.questiontype.QuestionTextAnswerPanel');
       	main.textArea = Ext.create('survey.view.pquestion.questiontype.QuestionTextAreaAnswerPanel');
       	main.textNumber = Ext.create('survey.view.pquestion.questiontype.QuestionTextNumberAnswerPanel');
       	
       	
       	main.layoutpanel = Ext.create('Ext.panel.Panel',{
       		layout : 'card',
       		items : [main.images,main.choose,main.text,main.textArea,main.textNumber]
       	});
       	
       	main.items = [main.layoutpanel];
       	
       	//main.layoutpanel.getLayout().setActiveItem(1);
       	this.callParent();
       	
   	},
   createQuestionImage : function(visiableColumns){
	   return Ext.create('survey.view.pquestion.questiontype.QuestionImageAnswerPanel',{visiableColumns : visiableColumns});
   }
});

   