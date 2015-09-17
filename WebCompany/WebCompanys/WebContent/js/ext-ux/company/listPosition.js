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
	//extend : 'Ext.panel.Panel', 	 
	
	extend: 'Ext.grid.Panel',
	width : '95%',
	height :  '100%',	 
	frame: true,	
	title: 'Position', 
	bodyPadding: 10,
	showClose : true,
	viewConfig: {
        emptyText: 'No images to display'
    },
    isCreate : true,
    parentForm : null,
    collapsible:false ,
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
    	       	       
    	    	    {header: 'position', dataIndex: 'position',width : '30%' , sortable: false }  ,
    	    	    {header: 'position number', dataIndex: 'position_no',width : '15%' , sortable: false }  ,
    	    	    {header: 'name of source', dataIndex: 'source',width : '15%' , sortable: false }  ,
    	    	    {header: 'post date', dataIndex: 'post_date',width : '10%',   sortable: false,renderer:Ext.util.Format.dateRenderer('d-m-Y') }  ,
    	    	   
    	            {
    	                xtype:'actioncolumn',
    	                
    	                width:'10%',
    	                items: [{
    	                	iconCls :'img-edit',
    	                	tooltip: 'Edit',
    	                	
    	                    handler: function(grid, rowIndex, colIndex) {
    	                        var rec = grid.getStore().getAt(rowIndex);
    	                         
    	                         
    	                        main.winAddPosition.show();
    	           			 	main.winAddPosition.loadDataRecord(rec);
    	                    }
    	                } ]
    	            }
    	    	    /*,
    	    	    {
    	                xtype:'actioncolumn',
    	                
    	                width:'10%',
    	                items: [{
    	                   
    	                	iconCls :'img-delete',
    	                	tooltip: 'Delete',
    	                    handler: function(grid, rowIndex, colIndex) {
    	                        var record = grid.getStore().getAt(rowIndex);
    	                         
    	                        var datajson = Ext.encode(record.data);
    		                    
    		                    //console.log(record);
    		                    Ext.Msg.show({
    		    				    title: 'confirm delete',
    		    				    message: 'Do you want to Delete position : ' + record.data.position+ ' ?',
    		    				    buttons: Ext.Msg.YESNO,
    		    				    icon: Ext.Msg.QUESTION,
    		    				    fn: function(btn) {
    		    				        if (btn === 'yes') {
    		    				        	 
    		    				        	Ext.Ajax.request({
    		    			              		url		: '/survey/deleteQuestion',
    		    			                	method  : 'POST',
    		    			                	jsonData: datajson,	
    		    			                	success: function(response, opts){
    		    			                		var resp = Ext.decode(response.responseText); 	
    		    			                		//console.log(resp);
    		    			                		if(resp.success){
    		    			                			grid.getStore().remove(record);
    		    			                			//main.resetData();
    		    			                		}
    		    			                		else{
    		    			                			Ext.Msg.alert('');
    		    			                		}
    		    			                			
    		    			                			 
    		    			                		},
    		    			                	failure: function(response, opts) {
    		    			                		console.log('server-side failure with status code ' );
    		    			                	}
    		    			                	
    		    				        	});
    		    				        	 
    		    				        	 
    		    				        }  
    		    				    }
    		    				}); 
    	                        
    	                    }
    	                } ]
    	            }*/
    	            
    	        ];
    	        
    	main.winAddPosition = Ext.create('company.winAddPosition',{
    		
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
    	this.callParent();
    	
    	this.getSelectionModel().on('selectionchange', this.onSelectChange, this);
    	
    },
    onSelectChange: function(selModel, selections){
        
       // this.fireEvent('showCompany', selections[0]);
    	//console.log(selections);
    	this.deletePosition.setDisabled(selections.length === 0);
		 
    },
    onDeleteClick: function(){
    	var selection = this.getView().getSelectionModel().getSelection()[0];
    	main = this;
        if (selection) {
        	Ext.Msg.show({
    		    title:'Confirm Delete?',
    		    message: 'Do you delete : ' + selection.get('position'),
    		    buttons: Ext.Msg.YESNO,
    		    icon: Ext.Msg.QUESTION,
    		    fn: function(btn) {
    		        if (btn === 'yes') {
    		        	
    		        	 
    		        	main.store.remove(selection);
    		        	main.store.sync();
    		          
    		            selection = null;
    		        }  
    		    }
    		});
        }
    	
    	
    	
    	
        
    }
    
});   