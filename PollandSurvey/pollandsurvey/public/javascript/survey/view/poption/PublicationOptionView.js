 

Ext.define('survey.view.poption.PublicationOptionView',{
	extend : 'Ext.form.Panel',
	alias: ['widget.PublicationOptionView'],
	fieldLabel :'', 
	frame: false,
	bodyPadding: 10,
	showClose : true,
    defaults: {
        anchor: '100%',
        labelWidth: 120
    },
    isCreate : true,
    parentForm : null,
    setLoadData : function(projectRecord,optionsrecord ){
    	var main = this;
    	main.record =  projectRecord; 
    	main.idquestion.setValue('');
    	main.record = optionsrecord;
    	main.getForm().reset();
		
		console.log(projectRecord);
    	console.log(optionsrecord);
    	
    	if(optionsrecord != null && optionsrecord.id != null){
    		//show only have option
    		main.idquestion.setValue(optionsrecord.id);
    		main.getForm().loadRecord(optionsrecord);
    		
    		//set save button is hidden when send to voter already 
    		if(optionsrecord.data.send_status == 1){
    			
    			main.btsave.setHidden(true);
    		}
    		
    		main.lenghtQuestion = survey.listQuestionsData.data.length;
    		main.useQuestionNo.setMaxValue(main.lenghtQuestion);
    		main.useQuestionNo.setMinValue( 0 );
    	//	console.log(main.lenghtQuestion);
    		
    		main.labelAllQuestion.setText( main.getQuestionNo(main.lenghtQuestion) );
    	}
    	else{
    	
			if (projectRecord != null && projectRecord.id != null) {
					main.projectid = projectRecord.id;
			    		 
					main.idquestion.setValue(this.projectid);
		   }
    	}
    	
    	
    	
    },
	createHtmlEditor : function(fieldName){
		return Ext.create('Ext.form.field.HtmlEditor',{name:fieldName,enableColors: false,enableAlignments: false});
	},
	getQuestionNo : function(lenghtQuestion){
		var main = this;
		 
		main.templateData = new Ext.Template(
				survey.label.all, ' ',
			        '{questionNo}', ' ',
			        survey.label.question
		);
		
		return main.templateData.apply({questionNo:  lenghtQuestion});
		 
	},
	initComponent : function(){
		var main = this;
		main.idoptions = Ext.create('Ext.form.field.Hidden',{name : 'id_question_option'} );    
		main.idquestion = Ext.create('Ext.form.field.Hidden',{name :'id_question_project' } );    
		
		main.optionName = Ext.create('Ext.form.field.Text',{name : 'name_publication',fieldLabel : survey.label.name, allowBlank : false});
		main.showTheme = Ext.create('Ext.form.ComboBox',{name : 'id_question_theme',fieldLabel : survey.label.theme,
			store: survey.listOptionTheme,
			queryMode: 'local',
			displayField: 'description',
			valueField: 'id_question_theme',
			editable : false,
			value : 1, allowBlank : false,
			listeners:{
		         scope: main,
		         'select': function ( combo, record, eOpts ){
		        	 console.log(record);
		         }
		    }
		});
		
		main.RandomType = Ext.create('Ext.form.ComboBox',{name : 'id_fix_random_type',fieldLabel : survey.label.random_type,
			store: survey.listRandomType,
			queryMode: 'local',
			displayField: 'description',
			valueField: 'id_fix_random_type',
			editable : false,
			value : 1, allowBlank : false});
		
		main.emailTemplate = Ext.create('Ext.form.ComboBox',{name : 'id_question_invitation',fieldLabel : survey.label.email_template,
			store: survey.listInvitationData,
			queryMode: 'local',
			displayField: 'name_content',
			valueField: 'id_question_invitation',
			editable : false,
			allowBlank : false
		});
		
		main.startDate = Ext.create('Ext.form.field.Date',{name : 'activate_date',fieldLabel : survey.label.start_date, format: 'd/m/Y',allowBlank: false ,editable : false});
		main.finishDate = Ext.create('Ext.form.field.Date',{name : 'expire_date',fieldLabel : survey.label.expire_date, format: 'd/m/Y',allowBlank: false ,editable : false});
		
		main.redirectURL = Ext.create('Ext.form.field.Text',{name : 'redirect_url',fieldLabel : survey.label.redirect_url, allowBlank: true  });
		
		main.useQuestionNo = Ext.create('Ext.form.field.Number', {name: 'use_question_no',hideLabel : true, fieldLabel: survey.label.use_question_no,allowBlank:true,keyNavEnabled: true,
	        mouseWheelEnabled: true,maxValue: 99,minValue: 0});
		main.labelAllQuestion = Ext.create('Ext.form.Label',{ text: main.getQuestionNo(),margin: '4 0 0 10'});

		main.durationTime = Ext.create('Ext.form.field.Number', {name: 'duration_time',hideLabel : true, fieldLabel: survey.label.duration_time,allowBlank:true,keyNavEnabled: true,
	        mouseWheelEnabled: true,maxValue: 120,minValue: 0});
		main.labelDurationTime = Ext.create('Ext.form.Label',{ text: survey.message.help_duration_time,margin: '4 0 0 10'});
		
		main.showQuestionNo = Ext.create('Ext.form.FieldContainer',{
			layout : 'hbox',
			
			fieldLabel : survey.label.use_question_no,
			items :[
			        main.useQuestionNo,main.labelAllQuestion
			]
		});
		
		
		main.showNavigator = Ext.create('Ext.form.FieldContainer',{name : 'navigator',defaultType: 'radiofield',
			defaults: {
		        flex: 1
		    },
		    layout: 'hbox',
			fieldLabel : survey.label.show_navigator,
			allowBlank : false,
			items: [
		             {
		                boxLabel  : survey.label.show_navigator_yes,
		                name      : 'show_navigator',
		                inputValue: '1' 
		                 
		            },
		            {
		                boxLabel  : survey.label.show_navigator_no,
		                name      : 'show_navigator',
		                inputValue: '0' 
		            }
		     ]  });
		
		main.showScore = Ext.create('Ext.form.FieldContainer',{name : 'navigator',defaultType: 'radiofield',
			defaults: {
		        flex: 1
		    },
		    layout: 'hbox',
			fieldLabel : survey.label.show_score,
			allowBlank : false,
			items: [
		             {
		                boxLabel  : survey.label.show_navigator_yes,
		                name      : 'show_score',
		                inputValue: '1' 
		                 
		            },
		            {
		                boxLabel  : survey.label.show_navigator_no,
		                name      : 'show_score',
		                inputValue: '0' 
		            }
		     ]  });
		
		main.randomAnswer = Ext.create('Ext.form.FieldContainer',{name : 'navigator',defaultType: 'radiofield',
			defaults: {
		        flex: 1
		    },
		    layout: 'hbox',
			fieldLabel : survey.label.random_answer,
			allowBlank : false,
			items: [
		             {
		                boxLabel  : survey.label.show_navigator_yes,
		                name      : 'random_answer',
		                inputValue: '1' 
		                 
		            },
		            {
		                boxLabel  : survey.label.show_navigator_no,
		                name      : 'random_answer',
		                inputValue: '0' 
		            }
		     ]  });
		
		
		main.ShowDurationTime = Ext.create('Ext.form.FieldContainer',{name : 'durationtime' ,
			 
		    layout: 'hbox',
			fieldLabel : survey.label.duration_time,
			defaults: {
				flex: 1,
	            layout: '100%'
	        },
			allowBlank : false,
			items: [main.durationTime,main.labelDurationTime
		     ]  });
		
		
		main.welcome_msg = main.createHtmlEditor('welcome_message') ; 
		main.goodbye_msg = main.createHtmlEditor('end_message') ;  
		main.header_msg = main.createHtmlEditor('header_message') ;  
		main.footer_msg = main.createHtmlEditor('footer_message') ;   
		
		main.tabMessage = Ext.create('Ext.tab.Panel', {
			height: 150,
			items: [
			        {
			        	title : survey.label.welcome_message ,
			        	layout: 'fit',
			        	items : [main.welcome_msg]
			        } ,
			        {
			        	title : survey.label.goodbye_message ,
			        	layout: 'fit',
			        	items : [main.goodbye_msg]
			        },
			        {
			        	title : survey.label.header_message ,
			        	layout: 'fit',
			        	items : [main.header_msg]
			        },
			        {
			        	title : survey.label.footer_message ,
			        	layout: 'fit',
			        	items : [main.footer_msg]
			        } 
			        
			]
		});
		
		
		main.items = [main.idoptions,main.idquestion,main.optionName,main.showTheme,main.showNavigator,main.showScore,main.RandomType,main.randomAnswer,main.showQuestionNo,main.ShowDurationTime ,main.emailTemplate,main.startDate,main.finishDate,main.redirectURL,main.tabMessage];
		
		
		main.btsave = Ext.create('Ext.Button',{		 
			text : survey.label.save,
			 
			formBind: true,  
	        disabled: true,
			handler : function(bt,ev){
				var form = this.up('form').getForm();
				
	            if (form.isValid()) {
	                form.submit({
	                	scope: this,
	                	method: 'POST',
	                	 
	                	waitMsg: survey.message.waiting_save ,
	                    success: function(form, action) {
	                    	
	                    	
	                    	console.log(action);
	                    	if( action.result.result){
	                    		
	                    		main.closeWindow(bt);
		                    	Ext.Msg.alert( survey.message.success , action.result.message);
		                    	main.refreshOther();
	                    		
	                    		
	                    		
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
	refreshOther : function(){
		console.log("refresh other from panel");
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

   