 

Ext.define('survey.view.ptrack.ListPublication',{
	extend : 'Ext.form.Panel',
	alias: ['widget.ListPublication'],
	fieldLabel :'', 
	layout: 'fit',
	frame: true,
	bodyPadding: 10,
	//showClose : true,
    defaults: {
        anchor: '100%',
        labelWidth: 120
    },
    isCreate : true,
    parentForm : null,
    setLoadData : function(projectRecord,optionsrecord ){
    	 
    	
    	
    	
    } ,
	 
	initComponent : function(){
		var main = this;
		 
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
		
		 
		
		
		main.items = [ main.showTheme ];
		
		 
		this.callParent();
	},
	refreshOther : function(){
		console.log("refresh other from panel");
		this.fireEvent('refreshOther', this);
		
	} 
});

   