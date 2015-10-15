Ext.define('survey.view.pproject.WinProjectView',{
	extend: 'Ext.window.Window',
	alias: ['widget.WinProjectView'],
	requires: [
	           'survey.view.pproject.ProjectView' 
	       ],
//	text : survey.label.create_invitation ,
	layout: 'fit',
	title : survey.label.add_project  ,
	modal : true,
	width : 600,
	minWidth: 350,
    height: 350,
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
     
    resetData : function(){
    	this.panelView.resetData();
    	this.panelView.setDefaultField();
    }, 
	initComponent: function() {
		 
		var main = this;
		main.panelView = Ext.create('survey.view.pproject.ProjectView' ,{
			url : main.url,
			showClose : main.showClose,
			parentForm : main,
			listeners : {
				refreshOther : function(cmp) {
					
		            main.refreshOther();
		            
		            main.closeWindow(cmp);
		            
		        }
		    }});
	 	 
		 
		main.items = [main.panelView]; 
		main.panelView.setDefaultField();
		
		this.callParent();
		
		 
		 
	},
	refreshOther : function( ) {
        //do some stuff here
		
        this.fireEvent('refreshOther', this);
    } ,
    closeWindow : function ( bt){
		
		var main = this;
		mian.hide();

			
	}
});

 
   