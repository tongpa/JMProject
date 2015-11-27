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
    setLoad : function (projectRecord,page){
    	
    	page = typeof page !== 'undefined' ? page : 1;
    	
    	this.projectid = '';
    	this.record = projectRecord;
    	if (projectRecord != null && projectRecord.id != null) {
    		
    		this.projectid = projectRecord.id;
    		 
    		this.store1.loadPage(page,{
				params : {
	    			projectid : projectRecord.id
	    		},
	    		scope : this
			});
    	}
    	
    },
    initComponent: function() {
		
		var main = this;
		
		 
		main.panel  = Ext.create('survey.view.ptrack.ListManageTrackInvitation' ,{store : main.store}  );
		
	 
		
		main.listPublication  = Ext.create(
				'survey.view.customs.CustomCombobox' 
				 
				//'survey.panel.ManageTrackInvitation.ListPublicationCombobox' 
				,{
			name : 'id_question_theme',
			fieldLabel : survey.label.create_publication,
			store: main.store1,
			displayField: 'name_publication',
			valueField: 'id_question_option',
			
			//allowBlank : false,
			listeners:{
		         scope: main,
		         'select': function ( combo, records, eOpts ){
		        	 if(records.length ==1)
		        		 main.panel.reloadData(records[0].id);
		        	 
		         },
		         afterrender: function(combo) {
		        	
		        	 if(combo.getStore().count() > 0){
		        		var recordSelected = combo.getStore().getAt(0);      
		        		 combo.setValue(recordSelected.get('id_question_option'));
		        		 main.panel.reloadData( recordSelected.get('id_question_option') );
		        		 recordSelected = null;
		        	 }
		         },
		         changeDataValue :function(paging,page){
		        	main.setLoad(main.record,page);
		         }
		         
		       
		    }}  );
		
		 
		
		main.tbar =  [  main.listPublication ];
		  
		main.items = [main.panel ];
		
		this.callParent();
    } 
    
});    


Ext.define('survey.panel.ManageTrackInvitation.ListPublicationCombobox',{
	extend : 'Ext.form.field.ComboBox',
	initComponent: function() {
		var main = this;
		
		
		
		this.callParent();
	},
	/**override*/
	onPageChange: function(toolbar, newPage){
		 
		this.fireEvent('changeDataValue',  toolbar, newPage);
		return false;
	}
	 
});
 