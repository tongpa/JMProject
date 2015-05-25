Ext.define('survey.view.poption.WinPublicationOptionView',{
	extend: 'Ext.window.Window',
	alias: ['widget.WinPublicationOptionView'],
	requires: [
	           'survey.view.poption.PublicationOptionView' 
	       ],
	text : survey.label.create_publication ,
	layout: 'fit',
	
	modal : true,
	width : 600,
	height : 600,
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
    	console.log(projectrecord);
    	console.log(optionsrecord);
     	this.panelView.setLoadData(projectrecord,optionsrecord );
    },
    
	initComponent: function() {
		 
		var main = this;
		main.panelView = Ext.create('survey.view.poption.PublicationOptionView' ,{
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

 
   