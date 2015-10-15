 

Ext.define('survey.view.pproject.ProjectView',{
	extend : 'Ext.form.Panel',
	alias: ['widget.ProjectView'],
	
	frame: false,
	bodyPadding: 10,
	showClose : true,
    defaults: {
        anchor: '100%',
        labelWidth: 120
    },
    isCreate : true,
    parentForm : null,
    setDefaultField : function(){
    	var main = this;
    	 
    	 
    	 
    	 main.fieldSets.setHidden(true);
    	 main.btsave.setDisabled(false);
    	 /*
         main.fieldHeaderMessage.setHidden(true);
         main.fieldFooterMessage.setHidden(true);
         main.fieldWelcomeText.setHidden(true);
         main.fieldEndText.setHidden(true);*/
    },
    setEditField : function(){
    	var main = this;
    	
    	 main.fieldSets.setVisible(true);
    	 
    	 /*
        main.fieldHeaderMessage.setVisible(true);
        main.fieldFooterMessage.setVisible(true);
        main.fieldWelcomeText.setVisible(true);
        main.fieldEndText.setVisible(true);*/
    },
    resetData :function(){
    	this.getForm().reset();
    },
	initComponent : function(){
		var main = this;
		
		main.projectid = Ext.create('Ext.form.field.Hidden',{name : 'id_question_project'} );
		main.name = Ext.create('Ext.form.field.Text',{
			msgTarget: 'side',name : 'name',fieldLabel: survey.label.project_name ,allowBlank: false 
		} );
		
		
		main.description = Ext.create('Ext.form.field.Text' ,{msgTarget: 'side',name : 'description',
			fieldLabel: survey.label.description  , allowBlank: true });
		 
		
		main.projectType = Ext.create('Ext.form.ComboBox',{msgTarget: 'side',name : 'id_question_project_type',
			fieldLabel: survey.label.project_type   ,  
			allowBlank: false ,
			store: survey.listProjectType,
		    queryMode: 'local',
		    displayField: 'description',
		    valueField: 'id_question_project_type',
		    blankText : survey.label.please_select  ,
		    emptyText : survey.label.please_select });
		
		 
		 
		main.fieldHeaderMessage = Ext.create('Ext.form.field.Text',{msgTarget: 'side',name : 'header_message',
			fieldLabel: survey.label.header_message  , 
			allowBlank: true });//,hidden : main.isCreate});
		
		main.fieldHeaderMessage = Ext.create('Ext.form.field.Text',{msgTarget: 'side',name : 'footer_message',
			fieldLabel: survey.label.footer_message  , 
			allowBlank: true });//,hidden : main.isCreate}); 
		
		main.fieldHeaderMessage = Ext.create('Ext.form.field.Text',{msgTarget: 'side',name : 'welcome_text',
			fieldLabel: survey.label.welcome_message  , 
			allowBlank: true });//,hidden : main.isCreate}); 
		
		main.fieldHeaderMessage = Ext.create('Ext.form.field.Text',{msgTarget: 'side',name : 'end_text',
			fieldLabel: survey.label.goodbye_message  , 
			allowBlank: true });//,hidden : main.isCreate}); 
		
		 
		
		 
		main.fieldSets = Ext.create('Ext.form.FieldSet',{
			title: survey.label.detail  ,
	        collapsible: true,
	        collapsed: true,
	        hidden : main.isCreate,
	        defaults: {
	            labelWidth: 120,
	            anchor: '100%',
	            layout: {   type: 'fix' }
	        },
	        items : [main.fieldHeaderMessage,
		              main.fieldFooterMessage,
		              main.fieldWelcomeText,
		              main.fieldEndText]
		});
		 
		
		main.items = [main.projectid, main.name, main.description, main.projectType  ];  //, main.fieldSets
		
		main.btsave = Ext.create('Ext.Button',{		 
			text : survey.label.save,
			iconCls : 'project-add', 
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
	                    	
	                    	
	                    	 
	                    	
	                    	 
	                    	if( action.result.success){
	                    		
	                    		//main.closeWindow(bt);
	                    		
	                    		main.refreshOther();
		                    	Ext.Msg.alert( survey.message.success , action.result.message);
		                    	
	                    		
	                    		
	                    		
	                    	}
	                    	else{
	                    		Ext.Msg.alert(survey.message.success, action.result.message);
	                    	}
	                    		
	                    	
	                    	//main.refreshOther();
	                    },
	                    failure: function(form, action) {
	                    	 
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
			
			//hidden : !main.showClose,
			handler: function (bt,ev){
				 
				main.closeWindow (bt);
			}
		});
		
		main.buttons = [ main.btsave,main.btclose];
		this.callParent();
	},
	refreshOther : function(){
		 
		this.fireEvent('refreshOther', this);
		
	},
	closeWindow : function ( bt){
		
		var main = this;
		main.form.reset();
		if(main.ownerCt != null){
			//debugger;
			if(main.ownerCt.ownerCt){
				main.ownerCt.ownerCt.close();
			}
			else{
				main.ownerCt.hide();
			}
			//
			
		}
		
		 
	}
});

   