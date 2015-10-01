
 


Ext.define('survey.panel.ManageVariable',{
	//extend : 'Ext.panel.Panel', 	 
	extend : 'Ext.form.Panel',
	layout: 'fit',
	alias: ['widget.ManageVariable'],
	defaults: {
        anchor: '100%',
        labelWidth: 120
    },
	frame: true,
	
	height : 500,
	bodyPadding: 10,
	showClose : true,
    
    isCreate : true,
    parentForm : null,
    setLoad : function (projectRecord){
    	
    	this.projectid = '';
    	this.record = projectRecord;
    	if (projectRecord != null && projectRecord.id != null) {
    		
    		this.projectid = projectRecord.id;
	    	/*survey.listOptions.load({
				params : {
	    			projectid : projectRecord.id
	    		},
	    		scope : this
			});*/
    	}
    	
    },
    initComponent: function() {
		
    	var main = this;
		//main.add111 = Ext.create('survey.view.list.Project.AddQuestion',{msgTarget: 'side'});
		 
		main.tbar =  [{
            xtype:'button',
            text: survey.label.create_publication ,
            iconCls: 'project-add',
            //iconCls: 'add16',
            handler: function(bt,ev){
            	 
            }
            //,            menu: [{text: 'Menu Button 1'}]
        }];
		
		  
		//main.items = main.add111;
		
		this.callParent();
    }
    
});    