
Ext.define('survey.view.PVoters.ListVoters',{
	extend : 'Ext.grid.Panel',
	alias: ['widget.ListVoters'],
     
	anchor: '100%',
	viewConfig: {
        emptyText: 'No images to display'
    },
    collapsible:false ,
	store: survey.listVoterData,
    getHeaderColumn : function(){
    	return [	{xtype: 'rownumberer'},
    	        	{header: 'id', width : '9%', sortable: false, dataIndex: 'id_voter' ,hidden : true,menuDisabled: true},        	 
    	        	{header: 'Email', dataIndex: 'email',  width : '45%',   sortable: false,menuDisabled: true}   ,
    	        	{header: 'Name', dataIndex: 'name',  width : '45%',   sortable: false,menuDisabled: true}   
    	        ];
    },
    getPagingToolsBar : function(){
    	var main = this;
    	return [{
            xtype: 'pagingtoolbar',
            store: main.store, // same store GridPanel is using
            dock: 'bottom',
            displayInfo: true
        }]
    },
	initComponent : function(){
		main = this;
    	main.columns = main.getHeaderColumn();
    	
    	this.dockedItems = main.getPagingToolsBar();
    	
		this.callParent();
		
		
	}
});

   