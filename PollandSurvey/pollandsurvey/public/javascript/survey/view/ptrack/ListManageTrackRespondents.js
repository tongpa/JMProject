
Ext.define('survey.view.ptrack.ListManageTrackRespondents',{
	extend : 'Ext.grid.Panel',
	alias: ['widget.listManageTrackRespondents'],
     
	anchor: '100%',
	viewConfig: {
        emptyText: 'No images to display'
    },
    collapsible:false ,
	store: survey.listTrackVoterData,
	hideHeaders : false,
    getHeaderColumn : function(){
    	
    	var main = this;
    	return [	{xtype: 'rownumberer',width : '3%'},
    	        	{header: 'id',   sortable: false, dataIndex: 'id_voter' ,hidden : true,menuDisabled: true},        	 
    	        	{header: 'Email', dataIndex: 'email',  width : '20%',   sortable: false,menuDisabled: true}   ,
    	        	{header: 'Name', dataIndex: 'name',  width : '20%',   sortable: false,menuDisabled: true}   ,
    	        	{header: 'Date', dataIndex: 'respondent_data',  width : '15%',   sortable: false,menuDisabled: true}   ,
    	        	{header: 'IP', dataIndex: 'response_ip',  width : '10%',   sortable: false,menuDisabled: true}   ,
    	        	 
    	        	 
    	        	{ header: 'View',dataIndex: 'status',  width : '10%',   sortable: false, menuDisabled: true, 
    	        			renderer: main.showResult
    	        	} 	 
    	        ];
    } ,
    getPagingToolsBar : function(){
    	var main = this;
    	return [{
            xtype: 'pagingtoolbar',
            store: main.store, // same store GridPanel is using
            dock: 'bottom',
            displayInfo: true,
            listeners:{
		         scope: main,
		         'beforechange' : function(pagingtoolsbar,params){
		        	 console.log("before reload");
		        	 main.reloadData(main.ipOption);
		        	 return false;
		         }
           }
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
		
		
	},
	showResult : function (value,m,r,rowIndex, colIndex, store){
    	var main = this;
    	var id = Ext.id();
    	
        Ext.defer(function () {
            Ext.widget('button', {
                renderTo: id,
                hidden : (value == 1)? false:true, 
                iconCls : 'icon-view',
                text: survey.label.view , 
              
                handler: function (button, evt) {
                	  
                    main.fireEvent('viewResult', this,r);   
                	
                 
                }
            });
        }, 50);
        return Ext.String.format('<div id="{0}"></div>', id);
   
    }
});

   