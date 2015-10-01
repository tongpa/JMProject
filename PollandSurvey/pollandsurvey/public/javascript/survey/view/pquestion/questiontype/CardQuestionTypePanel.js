 

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
               'survey.view.pquestion.questiontype.QuestionListAnswerPanel'
               
    ],
    setLoadData : function(projectrecord,questionrecord,questiontyperecord){
   	
	   	if(( questiontyperecord != null &&  questiontyperecord.data.type.toLowerCase().search("image") >=0) || 
	   		(questionrecord!=null && questionrecord.data.question_type_name.toLowerCase().search("image") >=0)  ){
	   		this.layoutpanel.getLayout().setActiveItem(0);
	   	}    
	   	else
	   	{
	   		this.layoutpanel.getLayout().setActiveItem(1);
	   	}
	   	
	   	this.choose.setLoadData(projectrecord,questionrecord);
	   	 
	   	this.images.setLoadData(projectrecord,questionrecord);
	   	
	    
   },
   	
   	initComponent: function() {
       	
       	var main = this;
       	
       	main.images =  Ext.create('survey.view.pquestion.questiontype.QuestionImageAnswerPanel',{visiableColumns : [true,true,true,true,true]});
       	main.choose = Ext.create('survey.view.pquestion.questiontype.QuestionListAnswerPanel');  
       	
       	main.layoutpanel = Ext.create('Ext.panel.Panel',{
       		layout : 'card',
       		items : [main.images,main.choose]
       	});
       	
       	main.items = [main.layoutpanel];
       	
       	//main.layoutpanel.getLayout().setActiveItem(1);
       	this.callParent();
       	
   	},
   createQuestionImage : function(visiableColumns){
	   return Ext.create('survey.view.pquestion.questiontype.QuestionImageAnswerPanel',{visiableColumns : visiableColumns});
   }
});

   