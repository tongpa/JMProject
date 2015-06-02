 

Ext.define('survey.view.pvariable.ListVariableTemplateView',{
	extend : 'Ext.form.Panel',
	alias: ['widget.ListVariableTemplateView'],
	 
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
    	 
    	console.log('setDefaultField');
    	 
      
    },
    setEditField : function(){
    	var main = this;
    	
    	  
    },
    resetData :function(){
    	this.getForm().reset();
    },
	initComponent : function(){
		var main = this;
		
		 
		
		main.items = [ 
					
					];
		 
		
		
		
		 
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

   