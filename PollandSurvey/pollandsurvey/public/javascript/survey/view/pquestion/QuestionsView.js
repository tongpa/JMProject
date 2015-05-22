 

Ext.define('survey.view.pquestion.QuestionsView',{
	extend : 'Ext.form.Panel',
	alias: ['widget.QuestionsView'],
	requires: [
	           'survey.view.pquestion.ImageView',
               'survey.view.pquestion.questiontype.CardQuestionTypePanel'
    ],
	fieldLabel :'', 
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
    setLoadData : function (projectrecord,questionrecord, questiontyperecord,numberorder){
    	
    	//console.log('survey.view.list.Project.PAddQuestion');
    	 
    	var form = this;
    	form.projectrecord = projectrecord;
		form.record = questionrecord;
		form.getForm().reset();
		
		if (numberorder == null){
			numberorder =0;
		}
		form.order.setValue(numberorder);
		
		if(questionrecord != null){
			form.getForm().loadRecord(questionrecord);
			 
		}
		
		if(projectrecord != null){			 	
			form.projectid.setValue(projectrecord.id);
		}
		
		//type of question
		if(questiontyperecord != null){		 	
			form.questiontypeid.setValue(questiontyperecord.id);
		}
		form.fileUpload.setLoadData(questionrecord, questiontyperecord);
		 
		
		
 
		//console.log("set data add question");
		//console.log(questionrecord);
		
		//load grid question
		form.answerCardPanel.setLoadData(questionrecord,questiontyperecord);
		//form.answerCardPanel.choose.setLoadData(questionrecord);
    },
	createHtmlEditor : function(fieldName){
		return Ext.create('Ext.form.field.HtmlEditor',{name:fieldName,enableColors: false,enableAlignments: false});
	},
	initComponent : function(){
		var main = this;
		console.log("init Question View");
		main.questionid = Ext.create('Ext.form.field.Hidden',{name: 'id_question',msgTarget: 'side'});
		main.question = Ext.create('Ext.form.field.TextArea',{name : 'question', fieldLabel: survey.label.question  , allowBlank: false,msgTarget: 'side'});
		main.order = Ext.create('Ext.form.field.Hidden',{name : 'order',msgTarget: 'side',value:'0'});
		main.help = Ext.create('Ext.form.field.TextArea',{name :  'help_message', fieldLabel: survey.label.help_message, allowBlank: true ,msgTarget: 'side'});
		
		main.projectid = Ext.create('Ext.form.field.Hidden',{name : 'id_question_project', msgTarget: 'side'});
		
		main.fileUpload = Ext.create('survey.view.pquestion.ImageView',{msgTarget: 'side'});
		
		main.questiontypeid  = Ext.create('Ext.form.field.Hidden',{name : 'id_question_type' });
		
		main.answerCardPanel = Ext.create('survey.view.pquestion.questiontype.CardQuestionTypePanel');
		
		main.dataGrid = Ext.create('Ext.form.field.Hidden',{name : 'datagrid'});
		
		
		
		main.fieldSetsHelp = Ext.create('Ext.form.FieldSet',{
			title: survey.label.help_message,
	        collapsible: true,
	        collapsed: true,
	         
	        defaults: {
	        	hideLabel : true,
	            labelWidth: 120,
	            anchor: '100%',
	            layout: {   type: 'fix' }
	        },
	        items : main.help
		});

		
//		
		 
		main.items = [main.questionid,main.projectid,main.order,main.questiontypeid ,main.dataGrid, main.question ,main.fileUpload, main.fieldSetsHelp,main.answerCardPanel   ];  
		
		main.btsave = Ext.create('Ext.Button',{		 
			text : survey.label.save,
			 
			formBind: true,  
	        disabled: true,
			handler : function(bt,ev){
				var form = this.up('form').getForm();
				
	            if (form.isValid()) {
	            	
	            	
	            	var data = [];
	            	
	            	var items = survey.listBasicData.data.items;
	            	var len = items.length;
	            	
	            	console.log('Get Data From Store');
	            	survey.listBasicData.each(function(record){ 	        	            		 		 
        		 	   data.push(record.data);
        		 	});
	            	
	            	survey.listBasicData.removeAll();
	            	
	            	for(var i = 0; i < len ; i++){
	            		  if (!main.checkInteger(data[i].id_basic_data)){
	            			  data[i].id_question = '';
	            			  data[i].id_basic_data = '';
	            		  }
	            	}
	            	  
	            	
	        		len = survey.listBasicMediaData.data.length;
	        		
	        		//console.log('survey.listBasicMediaData.data.length : ' + survey.listBasicMediaData.data.length);
        		 	
	        		
	        		
	        		for(var i = 0; i < len ; i++){
        		 		var record = survey.listBasicMediaData.data[i];
        		 		if(record == null ){
        		 			record = survey.listBasicMediaData.data.items[i];
        		 		}
        		 		 
        		 		var d = record.data;
        		 		var idQuestion = record.data.id_question;
	        			d.id_question='';
	        			
	        			if (main.checkInteger(record.id)){
	        				d.id_question =  idQuestion;
	        			}
	        			 
	        			
	        			
	        			//console.log(d);
	        			data.push(d);
	        			d = null; 
        		 	}
	        		
	        		
	        		
	        		main.dataGrid.setValue( Ext.encode(data));
	            	
	            	
	            	
	            	
	            	
	                form.submit({
	                	scope: this,
	                	method: 'POST',
	                	 
	                	waitMsg: survey.message.waiting_save ,
	                    success: function(form, action) {
	                    	
	                    	
	                    	console.log(action);
	                    	if( action.result.result){
	                    		
	                    		
		                    	Ext.Msg.alert( survey.message.success , action.result.message);
		                    	main.refreshOther();
		                    	main.closeWindow(bt);
	                    		
	                    		
	                    	}
	                    	else{
	                    		Ext.Msg.alert(survey.message.success, action.result.message);
	                    	}
	                    		
	                    	
	                    	//main.refreshOther();
	                    },
	                    failure: function(form, action) {
	                    	console.log(action); 
	                    	if (action.response.status = '404'){
	                    		
	                    		Ext.Msg.alert(survey.message.failed, action.response.statusText);
	                    		//main.closeWindow(main,bt); 
	                    	}
	                    	else{
	                    		Ext.Msg.alert(survey.message.success, action.result.message);
	                    	}
	                        
	                    }
	                });
	            }
			}
		});
		
		main.btclose = Ext.create('Ext.Button',{		 
			text : survey.label.close,
			
			hidden : !main.showClose,
			handler: function (bt,ev){
				 
				main.closeWindow(bt);
			}
		});
		
		main.buttons = [ main.btsave,main.btclose];
		this.callParent();
	},
 
	checkInteger : function (value) {
		  return !isNaN(value) && (function(x) { return (x | 0) === x; })(parseFloat(value))
	},
	refreshOther : function(){
		 
		this.fireEvent('refreshOther', this);
		
	},
	closeWindow : function (bt){
		
		var main = this;
		main.form.reset();
		if(main.ownerCt != null){
			main.ownerCt.hide();
		}
		
		 
	}
});

   