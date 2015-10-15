
Ext.define('survey.view.pemailtemplate.ListEmailTemplate',{
	extend : 'Ext.grid.Panel',
	alias: ['widget.ListEmailTemplate'],
     
	anchor: '100%',
	//width : '100%',
	//height :  '100%',
	//height :  '400',
	bufferedRenderer: false,
	disableSelection : true,
	forceFit: true,
	
	viewConfig: {
        emptyText: 'No images to display'
    },
    collapsible:false ,
    getHeaderColumn : function(){
    	var main = this;
    	return [
				{header: survey.label.name_content  , dataIndex: 'name_content',width : '25%' , sortable: false }  ,
				{header: survey.label.start_date , dataIndex: 'create_date',width : '20%' , sortable: false }  ,
				{header: survey.label.update_date , dataIndex: 'update_date',width : '20%' , sortable: false }  ,
				 
				{header: survey.label.delete  ,  width : '10%',  renderer :main.deletebuttonManage,  sortable: false  } ,
				{header: survey.label.edit ,  width : '10%',  renderer :main.showbuttonManage,  sortable: false  }   
	        ]
    },
    initComponent: function() {
    	 
    	var main = this;
    	//main.store = Ext.create('survey.listInvitationData'); 
    	main.columns = main.getHeaderColumn();
      
    	main.dockedItems = main.getPagingToolsBar(); 
    	
    	main.callParent();
    	
    	 
     
    } ,
    listeners: {
        'selectionchange': function(view, records) {
        	 
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
	                    
	                    Ext.Msg.show({
	    				    title: survey.message.confirm_delete ,
	    				    message: survey.message.confirm_delete  + r.data.name_content,
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
	    			                 
	    			                		
	    			                		if(resp.result){
	    			                			
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
    showbuttonManage : function (value,m,r){
    	var main = this;
    	var id = Ext.id();
        Ext.defer(function () {
            Ext.widget('button', {
                renderTo: id,
                text: survey.label.edit ,// + r.get('name'),
              //  width: 75,
                handler: function () {
                	//Ext.Msg.alert('Info', r.get('name'));  
                	//main.showManage(r);
                	 
                	main.fireEvent('showManageOption', this, r);
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
            displayInfo: true,
            listeners : {
            	scope: main,
            	'beforechange' : main.onBeforeChange,
            }
        }]
    },
    onBeforeChange : function(paging,page,opt){
    	var main = this;
    	main.fireEvent('changeDataValue', paging,page); 
		return false;
	}
});

   