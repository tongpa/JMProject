Ext.define('survey.view.pemailtemplate.WinEmailTemplateView',{
	extend: 'Ext.window.Window',
	alias: ['widget.WinEmailTemplateView'],
	requires: [
	           'survey.view.pemailtemplate.EmailTemplateView' 
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
     
     	this.panelView.setLoadData(projectrecord,optionsrecord );
    },
    
	initComponent: function() {
		 
		var main = this;
		main.panelView = Ext.create('survey.view.pemailtemplate.EmailTemplateView' ,{
			url : main.url,
			showClose : main.showClose,
			parentForm : main,
			listeners : {
				refreshOther : function(cmp) {
		            this.parentForm.refreshOther();
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

 
   