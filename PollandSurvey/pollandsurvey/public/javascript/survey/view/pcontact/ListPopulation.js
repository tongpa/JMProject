
Ext.define('survey.view.pcoters.ListPopulation',{
	extend : 'Ext.grid.Panel',
	alias: ['widget.ListPopulation'],
     
	anchor: '100%',
	viewConfig: {
        emptyText: 'No images to display'
    },
    collapsible:false ,
	store: survey.listVoterData,
	hideHeaders : true,
    getHeaderColumn : function(){
    	
    	return [	{xtype: 'rownumberer',width : '3%'},
    	        	{header: 'id',   sortable: false, dataIndex: 'id_voter' ,hidden : true,menuDisabled: true},        	 
    	        	{header: 'Email', dataIndex: 'email',  width : '35%',   sortable: false,menuDisabled: true}   ,
    	        	{header: 'Name', dataIndex: 'name',  width : '55%',   sortable: false,menuDisabled: true}   ,
    	        	{
    	                xtype:'actioncolumn',width:'3%', autoSizeColumn : true, menuDisabled:true,
    	                items: [{
    	                	iconCls : 'icon-edit'	, style: 'margin-left: 5px;', tooltip: survey.label.edit, flex: 1, 
    	                    handler: function(grid, rowIndex, colIndex) {
    	                        var rec = grid.getStore().getAt(rowIndex);
    	                        grid.fireEvent('editVoters', this,rec);
    	                        
    	                    }
    	                } ]
    	            },
    	            {
    	                xtype:'actioncolumn', width:'3%', autoSizeColumn : true, menuDisabled:true,
    	                items: [ {
    	                	iconCls : 'icon-delete',
    	                    tooltip: survey.label.delete,
    	                    flex: 1,
    	                    handler: function(grid, rowIndex, colIndex) {
    	                        var rec = grid.getStore().getAt(rowIndex);
    	                        
    	                        Ext.MessageBox.confirm(survey.label.confirm, survey.message.confirm_delete , function(btn){
    	                        	if(btn ==  'yes'){
    	                        		grid.getStore().remove(rec);
	                                    grid.getStore().sync();
	                                   
	                            	}
    	                        });
    	                        
    	                        
    	                        
    	                        
    	                    }
    	                }]
    	            }
    	        	 
    	        ];
    } ,
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

   