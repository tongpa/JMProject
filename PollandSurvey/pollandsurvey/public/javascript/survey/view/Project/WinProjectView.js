Ext.define('survey.view.project.WinProjectView',{
	extend: 'Ext.window.Window',
	alias: ['widget.WinProjectView'],
	requires: [
	           'survey.view.Project.ProjectView' 
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
		main.panelView = Ext.create('survey.view.Project.ProjectView' ,{
			url : main.url,
			showClose : main.showClose,
			parentForm : main,
			listeners : {
				refreshOther : function(cmp) {
		            this.parentForm.refreshOther();
		        }
		    }});
	 	 
		 
		main.items = [main.panelView]; 
		main.panelView.setDefaultField();
		
		this.callParent();
		
		 
		 
	},
	refreshOther : function( ) {
        //do some stuff here
		
        this.fireEvent('refreshOther', this);
    } 
});

 
   