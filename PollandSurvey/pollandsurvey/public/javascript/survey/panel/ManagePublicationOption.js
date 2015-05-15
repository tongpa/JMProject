
 


Ext.define('survey.panel.ManagePublicationOption',{
	//extend : 'Ext.panel.Panel', 	 
	extend : 'Ext.form.Panel',
	alias: ['widget.ManagePublicationOption'],
	defaults: {
        anchor: '100%',
        labelWidth: 120
    },
	frame: false,
	
	height : 500,
	bodyPadding: 10,
	showClose : true,
    
    isCreate : true,
    parentForm : null,
    setLoad : function (projectRecord){
    	
    	this.projectid = '';
    	this.record = projectRecord;
    	if (projectRecord != null && projectRecord.id != null) {
    		
    		this.projectid = projectRecord.id;
	    	survey.listOptions.load({
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
		main.showWindowsOption = Ext.create('survey.view.POption.WinPublicationOptionView',{
			url : '/survey/addOptions',
			title : survey.label.create_publication ,
			titleAlign : 'left',
			listeners : {
				refreshOther : function(cmp) {
					//survey.listProject.reload();
					
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
		
		main.showListOption = Ext.create('survey.view.POption.ListPublicationOption',{
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