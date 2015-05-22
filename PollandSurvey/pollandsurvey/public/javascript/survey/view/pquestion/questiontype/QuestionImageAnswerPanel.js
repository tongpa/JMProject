 

Ext.define('survey.view.pquestion.questiontype.QuestionImageAnswerPanel',{
	extend : 'Ext.panel.Panel',
	alias: ['widget.QuestionImageAnswerPanel'],
	
	requires: [
               'survey.view.pquestion.questiontype.imagepanel.UploadImagePanel' 
               
    ],
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
	setLoadData : function(questionrecord) {
    	//console.log('survey.view.gui.questiontype.ImagePanel'); 
    	//survey.listBasicData.removeAll();
    	this.record = questionrecord;
    	//debugger;
    	this.haveData = false;
    	
    	for(var i = (this.items.length-1 ) ; i >=0; i--){
    		this.remove(this.items.getAt(i));
    	}
    	
    	this.addHeader(this);
    	this.rowAt =0;
    	//console.log('start rowAt : ' + this.rowAt); 
    	if(questionrecord != null){
    		
    		//console.log('lenght : ' + survey.listBasicMediaData.data.length);
    		
    		survey.listBasicMediaData.load({
	    		params : {
	    			questionid : questionrecord.id
	    		},
	    		scope : this,
	    		callback: function(records, operation, success){
	    			 
	    			if(success){
	    				 
	    				this.haveData = records.length > 0;
	    				//console.log(' records.length '  +  records.length); 
	    				//console.log('have Data '  + (this.haveData)); 
	    				for(var i = 0; i < records.length; i++){

	    					var imageUrl = '/images/getSubImage?id=' + records[i].data.id_basic_data;
	    					
	    					this.addFileUpload(this,imageUrl,records[i]);
	    				}
	    				//console.log('lenght : ' + survey.listBasicMediaData.data.length);
	    			}
	    			
	    			//console.log('Add File Upload '  + (!this.haveData)); 
	    	    	
	    	    	if (!this.haveData){
	    	    		 //console.log('Add field upload');
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
		parent.headScore = Ext.create('Ext.form.Label',{text: survey.label.score  ,margin: '5 0 0 5' });
		parent.headAnswer = Ext.create('Ext.form.Label',{text: survey.label.answer  ,margin: '5 0 0 5' });
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
			   {
				   columnWidth: 0.15,frame : true,
				   items : [parent.headScore]
			   } ,
			   {
				   columnWidth: 0.15,frame : true,
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
    	//main.fileUpload = Ext.create('survey.view.gui.questiontype.ImagePanel.UploadImagePanel',{parentMain : main,store:main.store});
    	
    	
		
    	 
    	
    	//main.items = [ main.fileUpload ]; 
    	
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
    	//console.log('add data to listAnswerData') ;
    	Survey.model.listAnswerData
    	parent.rowAt = parent.rowAt +1;
    	var r = new Survey.model.listAnswerData({      		 
    		value: 'answer',
    		answer: 0,
    		seq:   parent.rowAt  
    		,id_question : parent.id_question ,
    		answer_image: ''
    	});    	 
    	
    	//rows = survey.listBasicMediaData.insert(survey.listBasicMediaData.data.length, r);
    	//console.log('rowAt : ' + parent.rowAt);
    	//console.log(r) ;
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
    	//console.log('removePanelAnswer');
    
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

   