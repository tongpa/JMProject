Ext.define('company.form.btAddPosition',{
	extend: 'Ext.Button',
	text : 'Add Position',
	iconCls : 'img-add',
	disabled : true
});

Ext.define('company.form.btDeletePosition',{
	extend: 'Ext.Button',
	text : 'Delete Position',
	iconCls : 'img-delete',
	disabled : true
});


Ext.define('company.listPosition',{
	
	
	extend: 'Ext.grid.Panel',
	width : '95%',
	//height :  '100%',	 
	 
	
	title: 'Position', 
	bodyPadding: 10,
	showClose : true,
	//autoHeight: true,
	
	viewConfig: {
        emptyText: 'No images to display'
    },
    isCreate : true,
    parentForm : null,
    collapsible:false ,
    autoScroll: true,
     
    resetData : function(){
    	this.addPosition.setDisabled(true);
    	this.store.removeAll();
    },
    
    loadPosition : function(company){
    	
    	this.storeCompany = company;
    	
    	console.log(company);
    	console.log(company.id);
    	//this.store.
    	 
    	this.store.load({
    		params : {
    			'keysearch' : company.id
    		},
    		scope:this,
    		callback : function(records,operation,success){
    			console.log('success');
	    		if(success){
	    			console.log('success');
	    		}
    		}
    	});
    	 
    	if (company.id >0){
    		this.addPosition.setDisabled(false);
    	}
    },
    initComponent: function() {
		
    	var main = this;
    	main.store = company.listPositionStore; 
    	main.columns = [
    	       	       
    	    	    {header: 'position', dataIndex: 'position',width : '20%' , sortable: false }  ,
    	    	    {header: 'experience', dataIndex: 'experience',width : '20%' , sortable: false }  ,
    	    	    {header: 'position number', dataIndex: 'position_no',width : '10%' , sortable: false }  ,
    	    	    {header: 'name of source', dataIndex: 'source',width : '15%' , sortable: false }  ,
    	    	    {header: 'post date', dataIndex: 'post_date',width : '10%',   sortable: false,renderer:Ext.util.Format.dateRenderer('d-m-Y') }  ,
    	    	    {header: 'Edit', dataIndex: 'source',width : '10%' , sortable: false, renderer :main.editPosition }  ,
    	    	    {header: 'Add Post Date', dataIndex: 'source',width : '10%' , sortable: false, renderer :main.addPostDate }  
    	            
    	        ];
    	        
    	main.winAddPosition = Ext.create('company.winAddPosition',{
    		
			listeners : {
				refreshOther : function(cmp) {
		             main.loadPosition(main.storeCompany);
		        }
		    }
    		
    	});
    	
    	main.winPostDate = Ext.create('company.winAddPositionPostDate',{
    		listeners : {
    			refreshOther : function(cmp) {
		             main.loadPosition(main.storeCompany);
		        }
    		}
    	});
    	
    	main.addPosition = Ext.create('company.form.btAddPosition',{
    		parent : main,
    		handler: function () { 
    			 main.winAddPosition.show();
    			 main.winAddPosition.initValue(main.storeCompany);
    			 
    			
    		}
    	} );
    	
    	main.deletePosition = Ext.create('company.form.btDeletePosition',{
    		parent : main,
    		handler: main.onDeleteClick,
    		itemId: 'delete',
            scope: this
    	});
    	main.tbar = [main.addPosition,main.deletePosition ] ;
    	
    	
    	main.dockedItems =  [{
            xtype: 'pagingtoolbar',
            store: main.store, // same store GridPanel is using
            dock: 'bottom',
            displayInfo: true,
            listeners : {
            	scope: main,
            	'beforechange' : main.onBeforeChangePosition,
            }
        }],
    	
    	this.callParent();
    	
    	this.getSelectionModel().on('selectionchange', this.onSelectChange, this);
    	
    },
    
    onBeforeChangePosition : function(paging,page,opt){
		console.log('beforechange');
		 
		 paging.store.loadPage(page,{params : {
			'keysearch' : this.storeCompany.id}
		}); 
		 
		return false;
	},
    onSelectChange: function(selModel, selections){
        
       // this.fireEvent('showCompany', selections[0]);
    	//console.log(selections);
    	this.deletePosition.setDisabled(selections.length === 0);
		 
    },
    onDeleteClick: function(){
    	var selection = this.getView().getSelectionModel().getSelection()[0];
    	var main = this;
        if (selection) {
        	Ext.Msg.show({
    		    title:'Confirm Delete?',
    		    message: 'Do you delete : ' + selection.get('position'),
    		    buttons: Ext.Msg.YESNO,
    		    icon: Ext.Msg.QUESTION,
    		    fn: function(btn) {
    		        if (btn === 'yes') {
    		        	
    		        	 
    		        	
    		        	//main.store.sync();
    		        	
    		        	var value = selection.getData();
    		          
    		        	Ext.Ajax.request({
                            url        : '/WebCompanys/jobs/delJobs',
                            method  : 'POST',
                            jsonData: value,    
                            success: function(response){
                               // var grid = Ext.ComponentQuery.query('bookslist')[0];
                              //  grid.getStore().load();
                            	//main.store.remove(selection);
                            	
                            	main.loadPosition(main.storeCompany);
                            	 
                            	Ext.Msg.show({title:"Delete Status.",message:"Delete Success.", icon: Ext.Msg.QUESTION,
                            	buttons: Ext.Msg.YES}
                            	);
                            },
                            failure: function(response) {
                            	Ext.Msg.show({title:"Delete Status.",message:"Delete Failure.", icon: Ext.Msg.ERROR,
                            	buttons: Ext.Msg.YES});
                  				 
     				         }
                            
                        });
    		        	
    		            selection = null;
    		        }  
    		    }
    		});
        }
    },
    editPosition :  function(value,m,rec){
    	var main = this;
    		 
		 	var id = Ext.id();
		 	
		 	Ext.defer(function () {
	            Ext.widget('button', {
	                renderTo: id,
	                text: "Edit Position" ,// + r.get('name'),
	               // width: 75,
	                handler: function () {
	                	
	                	main.winAddPosition.show();
	        		 	main.winAddPosition.loadDataRecord(rec); 
	                	 
	                }
	            });
	        }, 50);
    	 
        return Ext.String.format('<div id="{0}"></div>', id);
    },
    addPostDate : function (value,m,rec){
    	var main = this;
		 
	 	var id = Ext.id();
	 	
	 	Ext.defer(function () {
            Ext.widget('button', {
                renderTo: id,
                text: "Add Post Date" ,// + r.get('name'),
               // width: 75,
                handler: function () {
                	
                	main.winPostDate.show();
        		 	main.winPostDate.loadDataRecord(rec); 
                	 
                }
            });
        }, 50);
	 
    return Ext.String.format('<div id="{0}"></div>', id);
    }
    
});   