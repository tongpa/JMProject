
 


Ext.define('survey.panel.ManageProject',{
	//extend : 'Ext.panel.Panel', 	 
	extend : 'Ext.form.Panel',
	layout: 'fit',
	alias: ['widget.ManageProject'],
	defaults: {
        anchor: '100%',
        labelWidth: 100
    },
	frame: true,
	
	 
	bodyPadding: 10,
	showClose : true,
    
    isCreate : true,
    parentForm : null,
    url : '',
     
    setLoad : function (record){
    	
    	var main = this;
    	main.record = record;
		
    	main.getForm().reset();
		
    	main.getForm().loadRecord(record);
    	main.currentRecord = record;
    	
    },
    initComponent: function() {
		
    	
    	var main = this;
		
		main.panelProject = Ext.create('survey.view.Project.ProjectView' ,{
			url : main.url,
			showClose : false,
			isCreate : false, 
			listeners : {
				refreshOther : function(cmp) {
		            //this.parentForm.refreshOther();
		        }
		    }});
		this.items = [main.panelProject] ;
		
		this.callParent();
    	
    	 
    }
    
});    