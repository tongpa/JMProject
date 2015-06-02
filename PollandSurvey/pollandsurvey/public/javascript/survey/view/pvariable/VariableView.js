 

Ext.define('survey.view.pvariable.VariableView',{
	extend : 'Ext.form.Panel',
	alias: ['widget.VariableView'],
	layout: 'border',
	frame: false,
	bodyPadding: 10,
	showClose : true,
    defaults: {
        anchor: '100%',
        labelWidth: 120
    },
    isCreate : true,
    parentForm : null,
    setDefaultField : function(){
    	var main = this;
    	 
    	console.log('setDefaultField');
    	 
    	 
    },
    setEditField : function(){
    	var main = this;
    	
    	 main.fieldSets.setVisible(true);
    	 
    },
    resetData :function(){
    	this.getForm().reset();
    },
	initComponent : function(){
		var main = this;
		
		main.createOther = Ext.create('Ext.Button',{		 
			 
			text: survey.label.create_publication ,
            iconCls: 'project-add',
            //iconCls: 'add16',
            handler: function(bt,ev){
            	 
            }
		});
		
		main.listVariable = Ext.create('survey.view.pvariable.ListVariableTemplateView',{region: 'west',
            id: 'northPanel',
            labelWidth: 130, // label settings here cascade unless overridden
            frame: true,
            height: 200,
            width: 300,
            defaults: {width: 250},
         //   bodyStyle: 'padding:5px 5px 0',
 
            
            tbar : [ main.createOther]});
		
		main.items = [main.listVariable,
					{
		                 region: 'center',
		                 id: 'westPanel',
		                 labelWidth: 130, // label settings here cascade unless overridden
		                 frame: true,
		                 width: 350,
		              //   bodyStyle: 'padding:5px 5px 0',
		                 defaults: {width: 320},
		                 layout: 'form',
		                 title : 'west' 
					}
					
					];
		 
		
		
		
		 
		this.callParent();
	},
	refreshOther : function(){
		this.fireEvent('refreshOther', this);
		
	},
	closeWindow : function ( bt){
		
		var main = this;
		main.form.reset();
		if(main.ownerCt != null){
			//debugger;
			if(main.ownerCt.ownerCt){
				main.ownerCt.ownerCt.close();
			}
			else{
				main.ownerCt.hide();
			}
			//
			
		}
		
		 
	}
});

   