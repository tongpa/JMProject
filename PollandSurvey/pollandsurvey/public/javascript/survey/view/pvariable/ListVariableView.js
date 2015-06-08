 

Ext.define('survey.view.pvariable.ListVariableView',{
	//extend : 'Ext.form.Panel',
	extend : 'Ext.grid.Panel',
	alias: ['widget.ListVariableView'],
	anchor: '100%',
	width : '100%',
	height :  '100%',
	
	frame: false,
	bodyPadding: 10,
	showClose : true,
    defaults: {
        anchor: '100%',
        labelWidth: 120
    },
    isCreate : true,
    parentForm : null,
    collapsible:false ,
    bufferedRenderer: false,
	disableSelection : true,
	forceFit: true,
	store : survey.listVariableTemplate,
	stripeRows       : true,
    getHeaderColumn : function(){
    	var main = this;
    	return [
	       	    {header: survey.label.name, dataIndex: 'name' , width : '99%', sortable: false }         	    	     
	        ] ;
    },
    setDefaultField : function(){
    	var main = this;
    	 
    	console.log('setDefaultField');
    	 
      
    },
    setEditField : function(){
    	var main = this;
    	
    	  
    },
    resetData :function(){
    	this.getForm().reset();
    },
	initComponent : function(){
		var main = this;
		
		var main = this;
   	 
    	main.columns = main.getHeaderColumn(); 
		
    	
    	main.viewConfig = {
                plugins: {
                    ptype: 'gridviewdragdrop',
                    dragGroup: 'secondGridDDGroup',
                    dropGroup: 'firstGridDDGroup'
                },
                listeners: {
                    drop: function(node, data, dropRec, dropPosition) {
                    	
                        //var dropOn = dropRec ? ' ' + dropPosition + ' ' + dropRec.get('name') : ' on empty view';
                        //Ext.MessageBox.show("Drag from left to right", 'Dropped ' + data.records[0].get('name') + dropOn);
                    }
                }
            };
    	
    	
		//main.items = [  ];
		 
		
		
		
		 
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

   