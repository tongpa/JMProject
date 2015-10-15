 

Ext.define('survey.view.pquestion.questiontype.QuestionImageAnswerPanel',{
	extend : 'Ext.panel.Panel',
	alias: ['widget.QuestionImageAnswerPanel'],
	
	requires: [
               'survey.view.pquestion.questiontype.imagepanel.UploadImagePanel' 
               
    ],
    visiableColumns : [true,true,false,true,true],
	store :survey.listBasicMediaData,
	width : '100%',
	height : '100%',
	defaults: {
        anchor: '100%'
        //,labelWidth: 120
    },
    idFileUploads : [],
    rowAt : 0,
	frame: false,
	setVisiableColumns : function (visiableColumns){
		
		/*this.headScore.setVisible(!visiableColumns[2]);
		this.headAnswer.setVisible(!visiableColumns[3]) ;
		
		Ext.getCmp( 'column_layout_score' ).setVisible(!visiableColumns[2]);
		Ext.getCmp( 'column_layout_answer' ).setVisible(!visiableColumns[3]);
		*/
		this.visiableColumns = visiableColumns;
		
		//this.addHeader(this);
		
	},
	setLoadData : function(projectrecord,questionrecord) {
    	
		/**set show header*/
		if(projectrecord.data.id_question_project_type == 3){  //test and exam
			this.visiableColumns = [true,true,true,true,true] ; 
	   	}else
	   	{	this.visiableColumns = [true,true,true,false,true] ; 
	   		 
	    
	   	}
		
		
    	this.record = questionrecord;
    	//debugger;
    	this.haveData = false;
    	
    	for(var i = (this.items.length-1 ) ; i >=0; i--){
    		this.remove(this.items.getAt(i));
    	}
    	
    	this.addHeader(this);
    	this.rowAt =0;
    
    	if(questionrecord != null){
    		
    	 
    		
    		survey.listBasicMediaData.load({
	    		params : {
	    			questionid : questionrecord.id
	    		},
	    		scope : this,
	    		callback: function(records, operation, success){
	    			 
	    			if(success){
	    				 
	    				this.haveData = records.length > 0;
	    				 
	    				for(var i = 0; i < records.length; i++){

	    					var imageUrl = '/images/getSubImage?id=' + records[i].data.id_basic_data;
	    					
	    					this.addFileUpload(this,imageUrl,records[i]);
	    				}
	    				 
	    			}
	    			
	    			 
	    	    	
	    	    	if (!this.haveData){
	    	    		 
	    	    		//this.addFileUpload(this);
	    	    	}
	    			
	    			
	    		}
	    	});
    		
    		
    	} 
    	 
    	//this.fileUpload.setLoadData(questionrecord);
    },
	addHeader : function(parent){
		 
		parent.headImage = Ext.create('Ext.form.Label',{text: survey.label.image ,margin: '5 0 0 5' });
		parent.headUpload = Ext.create('Ext.form.Label',{text: survey.label.upload  ,margin: '5 0 0 5' });
		parent.headScore = Ext.create('Ext.form.Label',{text: survey.label.score  ,margin: '5 0 0 5', hidden : !this.visiableColumns[2] });
		parent.headAnswer = Ext.create('Ext.form.Label',{text: survey.label.answer  ,margin: '5 0 0 5', hidden : !this.visiableColumns[3] });
		parent.headDelete = Ext.create('Ext.form.Label',{text: survey.label.delete  ,margin: '5 0 0 5' });
		var panelColumn = Ext.create('Ext.panel.Panel',{
			layout : 'column',
			
			items : [
			   {
				   columnWidth: 0.3,frame : true,
				   items : [parent.headImage ]
			   } ,
			   {
				   columnWidth: 0.2,frame : true,
				   items : [parent.headUpload]
			   },
			   {   id : 'column_layout_score',
				   columnWidth: 0.15,frame : true,hidden : !this.visiableColumns[2],
				   items : [parent.headScore]
			   } ,
			   {   id : 'column_layout_answer',	
				   columnWidth: 0.15,frame : true,hidden : !this.visiableColumns[3],
				   items : [parent.headAnswer]
			   } ,
			   {
				   columnWidth: 0.2,frame : true,
				   items : [parent.headDelete]
			   } 
			]
		});
		parent.add(panelColumn);
	}  ,
	initComponent: function() {
    	
    	var main = this;
    
    	
    	main.dockedItems = [{
            xtype: 'toolbar',
            items: [{
                iconCls: 'icon-add',
                text:survey.label.add,
                scope: this,
                parent : main,
                handler: this.onAddClick
            } ]
        }]  
    	
    	this.callParent();
    	
	},
    onAddClick : function(bt,ev){
    	
    	bt.parent.id_question = 0;
    	if(bt.parent.record != null){
    		bt.parent.id_question = bt.parent.record.get('id_question');
    		 
    	}
    	bt.parent.addFileUpload(bt.parent,null,null);
    	
        
    },
    addFileUpload : function(parent,urlImage,listAnswerData){
    	 
    	Survey.model.listAnswerData
    	parent.rowAt = parent.rowAt +1;
    	var r = new survey.model.listAnswerData({      		 
    		value: 'answer',
    		answer: 0,
    		seq:   parent.rowAt  
    		,id_question : parent.id_question ,
    		answer_image: ''
    	});    	 
    	
    	//rows = survey.listBasicMediaData.insert(survey.listBasicMediaData.data.length, r);
     
    	var id_FileUpload = Ext.id();
    	var urlImage = '';
    	if (listAnswerData != null) {
    		urlImage =  '/images/getSubImage?id=' + listAnswerData.get('id_basic_data');
    		r = listAnswerData;
    		
    		//rows = this.store.insert(this.store.data.length, r);
    		
    		/*r.set('answer',listAnswerData.answer == 1);
    		r.set('seq',listAnswerData.seq)
    		r.set('id_basic_data',)
    		*/
    	}else
    	{
    		rows = this.store.insert(this.store.data.length, r);
    	}
    	
    	var fileUpload = Ext.create('survey.view.pquestion.questiontype.imagepanel.UploadImagePanel',{
    		id : id_FileUpload,
    		parentMain : parent,
    		store:parent.store,
    		record: r,
    		visiableColumns : parent.visiableColumns,
    		imageUrl : urlImage,
    		hiddenImage : listAnswerData == null ,
    		listeners : {
           	 	'onChangeCheckAnswer' : parent.checkAnswerOnlyOne  ,
           	 	'removePanelAnswer' : parent.removePanelAnswer
    		}
    	}); 
    	
    	this.idFileUploads.push(id_FileUpload);
    	parent.add(fileUpload);
    	 
    },
    checkAnswerOnlyOne : function(ch, newValue, oldValue, eOpts){
    	 
    	
    	for(var i=0; i < this.parentMain.idFileUploads.length ;i++){
    		var fileUploadPanel  = Ext.getCmp(this.parentMain.idFileUploads[i]);
    		 
    		if ( fileUploadPanel != null && fileUploadPanel.getId() != this.getId()){
    			 
    			fileUploadPanel.checkbox.setValue(false);
    		} 
    		fileUploadPanel = null;
    		 
    	}
    	//debugger;
    },
    removePanelAnswer: function(fileUpload){
   
    
    	for(var i=0; i < this.parentMain.idFileUploads.length ;i++){
    		var fileUploadPanel  = Ext.getCmp(this.parentMain.idFileUploads[i]);
    	 	if ( fileUploadPanel != null && fileUploadPanel.getId() == fileUpload.getId()){
    			 this.parentMain.idFileUploads.splice(i, 1);
    			 fileUploadPanel = null;
    			 break;
    		} 
    		fileUploadPanel = null;
    	}
    	 
    }
 
});

   