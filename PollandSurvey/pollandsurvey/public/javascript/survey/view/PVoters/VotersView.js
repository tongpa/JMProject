 

Ext.define('survey.view.PVoters.VotersView',{
	extend : 'Ext.form.Panel',
	alias: ['widget.VotersView'],
	
	frame: false,
	bodyPadding: 10,
	showClose : true,
    defaults: {
        anchor: '100%',
        labelWidth: 120
    },
    
	
	initComponent : function(){
		main = this;
		
		main.voterid = Ext.create('Ext.form.field.Hidden',{name : 'id_voter'} );
		
		main.prefix = Ext.create('Ext.form.field.Text',{name : 'prefix',fieldLabel : survey.label.prefix, allowBlank : true});
		main.firstname = Ext.create('Ext.form.field.Text',{name : 'first_name',fieldLabel : survey.label.first_name, allowBlank : true});
		main.lastname = Ext.create('Ext.form.field.Text',{name : 'last_name',fieldLabel : survey.label.last_name, allowBlank : true});
		main.email = Ext.create('Ext.form.field.Text',{name : 'email',fieldLabel : survey.label.email, allowBlank : false,
			 vtype: 'email' 
			 });
		
		main.gender = Ext.create('Ext.form.RadioGroup',{name : 'groupgender',fieldLabel: survey.label.gender,
			cls: 'x-check-group-alt',
			columns: 3,
		    vertical: true,
		    items: [
		            {boxLabel: survey.label.male, name: 'gender', inputValue: '1'},
		            {boxLabel: survey.label.female, name: 'gender', inputValue: '2'},
		            {boxLabel: survey.label.other, name: 'gender', inputValue: '3', checked: true}
		            ]
		});
		 
		
		
		main.btsave = Ext.create('Ext.Button',{		 
			text : survey.label.save,
			iconCls : 'project-add',
			formBind: true,  
	        disabled: true,
			handler : function(bt,ev){
				var form = this.up('form').getForm();
	            if (form.isValid()) {
	                form.submit({
	                    success: function(form, action) {
	                    	
	                    	//main.closeWindow(main,bt);
	                    	//form.reset();
	                    	console.log(action);
	                    	if( action.result.result){
	                    		Ext.Msg.alert(survey.message.success, action.result.message);
	                    		main.ownerCt.hide(bt);
	                    		form.reset();
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
				//main.closeWindow(main,bt);
				main.ownerCt.hide(bt);
				
				//main.up('form').getForm().reset();
				//main.parentForm.hide(bt);
			}
		});
		
		main.buttons = [ main.btsave,main.btclose];
		
		
		main.items = [main.voterid,main.prefix,main.firstname,main.lastname,main.email,main.gender ];
		
		this.callParent();
	},
	refreshOther : function(){
		this.fireEvent('refreshOther', this);
		
	}
});

   