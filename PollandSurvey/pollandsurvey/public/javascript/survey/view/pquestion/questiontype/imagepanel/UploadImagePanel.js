 

Ext.define('survey.view.pquestion.questiontype.imagepanel.UploadImagePanel',{
	extend : 'Ext.panel.Panel',
	alias: ['widget.UploadImagePanel'],
	parentMain : null,
	store :survey.listBasicMediaData,
	width : '100%',
	height : '100%',
	accept: ['jpg', 'png', 'gif',  'bmp', 'tif'],  
	fileslist: [],   
	visiableColumns : [true,true,false,true,true],
	imageUrl : '',
	record :   new survey.model.listAnswerData({      		 
				value: 'answer',
				answer: 0,
				seq:  0  
				,id_question : Ext.id(),
	    		answer_image: ''
	}),
	hiddenImage : true,
	isReset: false,
	/* layout: {
	        type: 'hbox',
	        pack: 'start',
	        align: 'stretch'
	    },*/
	setLoadData : function(questionrecord) {
    	//console.log('survey.view.gui.questiontype.ImagePanel.UploadImagePanel'); 
    	 
    	
    	//entMain.remove(bt.parent);
    	
    }, 
initComponent: function() {
		
		var main = this; 
		 
		//main.addEvents('onChangeCheckAnswer' );
		
		main.labelupload = Ext.create('Ext.form.Label',{text : survey.label.none_image,margin: '5 0 0 5',hidden : !main.hiddenImage});
		main.imageFileUpload = main.wrappedImage = Ext.create('Ext.Img', {
	  		   //anchor: '15%' ,
			width : '15%',
			height: '15%',
	  		   src : main.imageUrl, 
	  		   //'/images/user_1/project_1/question_3/answer_1.png',
	  		//   flex:1,
	  		   hidden  : main.hiddenImage,
	  		  margin: '5 0 0 5' 
	  		}); 
		
		
		main.fileUpload = Ext.create('Ext.form.field.File',{
			flex:1,hideLabel :true,
			name : 'answer_image',
			fieldLabel: survey.label.image, 
			allowBlank: true ,
			buttonOnly: true,
			
			parent : main,
			 margin: '5 0 0 5' ,
			listeners: {
				scope: this,
	            'change': function(button, value){
	            	//debugger;
	            	//var parent = this.up('form');  
	            	//console.log(value);
	            	if (!button.parent.isReset) {
	            		var IsValid = button.parent.fileValidiation(button,value);
	            		 
		            	if (!IsValid) { 
		            		button.parent.isReset = true;
		            		button.parent.imageFileUpload.setSrc('');
		            		button.reset( );
		            		return; } 
		            	
		            	button.parent.isReset = false;
		            	
		            	//button.parent.imageFileUpload.setSrc('/images/user_1/project_1/question_3/answer_1.png');
		            	
		            	//button.parent.imageFileUpload.setSrc(value);
		            	button.parent.labelupload.setText(value);
		            	main.record.set('answer_image',value);
		            	 
		            	
	            	}else{
	            		button.parent.isReset = false;
	            	}
	                 
	            } 
	        }
			});
		
		main.score = Ext.create('Ext.form.field.Text',{
			name: 'score',
			 margin: '5 0 0 5' ,
			 hideLabel : true,
			 anchor: '100%',
			 hidden : !main.visiableColumns[2],
			 value : main.record.get('score')
		});
		main.checkbox = Ext.create('Ext.form.field.Checkbox',{
			name: 'answer',
			 margin: '5 0 0 5' ,
			 value : main.record.get('answer'),
			 hidden : !main.visiableColumns[3],
             listeners : {
            	 'change' :   
            		 function ( ch, newValue, oldValue, eOpts) {
            		 //console.log("set other answer is false");
            		  
            		 
            		 	if (oldValue == false)
            		 	{	
            		 		var len = main.store.data.length;
            		 		//console.log(len);
            		 		var len = main.store.data.length;
            		 		
            		 		
            		 		main.store.each(function(record){ 	   
            		 			if(main.record == record){
            		 				record.beginEdit();
                    		 		record.set('answer', 1);
                    		 	    record.modified = false;
                    		 	    record.endEdit();
                    		 	    //console.log("set other answer is true");
            		 			}
            		 			else{
            		 				record.beginEdit();
                    		 		record.set('answer', 0);
                    		 	    record.modified = false;
                    		 	    record.endEdit();
                    		 	    //console.log("set other answer is false");
            		 			}
                		 		
                		 	});
            		 		
            		 		
            		 		main.fireEvent('onChangeCheckAnswer',ch, newValue, oldValue, eOpts);  
            		 	}
            		 
            		  	/*main.store.each(function(record){ 	        	            		 		 
            		 		record.beginEdit();
            		 		record.set('answer', false);
            		 	    record.modified = false;
            		 	    record.endEdit();
            		 	    console.log("set other answer is false");
            		 	});*/
            			//debugger; 
            		  //	main.store.getAt(rowIndex).set('answer', true);
            		  
            		 }
             }
		});
		
		main.deletebt = Ext.create('Ext.Button',{
			name : 'delete_image',
			text : survey.label.delete,
			iconCls: 'icon-delete',
			parent : main,
            scope: this,
            margin: '5 0 0 5',
          //  flex:1,
            handler: this.onDeleteClick});
		
		/*main.headImage 
		main.headUpload  
		main.headAnswer  
		main.headDelete */
		
		main.panelColumn = Ext.create('Ext.panel.Panel',{
			layout : 'column',
			
			items : [
			   {
				   columnWidth: 0.3,
				   items : [main.labelupload,main.imageFileUpload ]
			   } ,
			   {
				   columnWidth: 0.2,
				   layout: {
				        type: 'vbox',
				        align : 'middle'
				    },
				   items : [main.fileUpload]
			   } ,
			   {
				   columnWidth: 0.15,
				   layout: 'fit',
				   
				   items : [main.score]
			   },
			   {
				   columnWidth: 0.15,
				   layout: {
				        type: 'vbox',
				        align : 'middle'
				    },
				   items : [main.checkbox]
			   } ,
			   {
				   columnWidth: 0.2,frame : false,
				   layout: {
				        type: 'vbox',
				        align : 'middle'
				    },
				   items : [main.deletebt]
			   } 
			]
		});
		
		
		
		main.items = [main.panelColumn];
		
		//main.items = [main.labelupload,main.imageFileUpload,main.fileUpload,main.checkbox,main.deletebt];
		this.callParent();
	},
	onDeleteClick : function(bt,ev){
		//console.log('onDeleteClick');
		main = this;
		Ext.Msg.show({
		    title:survey.message.confirm_delete,
		    message: survey.message.confirm_delete  ,
		    buttons: Ext.Msg.YESNO,
		    icon: Ext.Msg.QUESTION,
		    fn: function(btn) {
		        if (btn === 'yes') {
		        	
		        	//console.log(bt.parent.record.get('id_basic_data'));
		        	
		        	
		        	 
		        	Ext.Ajax.request({
	              		url		: '/survey/deleteQuestionData',
	              		method: 'POST',
	                    headers: { 'Content-Type': 'application/json' },
	                    params : Ext.JSON.encode( {'id' : bt.parent.record.get('id_basic_data') } ),
	                	success: function(response, opts){
	                		var resp = Ext.decode(response.responseText); 	
	                		//console.log(resp);
	                		if(resp.success){
	                			bt.parent.fireEvent('removePanelAnswer',bt.parent);
	                			bt.parent.parentMain.remove(bt.parent);
	                		}
	                		else{
	                			Ext.Msg.alert( survey.message.failed , resp.message);
	                		}
	                		resp = null;	
	                			 
	                		},
	                	failure: function(response, opts) {
	                		console.log('server-side failure with status code ' );
	                	}
	                	
		        	});
		        	 
		        	 
		        }  
		    }
		});
		 
		
	},
	fileValidiation: function(view, filename){
		 
		var isValid = true;  
	     var indexofPeriod = view.getValue().lastIndexOf("."),  
	            uploadedExtension = view.getValue().substr(indexofPeriod + 1, view.getValue().length - indexofPeriod); 
	     
	 
	     
	     if (!Ext.Array.contains(this.accept, uploadedExtension.toLowerCase())) {  
	         isValid = false;  
	         // Add the tooltip below to   
	         // the red exclamation point on the form field  
	         var erroMsg = Ext.String.format(survey.message.error_upload_without_extention, this.accept.join());  
	         //me.setActiveError(erroMsg);
	         //console.log(erroMsg);
	         // Let the user know why the field is red and blank!  
	         var messageBox = Ext.MessageBox.show({  
	           title: survey.message.upload,  
	           msg: erroMsg,  
	           buttons: Ext.Msg.OK,  
	           icon: Ext.Msg.WARNING  
	         });       
	         //view.setRawValue(null);  
	         //view.reset();  
	       }  
	       for (var i = 0; i < this.fileslist.length; i++) {  
	         if (this.fileslist[i].indexOf(filename) !== -1) {  
	           isValid = false;  
	           var erMsg = Ext.String.format(survey.message.upload_success, filename);  
	           //console.log(erroMsg);
	           var messageBox = Ext.MessageBox.show({  
	             title: survey.message.upload,  
	             msg: erMsg,  
	             buttons: Ext.Msg.OK,  
	             icon: Ext.Msg.INFO  
	           });  
	           view.setRawValue(null);  
	           view.reset();  
	           break;  
	         }  
	       }    
	       return isValid;  
	}
 
});

   