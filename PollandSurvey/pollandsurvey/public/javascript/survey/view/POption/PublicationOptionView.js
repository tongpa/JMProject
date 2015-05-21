 

Ext.define('survey.view.POption.PublicationOptionView',{
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
    	
    	this.record =  projectRecord; 
    	this.idquestion.setValue('');
    	this.record = optionsrecord;
		this.getForm().reset();
		
		console.log(projectRecord);
    	console.log(optionsrecord);
    	
    	if(optionsrecord != null && optionsrecord.id != null){
    		 
    		this.idquestion.setValue(optionsrecord.id);
    		this.getForm().loadRecord(optionsrecord);
    		
    		//set save button is hidden when send to voter already 
    		if(optionsrecord.data.send_status == 1){
    			
    			this.btsave.setHidden(true);
    		}
    	}
    	else{
    	
			if (projectRecord != null && projectRecord.id != null) {
			    		this.projectid = projectRecord.id;
			    		 
			    		this.idquestion.setValue(this.projectid);
		   }
    	}
    },
	createHtmlEditor : function(fieldName){
		return Ext.create('Ext.form.field.HtmlEditor',{name:fieldName,enableColors: false,enableAlignments: false});
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
								value : 1, allowBlank : false});
		
		main.emailTemplate = Ext.create('Ext.form.ComboBox',{name : 'id_question_invitation',fieldLabel : survey.label.email_template,
			store: survey.listInvitationData,
			queryMode: 'local',
			displayField: 'name_content',
			valueField: 'id_question_invitation',
			editable : false,
			allowBlank : false});
		
		main.startDate = Ext.create('Ext.form.field.Date',{name : 'activate_date',fieldLabel : survey.label.start_date, format: 'd/m/Y',allowBlank: false ,editable : false});
		main.finishDate = Ext.create('Ext.form.field.Date',{name : 'expire_date',fieldLabel : survey.label.expire_date, format: 'd/m/Y',allowBlank: false ,editable : false});
		
		main.redirectURL = Ext.create('Ext.form.field.Text',{name : 'redirect_url',fieldLabel : survey.label.redirect_url, allowBlank: true  });
		
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
		
		
		main.welcome_msg = main.createHtmlEditor('welcome_message') ; 
		main.goodbye_msg = main.createHtmlEditor('end_message') ;  
		main.header_msg = main.createHtmlEditor('header_message') ;  
		main.footer_msg = main.createHtmlEditor('footer_message') ;   
		
		main.tabMessage = Ext.create('Ext.tab.Panel', {
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
		
		
		main.items = [main.idoptions,main.idquestion,main.optionName,main.showTheme,main.showNavigator ,main.emailTemplate,main.startDate,main.finishDate,main.redirectURL,main.tabMessage];
		
		
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

   