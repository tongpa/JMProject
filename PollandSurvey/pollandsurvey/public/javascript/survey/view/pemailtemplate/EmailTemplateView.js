 

Ext.define('survey.view.pemailtemplate.EmailTemplateView',{
	extend : 'Ext.form.Panel',
	alias: ['widget.EmailTemplateView'],
	
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
		 
    	if(optionsrecord != null && optionsrecord.id != null){
    		 
    		this.idquestion.setValue(optionsrecord.id);
    		this.getForm().loadRecord(optionsrecord);
    	}
    	else{
    	
			if (projectRecord != null && projectRecord.id != null) {
			    		this.projectid = projectRecord.id;
			    		this.idquestion.setValue(this.projectid);
		   }
    	}
    },
	
	initComponent : function(){
		var main = this;
		
		main.idquestion = Ext.create('Ext.form.field.Hidden',{name : 'id_question_project'} );
		main.idinvitation = Ext.create('Ext.form.field.Hidden',{name : 'id_question_invitation'} );
		
		main.nameContent = Ext.create('Ext.form.field.Text',{name : 'name_content',fieldLabel : survey.label.name_content, allowBlank : false});
		main.subjectinvitation = Ext.create('Ext.form.field.Text',{name : 'subject',fieldLabel : survey.label.email_title, allowBlank : false});
		main.fromName = Ext.create('Ext.form.field.Text',{name : 'from_name',fieldLabel : survey.label.from_name, allowBlank : true});
		
		main.content = Ext.create('Ext.form.field.HtmlEditor',{name : 'content',enableColors: false, enableAlignments: false});
		 
		
		
		main.items = [main.idquestion,main.idinvitation,main.nameContent,main.subjectinvitation,main.fromName,main.content];
		
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
			main.ownerCt.hide();
		}
		
		 
	}
});

   