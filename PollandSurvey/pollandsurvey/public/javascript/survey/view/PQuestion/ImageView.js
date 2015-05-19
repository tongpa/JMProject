 

Ext.define('survey.view.PQuestion.ImageView',{
	extend : 'Ext.form.Panel',
	alias: ['widget.ImageView'],
 
	record : null,
	accept: ['jpg', 'png', 'gif',  'bmp', 'tif'],  
	fileslist: [],  
	defaults: {
        anchor: '100%',
        labelWidth: 100
    }, 
    setLoadData : function( questionrecord, questiontyperecord ){
    	var form = this;
    	form.record = questionrecord;
    	form.wrappedImage.setHidden(true);
		form.labelShowFileUpload.setHidden(false); 
		form.labelShowFileUpload.setText(survey.label.none_image);
 
    	form.fileUpload.reset();
		form.wrappedImage.setSrc('');
		//console.log('load image');
		
		  
    	if(questionrecord != null  ){
    		//&& (questionrecord.data.question_type_name.toLowerCase().search("image") >=0 )
    		//console.log("setShow");
    		form.wrappedImage.setHidden(false);
    		form.wrappedImage.setSrc('/images/getImage?id=' + questionrecord.data.id_question);
    		
    		form.labelShowFileUpload.setHidden(true);
    	}
    	form = null;
    	 
    },
    initComponent: function() {
    	
    	var main = this;
    	main.labelFileUpload = Ext.create('Ext.form.Label',{ text :  survey.label.image  ,
    		margin: '5 0 0 5' ,
    		style : 'color: #666666; font-weight: normal; font-size: 13px', flex: 1 });
    	main.wrappedImage = Ext.create('Ext.Img', { anchor: '15%',margin: '5 0 0 5', title : '' , flex: 1});    	
    	main.labelShowFileUpload = Ext.create('Ext.form.Label',{text :  survey.label.image  ,
    		margin: '5 0 0 5' ,
    		style : 'color: #666666; font-weight: normal; font-size: 13px',text : survey.label.none_image , flex: 1 });    	
    	main.fileUpload = Ext.create('Ext.form.field.File',{name : 'image_upload',
    		fieldLabel: survey.label.image, 
    		buttonOnly: true,
    		hideLabel: true,
    		margin: '5 0 0 5' ,
    		msgTarget: 'side', flex: 2,
    		parent : main,
    		margins:'0',
    		listeners: {
				scope: this,
	            'change': function(button, value){
	            	//debugger;
	            	//console.log(value);
	            	if (!button.parent.isReset) {
	            		var IsValid = button.parent.fileValidiation(button,value);
	            		 
		            	if (!IsValid) { 
		            		button.parent.isReset = true;
		            		button.parent.wrappedImage.setSrc('');
		            		button.reset( );
		            		return; } 
		            	
		            	button.parent.isReset = false;
		            	button.parent.labelShowFileUpload.setHidden(false);
		            	button.parent.labelShowFileUpload.setText(value);
		            	
	            	}else{
	            		button.parent.isReset = false;
	            	}
	                 
	            } 
	        }
		});
    	
    	main.deleteFileUpload = Ext.create('Ext.Button',{
			parent : main,
            scope: this,
            margin: '5 0 0 5',
            flex:1,
            margins:'0',
            name : 'delete_image',
        	text : survey.label.delete,
        	iconCls: 'icon-delete',
            handler: this.onDeleteClick
           });
    	 
    	
    	//main.wrappedImage.setHidden(true);
    	//main.fileUpload.setHidden(true);
    	
    	
    	main.items = [
    	              {	
    	            	  layout: {
    	            	        type: 'hbox' 
    	            	        ,align:'middle'	
    	            	        ,pack:'start'
    	            	        //,align: 'stretch'
    	            	    },
    	            	    
    	            	    //defaults:{margins:'0 5 0 0'},
    	            	    items : [main.labelFileUpload ,main.wrappedImage,main.labelShowFileUpload,main.fileUpload,main.deleteFileUpload ]
    	              }
    	              
    	              ];
    	this.callParent();
    },
	onDeleteClick : function(bt,ev){
		//console.log('onDeleteClick');
		var form = this;
		
		//debugger;
		

		Ext.Ajax.request({
		   url: '/survey/deleteMediaQuestion',
		   method: 'POST',
           headers: { 'Content-Type': 'application/json' },
           params : Ext.JSON.encode( {'id' : this.record.get('id_question')} ),
		   success: function(response, opts) {
		      var obj = Ext.decode(response.responseText);
		      //console.log(obj);
		   },
		   failure: function(response, opts) {
		      console.log('server-side failure with status code ' + response.status);
		   }
		});
		
		form.wrappedImage.setHidden(true);
		form.wrappedImage.setSrc('');
		
		form.labelShowFileUpload.setHidden(false); 
		form.labelShowFileUpload.setText(survey.label.none_image);
		
		form.fileUpload.reset();
		
		
		
	},
	fileValidiation: function(view, filename){
		 
		var isValid = true;  
	     var indexofPeriod = view.getValue().lastIndexOf("."),  
	            uploadedExtension = view.getValue().substr(indexofPeriod + 1, view.getValue().length - indexofPeriod); 
	     
	 
	     
	     if (!Ext.Array.contains(this.accept, uploadedExtension.toLowerCase())) {  
	         isValid = false;  
	         // Add the tooltip below to   
	         // the red exclamation point on the form field  
	         
	         //var erroMsg = Ext.String.format('Please upload files with an extension of {0} only!', this.accept.join());
	         var erroMsg = Ext.String.format(survey.message.error_upload_without_extention , this.accept.join()); 
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

   