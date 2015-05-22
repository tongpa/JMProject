
Ext.define('survey.view.pproject.ListProject',{
	extend : 'Ext.grid.Panel',
	alias: ['widget.ListProject'],
     
	anchor: '100%',
	//width : '100%',
	//height :  '100%',
	//height :  '400',
	bufferedRenderer: false,
	disableSelection : true,
	forceFit: true,
	store: survey.listProject,
	viewConfig: {
        emptyText: 'No images to display',
        forceFit: true ,
        listeners : {
        	refresh : function(dataview){
        		Ext.each(dataview.panel.columns, function (column) {
        		       if (column.autoSizeColumn === true)
        		        column.autoSize();
        		      })
        	}
        }
    },
    collapsible:false ,
    getHeaderColumn : function(){
    	var main = this;
    	return [
	       	       
	    	//    {header: survey.label.name, dataIndex: 'name' ,autoSizeColumn : true ,width : '15%', sortable: false }  ,
	    	    {header: survey.label.name, dataIndex: 'name' , width : '15%', sortable: false }  ,
	    	    {header: survey.label.project_type, dataIndex: 'question_project_type',width : '15%', renderer :main.showprojecttype , sortable: false }  ,
	    	    {header: survey.label.start_date , dataIndex: 'start_date',width : '15%' ,renderer :main.convertDate, sortable: false }   ,
	    	    {header: survey.label.delete,  width : '10%', renderer :main.deleteButton, sortable: false  } ,
	    	    {header: survey.label.edit,  width : '10%',  renderer :main.showbuttonManage,  sortable: false  }       	    	     
	            
	        ] ;
    },
    initComponent: function() {
    	 
    	var main = this;
    	 
    	main.columns = main.getHeaderColumn();
      
    	main.dockedItems = main.getPagingToolsBar(); 
    	
    	
    	
    	main.showWin =  Ext.create('survey.view.pproject.WinProjectView',{
    		url : '/survey/saveProject',
    		//height : 500,
			listeners : {
				refreshOther : function(cmp) {
					survey.listProject.reload();
		        }
			}
    	} ) ;
    	 
    	main.addProject = Ext.create('Ext.Button',{
    		parent : main,
    		text : survey.label.add_project,
    		iconCls : 'project-add',
    		handler: function () { 
    			 
    			 
    			this.parent.showWin.show(this);
    			this.parent.showWin.resetData();
    		}
    	} );
    	
    	//main.showWin.targetFrom = main.addProject;
    	main.tbar = [main.addProject ] ;
    	
    	
    	
    	main.callParent();
    	
    	 
     
    },
    showprojecttype : function (value, m, r){
    	 
    	return value.description;
    },
    convertDate : function(value,m,r){
    	 
    	return Ext.Date.format(Ext.Date.parse(value, 'Y-m-d G:i:s'), 'd/m/Y G:i')
    },
    showbuttonManage : function (value,m,r){
    	var main = this;
    	var id = Ext.id();
        Ext.defer(function () {
            Ext.widget('button', {
                renderTo: id,
                text: survey.label.edit,// + r.get('name'),
                autoWidth : true,
             //   width: 75,
                handler: function () {
                	//Ext.Msg.alert('Info', r.get('name'));  
                	main.showManage(r);
                }
            });
        }, 50);
        return Ext.String.format('<div id="{0}"></div>', id);
   
    } ,
    deleteButton : function(value,m,r){
    	var main = this;
    	var id = Ext.id();
    	 
    	 
        Ext.defer(function () {
            Ext.widget('button', {
                renderTo: id,
                iconCls : 'project-remove',
                text: survey.label.delete,// + r.get('name'),
               // width: 75,
                record : r,
                
                handler: function (bt,ev) { 
                	//debugger;
                	 
                	main.removeProject(r);
                	 
                	
                }
            });
        }, 50);
        return Ext.String.format('<div id="{0}"></div>', id);
    },
     
    showManage : function( record ) {
        //do some stuff here

        this.fireEvent('showManage', this,record);
    },
    removeProject : function(record){
    	 
    	
    	var main= this;
    	//survey.listProject.remove(r);
    	var datajson =  Ext.encode(record.data);
    	
    	console.log(datajson);
    	
    	Ext.Msg.show({
		    title: survey.message.confirm_delete,
		    message: survey.message.confirm_delete + record.data.name,
		    buttons: Ext.Msg.YESNO,
		    icon: Ext.Msg.QUESTION,
		    fn: function(btn) {
		        if (btn === 'yes') {
		        	 
		        	Ext.Ajax.request({
	              		url		: '/survey/deleteProject',
	                	method  : 'POST',
	                	jsonData: datajson,	
	                	success: function(response){
	                	    	
	                		main.getStore().remove(record);
	                		 
	                			
	                			 
	                		}
	                	});
		        	 
		        	 
		        }  
		    }
		});
    	
    	
    } ,
    listeners: {
        'selectionchange': function(view, records) {
        	console.log('selectionchange');
        	grid.down('#removeEmployee').setDisabled(!records.length);
          //  grid.down('#removeEmployee').setDisabled(!records.length);
        }
    } ,
    deletebuttonManage : function(value,m,r){
    	var main = this;
    	var id = Ext.id();
    	Ext.defer(function () {
            Ext.widget('button', {
                renderTo: id,
                iconCls : 'project-remove',
                text: survey.label.delete    ,// + r.get('name'),
              //  width: 75,
                handler: function () {
                	    
                	  
                		var datajson = Ext.encode(r.data);
	                    //console.log(record);
	                    Ext.Msg.show({
	    				    title: survey.message.confirm_delete ,
	    				    message: survey.message.confirm_delete  + r.data.name_publication,
	    				    buttons: Ext.Msg.YESNO,
	    				    icon: Ext.Msg.QUESTION,
	    				    fn: function(btn) {
	    				        if (btn === 'yes') {
	    				         
	    				        	 
	    				        	Ext.Ajax.request({
	    			              		url		: '/survey/deleteInvitation',
	    			                	method  : 'POST',
	    			                	jsonData: datajson,	
	    			                	success: function(response, opts){
	    			                		var resp = Ext.decode(response.responseText); 	
	    			                		//console.log(resp);
	    			                		if(resp.success){
	    			                			
	    			                			main.getStore().remove(r);
	    			                			
	    			                		}
	    			                		else{
	    			                			Ext.Msg.alert(survey.message.failed, resp.message);
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
            });
        }, 50);
        return Ext.String.format('<div id="{0}"></div>', id);
    },
     
    refreshOther : function(){
		this.fireEvent('refreshOther', this);
		
	},
    getPagingToolsBar : function(){
    	var main = this;
    	return [{
            xtype: 'pagingtoolbar',
            store: main.store, // same store GridPanel is using
            dock: 'bottom',
            displayInfo: true
        }]
    }
});

   