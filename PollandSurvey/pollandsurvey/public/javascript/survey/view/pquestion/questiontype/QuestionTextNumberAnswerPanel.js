 

Ext.define('survey.view.pquestion.questiontype.QuestionTextNumberAnswerPanel',{
	extend : 'Ext.panel.Panel',
	alias: ['widget.QuestionTextNumberAnswerPanel'],
	
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
    	
    	/**set show header*/
		 
    	 
    },
    initComponent: function() {
    	
    	
    	 
    	
    	
    	var main = this;
    	 
    	 
    	this.callParent(arguments);    	
    	//this.getSelectionModel().on('selectionchange', this.onSelectChange, this);
    } 
       
 
});

   