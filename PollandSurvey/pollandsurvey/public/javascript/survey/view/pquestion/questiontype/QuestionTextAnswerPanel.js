 

Ext.define('survey.view.pquestion.questiontype.QuestionTextAnswerPanel',{
	//extend : 'Ext.grid.Panel',
	extend : 'Ext.panel.Panel',
	alias: ['widget.QuestionTextAnswerPanel'],
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
	
	viewConfig: {
        emptyText: 'No images to display'
    },
     
    setLoadData : function(projectrecord,questionrecord) {
    	
    	console.log("QuestionTextAnswerPanel setLoad Data");
    	/**set show header*/
		console.log(projectrecord);
		console.log(questionrecord); 
		this.record = projectrecord;
		
		if(questionrecord == null){
			//create new question
			this.store.add(new survey.model.listAnswerData( {
	    		value: '',
	    		answer : 1,
	    		seq: (this.store.data.length +1),
	    		id_question : this.record.id,// bt.parent.id_question,
	    		answer_image: ''
	    	} ));
		}
    	
	 
    	 console.log(this.store);
		//debugger;
    },
    initComponent: function() {
    	var main = this;
    	
    	/* 
    	main.editing = Ext.create('Ext.grid.plugin.CellEditing',{clicksToMoveEditor: 1});    	
    	main.plugins =  [main.editing];
    	var row = 1;
    	main.columns = [
    	                	{xtype: 'rownumberer'},
    	                	{header: 'id', width : '9%', sortable: false, dataIndex: 'id_question' ,hidden : true,menuDisabled: true},
    	                	{header: 'Choose', dataIndex: 'value', 
		    	    	   		field : { type : 'textfield' },
		    	    	   		//editor: 'textfield',  
		    	    	   		width : '60%',   sortable: false,menuDisabled: true}  , 
		    	    	   	{header: 'Score', width : '10%', 
		    	    	   			//id: 'score_column',
		    	    	   			sortable: false, dataIndex: 'score',menuDisabled: true,
		    	    	   			field : { type : 'textfield' }},	
		    	    	   	{
		        	            xtype: 'checkcolumn',
		        	            header: survey.label.answer,
		        	            dataIndex: 'answer',
		        	            width: '20%',
		        	             //id: 'answer_column',
		        	            // hidden : true,
		        	           
		        	             sortable: false ,
		        	             handler : function(){
		        	            	  
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
		        	            		 	//survey.listBasicData.getAt(rowIndex).set('score', 1);
		  
		        	            		 }
		        	            	  
		        	            	 
		        	             }
		    	    	   }   
    	            
    	        ];
     */
    	this.callParent(arguments);    	
    	//this.getSelectionModel().on('selectionchange', this.onSelectChange, this);
    } 
       
 
});

   