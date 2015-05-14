
 


Ext.define('survey.panel.ManageEmailTemplate',{
	//extend : 'Ext.panel.Panel', 	 
	extend : 'Ext.form.Panel',
	layout: 'fit',
	defaults: {
        anchor: '100%',
        labelWidth: 120 
       // layout: {   type: 'fix' }
    },
	frame: true,
	 
	height : 600,
	bodyPadding: 10,
	showClose : true,
    
    isCreate : true,
    parentForm : null,
    loadData : function (projectRecord){
    	
    	this.projectid = '';
    	this.record = projectRecord;
    	if (projectRecord != null && projectRecord.id != null) {
    		
    		this.projectid = projectRecord.id;
    		survey.listInvitationData.load({
				params : {
	    			projectid : projectRecord.id
	    		},
	    		scope : this
			});
    	}
    	
    } ,
    initComponent: function() {
		
		var main = this;
		//main.add111 = Ext.create('survey.view.list.Project.AddQuestion',{msgTarget: 'side'});
		main.showWindowsOption =   Ext.create('survey.view.PEmailTemplate.WinEmailTemplateView',{ // Ext.create('survey.view.list.Project.Invitation.winAddInvitation',{
			url : '/survey/addInvitation',
			title : survey.label.create_invitation ,
			titleAlign : 'left',
			listeners : {
				refreshOther : function(cmp) {
					//survey.listProject.reload();
					
					//main.setLoad(main.record);
		        }
			}
			
		});
		main.tbar =  [{
            xtype:'button',
            text: survey.label.create_invitation ,
            iconCls: 'project-add',
            handler: function(bt,ev){
            	main.showWindowsOption.show();
				console.log(main.record);
			 	main.showWindowsOption.setLoadData(main.record );
            }
            //,            menu: [{text: 'Menu Button 1'}]
        }];
		
		main.showListOption = Ext.create('survey.view.PEmailTemplate.ListEmailTemplate',{
			listeners : {
				showManageOption : function(grid,optionsrecord) {
					main.showWindowsOption.show();
				 	main.showWindowsOption.setLoadData(main.record,optionsrecord );
					 
		        }
			}
		});
		
		main.items = [main.showListOption];
		
		//main.items = main.add111;
		
		this.callParent();
    }
    
});    