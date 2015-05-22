Ext.define('survey.view.pquestion.WinQuestionsView',{
	extend: 'Ext.window.Window',
	alias: ['widget.WinQuestionsView'],
	requires: [
	           'survey.view.pquestion.QuestionsView' 
	       ],
	text : survey.label.create_question,
	layout: 'fit',
	
	modal : true,
	width : 600,
	height : 500,
	closable: true,
	 
    closeAction: 'hide',
    showClose : true,
    maximizable: true,
    constrain: true,
    url : '',
    //animateTarget: button,
	header: {
        titlePosition: 2,
        titleAlign: 'center' 
    },
    
    setLoadData : function(projectrecord,questionrecord, questiontyperecord,numberorder){
     
    	
    	this.panelView.setLoadData(projectrecord,questionrecord, questiontyperecord,numberorder);
    },
    
	initComponent: function() {
		
		console.log("init component");
		var main = this;
		main.panelView = Ext.create('survey.view.pquestion.QuestionsView' ,{
			url : main.url,
			showClose : main.showClose,
			parentForm : main,
			listeners : {
				refreshOther : function(cmp) {
					
					 
					main.refreshOther();
		        }
		    }});
	 	 
		 
		main.items = [main.panelView]; 
		 
		this.callParent();
		
		 
		 
	},
	refreshOther : function( ) {
        //do some stuff here

        this.fireEvent('refreshOther', this);
    } 
});

 
   