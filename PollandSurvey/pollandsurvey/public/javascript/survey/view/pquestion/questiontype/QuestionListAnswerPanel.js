 

Ext.define('survey.view.pquestion.questiontype.QuestionListAnswerPanel',{
	extend : 'Ext.grid.Panel',
	alias: ['widget.QuestionListAnswerPanel'],
	store : survey.listBasicData,
	width : '100%',
	height : '100%',
	defaults: {
        anchor: '100%'
        //,labelWidth: 120
    },
    rowAt : 0,
	frame: false,
	forceFit: true,
	frame: true,
	record: null,
	collapsible:false ,
	selType: 'cellmodel',
	viewConfig: {
        emptyText: 'No images to display'
    },
    requires: [
               'Ext.grid.plugin.CellEditing',
               'Ext.form.field.Text',
               'Ext.toolbar.TextItem'
           ],
    
    setLoadData : function(questionrecord) {
    	//console.log('survey.view.list.GridAnswer'); 
    	survey.listBasicData.removeAll();
    	this.getStore().removeAll();
    	 
    	//console.log('survey.listBasicData.data.length : ' + survey.listBasicData.data.length );
    	this.record = questionrecord;
    	
    	//this.getStore().data = Ext.create("Ext.util.Collection");
    	 
    	 
    	if(questionrecord != null){
	    
    		survey.listBasicData.load({
	    		params : {
	    			questionid : questionrecord.id
	    		},
	    		scope : this
	    	});
	    	
    	}
    	//debugger;
    },
    initComponent: function() {
    	
    	
    	 
    	
    	
    	var main = this;
    	main.editing = Ext.create('Ext.grid.plugin.CellEditing',{clicksToMoveEditor: 1});    	
    	main.plugins =  [main.editing];
    	var row = 1;
    	main.columns = [
    	                	{xtype: 'rownumberer'},
    	                	{header: 'id', width : '9%', sortable: false, dataIndex: 'id_question' ,hidden : true,menuDisabled: true},
    	    	   //	{header: 'No.', width : '9%', sortable: false, dataIndex: 'seq',menuDisabled: true},
    	                	{header: 'Choose', dataIndex: 'value', 
		    	    	   		field : {
		    	    	   			type : 'textfield'
		    	    	   		},
		    	    	   		//editor: 'textfield',  
		    	    	   		width : '70%',   sortable: false,menuDisabled: true}  , 
    	          
		    	    	   	{
		        	            xtype: 'checkcolumn',
		        	            header: survey.label.answer,
		        	            dataIndex: 'answer',
		        	            width: '20%',
		        	           
		        	            sortable: false,
		        	           
		        	             sortable: false ,
		        	             handler : function(){
		        	            	 //console.log("click");
		        	             },
		        	             listeners : {
		        	            	 checkChange :  
		        	            		 function ( ch, rowIndex, checked, eOpts) {
		        	            		 	 
		        	            		 	
		        	            		 	survey.listBasicData.each(function(record){ 
		        	            		 		 
		        	            		 		record.beginEdit();
		        	            		 		record.set('answer', 0);
		        	            		 	    //record.modified = false;
		        	            		 	    record.endEdit();
		        	            		 	});
		        	            		 	
		        	            		 	survey.listBasicData.getAt(rowIndex).set('answer', 1);
		  
		        	            		 }
		        	            	  
		        	            	 
		        	             }
		    	    	   }   
    	            
    	        ];
    	
    	main.dockedItems = [{
            xtype: 'toolbar',
            items: [{
                iconCls: 'icon-add',
                text: survey.label.add,
                scope: this,
                parent : main,
                handler: this.onAddClick
            }, {
            	itemId: 'removeAnswer',
                iconCls: 'icon-delete',
                text: survey.label.delete,
                //disabled: true,
                parent : main,
                scope: this,
                handler: this.onDeleteClick
            }]
        }]  	
  
    	 
    	this.callParent(arguments);    	
    	//this.getSelectionModel().on('selectionchange', this.onSelectChange, this);
    } ,
    
    listeners: {
    	'click' : function(){
    		//alert('test');
    	},
        'selectionchange': function(view, records) {
        	//alert('test');
        	//this.down('#removeAnswer').setDisabled(!records.length);
        }
    },
    onAddClick : function(bt,ev){
    	
    	bt.parent.id_question = 0;
    	if(bt.parent.record != null){
    		bt.parent.id_question = bt.parent.record;
    	}
    	 
    	this.store.add(new Survey.model.listAnswerData( {
    		value: '',
    		answer : 0,
    		seq: (this.store.data.length +1),
    		id_question : bt.parent.id_question,
    		answer_image: ''
    	} ));
    	
    	this.editing.cancelEdit(); 
    	 
    	this.editing.startEditByPosition({
            row: this.store.data.length -1 ,
            column: 1
        });
        
    },
    onDeleteClick : function(bt,ev){
    	
    	//console.log('delete from cell');
    	 
    	Ext.Msg.show({
		    title: survey.message.confirm_delete,
		    message: survey.message.confirm_delete  ,
		    buttons: Ext.Msg.YESNO,
		    icon: Ext.Msg.QUESTION,
		    fn: function(btn) {
		        if (btn === 'yes') {
		        	
		        	var recordSelected = bt.parent.getView().getSelectionModel().getSelection()[0];
		        	if (recordSelected){
			        	//console.log(recordSelected.get('id_basic_data'));
			        	Ext.Ajax.request({
		              		url		: '/survey/deleteQuestionData',
		              		method: 'POST',
		                    headers: { 'Content-Type': 'application/json' },
		                    params : Ext.JSON.encode( {'id' : recordSelected.get('id_basic_data') } ),
		                	success: function(response, opts){
		                		var resp = Ext.decode(response.responseText); 	
		                		//console.log(resp);
		                		if(resp.success){
		                			bt.parent.store.remove(recordSelected);
		                		}
		                		else{
		                			Ext.Msg.alert(survey.message.failed, resp.message);
		                		}
		                		resp = null;	
		                			 
		                		},
		                	failure: function(response, opts) {
		                		//console.log('server-side failure with status code ' );
		                	}
		                	
			        	});
		        	}
		        	 
		        	 
		        }  
		    }
		});
    	 
        
    }
 
});

   