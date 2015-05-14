Ext.define('survey.view.PEmailTemplate.WinEmailTemplateView',{
	extend: 'Ext.window.Window',
	alias: ['widget.WinEmailTemplateView'],
	requires: [
	           'survey.view.PEmailTemplate.EmailTemplateView' 
	       ],
//	text : survey.label.create_invitation ,
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
    
    setLoadData : function(projectrecord,optionsrecord ){
    	//console.log('survey.view.list.Project.winAddQuestion');
     	this.panelOption.setLoadData(projectrecord,optionsrecord );
    },
    
	initComponent: function() {
		 
		var main = this;
		main.panelOption = Ext.create('survey.view.PEmailTemplate.EmailTemplateView' ,{
			url : main.url,
			showClose : main.showClose,
			parentForm : main,
			listeners : {
				refreshOther : function(cmp) {
		            this.parentForm.refreshOther();
		        }
		    }});
	 	 
		 
		main.items = [main.panelOption]; 
		 
		this.callParent();
		
		 
		 
	},
	refreshOther : function( ) {
        //do some stuff here

        this.fireEvent('refreshOther', this);
    } 
});

 
   