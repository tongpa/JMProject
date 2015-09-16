
Ext.define('survey.view.ptrack.ListManageTrackInvitation',{
	extend : 'Ext.grid.Panel',
	alias: ['widget.listManageTrackInvitation'],
     
	anchor: '100%',
	viewConfig: {
        emptyText: 'No images to display'
    },
    collapsible:false ,
	store: survey.listInvitationNumberData,
	hideHeaders : false,
    getHeaderColumn : function(){
    	
    	var main = this;
    	return [	{xtype: 'rownumberer',width : '3%'},
    	        	{header: 'id',   sortable: false, dataIndex: 'id_voter' ,hidden : true,menuDisabled: true},        	 
    	        	{header: 'Email', dataIndex: 'email',  width : '25%',   sortable: false,menuDisabled: true}   ,
    	        	{header: 'Name', dataIndex: 'name',  width : '25%',   sortable: false,menuDisabled: true}   ,
    	        	{header: 'Date', dataIndex: 'last_create_date',  width : '15%',   sortable: false,menuDisabled: true}   ,
    	        	{header: 'send no.', dataIndex: 'no_send',  width : '10%',   sortable: false,menuDisabled: true}    
    	        	 
    	        ];
    } ,
    getPagingToolsBar : function(){
    	var main = this;
    	return [{
            xtype: 'pagingtoolbar',
            store: main.store, // same store GridPanel is using
            dock: 'bottom',
            displayInfo: true ,
            listeners:{
		         scope: main,
		         'beforechange' : function(pagingtoolsbar,params){
		        	 console.log("before reload");
		        	 main.reloadData(main.ipOption);
		        	 return false;
		         }
            }
            //,pageSize: main.store.pageSize

        }]
    },
    reloadData : function(idOption){
    	var main = this;
    	main.ipOption = idOption;
    	 main.store.load({
			params : {
				idOption : idOption
    		},
    		scope : this
		});
    },
	initComponent : function(){
		main = this;
    	main.columns = main.getHeaderColumn();
    	
    	this.dockedItems = main.getPagingToolsBar();
    	
		this.callParent();
		
		
	}
});

   