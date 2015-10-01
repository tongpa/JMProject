
 


Ext.define('survey.panel.ManageEmailTemplate',{ 	 
	extend : 'Ext.form.Panel',
	alias: ['widget.ManageEmailTemplate'],
	layout: 'fit',
	defaults: {
        anchor: '100%',
        labelWidth: 120  
    },
	frame: true,
	 
	height : 500,
	bodyPadding: 10,
	showClose : true,
    
    isCreate : true,
    parentForm : null,
    loadData : function (projectRecord,page=1){
    	
    	this.projectid = '';
    	this.record = projectRecord;
    	if (projectRecord != null && projectRecord.id != null) {
    		
    		this.projectid = projectRecord.id;
    		this.showListOption.store.loadPage(page,{
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
		main.showWindowsOption =   Ext.create('survey.view.pemailtemplate.WinEmailTemplateView',{ // Ext.create('survey.view.list.Project.Invitation.winAddInvitation',{
			url : '/survey/addInvitation',
			title : survey.label.create_invitation ,
			titleAlign : 'left',
			listeners : {
				refreshOther : function(cmp) {
					
					main.loadData(main.record);
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
		
		main.showListOption = Ext.create('survey.view.pemailtemplate.ListEmailTemplate',{
			store : main.store,
			listeners : {
				showManageOption : function(grid,optionsrecord) {
					main.showWindowsOption.show();
				 	main.showWindowsOption.setLoadData(main.record,optionsrecord );
					 
		        },
		        changeDataValue : function(paging,page){
		        	main.loadData(main.record,page);
		        	console.log("onBeforeChange");
		        }
			}
		});
		
		main.items = [main.showListOption];
		
		//main.items = main.add111;
		
		this.callParent();
    }
    
});    