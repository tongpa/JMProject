
 


Ext.define('survey.panel.ManagePublicationOption',{  
	extend : 'Ext.form.Panel',
	alias: ['widget.ManagePublicationOption'],
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
    setLoad : function (projectRecord,page =1){
    	
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
    	
    },
    initComponent: function() {
		
    	var main = this;
		//main.add111 = Ext.create('survey.view.list.Project.AddQuestion',{msgTarget: 'side'});
		main.showWindowsOption = Ext.create('survey.view.poption.WinPublicationOptionView',{
			url : '/survey/addOptions',
			title : survey.label.create_publication ,
			titleAlign : 'left',
			store : main.store1,
			store1 : main.store2,
			listeners : {
				refreshOther : function(cmp) {
					
					
					main.setLoad(main.record);
		        }
			}
			
		});
		main.tbar =  [{
            xtype:'button',
            text: survey.label.create_publication ,
            iconCls: 'project-add',
            //iconCls: 'add16',
            handler: function(bt,ev){
            	main.showWindowsOption.show();
				//console.log(record);
			 	main.showWindowsOption.setLoadData(main.record );
            }
            //,            menu: [{text: 'Menu Button 1'}]
        }];
		
		main.showListOption = Ext.create('survey.view.poption.ListPublicationOption',{
			store : main.store,
			listeners : {
				showManageOption : function(grid,optionsrecord) {
					main.showWindowsOption.show();
				 	main.showWindowsOption.setLoadData(main.record,optionsrecord );
					 
		        },
		        refreshOther : function(cmp){
		        	main.setLoad(main.record);
		        },
		        changeDataValue : function(paging,page){
		        	main.setLoad(main.record,page);
		        }
			}
		});
		
		main.items = [main.showListOption];
		
		//main.items = main.add111;
		
		this.callParent();
    }
    
});    