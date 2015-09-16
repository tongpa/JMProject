
 


Ext.define('survey.panel.ManageTrackInvitation',{
	//extend : 'Ext.panel.Panel', 	 
	extend : 'Ext.form.Panel',
	alias: ['widget.manageTrackInvitation'],
	layout: 'fit',
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
    initComponent: function() {
		
		var main = this;
		
		//main.select = Ext.create('survey.view.ptrack.ListPublication');
		main.select =   Ext.create('Ext.form.ComboBox',{name : 'id_question_theme',
			fieldLabel : survey.label.theme,
			store: survey.listOptionTheme,
			queryMode: 'local',
			displayField: 'description',
			valueField: 'id_question_theme',
			editable : false,
			value : 1, 
			allowBlank : false,
			listeners:{
		         scope: main,
		         'select': function ( combo, record, eOpts ){
		        	 console.log(record);
		         }
		    }
		});
		main.panel  = Ext.create('survey.view.ptrack.ListManageTrackInvitation'  );
		
		main.tbar =  [{
            xtype:'combobox',
            name : 'id_question_theme',
			fieldLabel : survey.label.create_publication,
			store: survey.listOptions,
			queryMode: 'local',
			displayField: 'name_publication',
			valueField: 'id_question_option',
			editable : false,
			 
			allowBlank : false,
			listeners:{
		         scope: main,
		         'select': function ( combo, record, eOpts ){
		        	 console.log(record);
		         },
		         afterrender: function(combo) {
		        	 if(combo.getStore().count() > 0){
		        		 console.log("after render ");
		        		 
		        		 var recordSelected = combo.getStore().getAt(0);      
		        		 console.log(recordSelected);
		        		 combo.setValue(recordSelected.get('id_question_option'));
		        		 main.panel.reloadData( recordSelected.get('id_question_option') );
		        		 
		        		 recordSelected = null;
		        	 }
		         }
		       
		    }
        }];
		  
		main.items = [main.panel ];
		
		this.callParent();
    }
    
});    