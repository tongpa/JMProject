
 


Ext.define('survey.view.list.Project.PVoters',{
	//extend : 'Ext.panel.Panel', 	 
	extend : 'Ext.form.Panel',
 
	defaults: {
        anchor: '100%',
        labelWidth: 120
    },
	frame: false,
	
	height : 200,
	bodyPadding: 10,
	showClose : true,
    
    isCreate : true,
    parentForm : null,
    initComponent: function() {
		
		var main = this;
		
		
		Ext.ux.ajax.SimManager.init({
	        delay: 300,
	        defaultSimlet: null
	    }).register({
	        'Numbers': {
	            data: [[123,'One Hundred Twenty Three'],
	                    ['1', 'One'], ['2', 'Two'], ['3', 'Three'], ['4', 'Four'], ['5', 'Five'],
	                    ['6', 'Six'], ['7', 'Seven'], ['8', 'Eight'], ['9', 'Nine']],
	            stype: 'json'
	        }
	    });
		
		
		
		var ds = Ext.create('Ext.data.ArrayStore', {
	        fields: ['value','text'],
	        proxy: {
	            type: 'ajax',
	            url: 'Numbers',
	            reader: 'array'
	        },
	        autoLoad: true,
	        sortInfo: {
	            field: 'value',
	            direction: 'ASC'
	        }
	    });
		
		main.selectVoters = Ext.create(
				//'Ext.ux.form.ItemSelector' 
				'survey.view.PVoters.ShowVoters'
				,{
			name: 'itemselector',
            id: 'itemselector-field',
         
            store: ds,
            displayField: 'text',
            valueField: 'value',
            value: ['3', '4', '6'] 
            
            
		});

		
		 
		
		
		
		 
		
		
		
		main.tbar =  [{
            xtype:'button',
            text: survey.label.create_voters,
            iconCls: 'add16',
            handler: function(bt,ev){
            	 
            }
        },
        {
            xtype:'button',
            text: survey.label.add_voter_from_contract,
            iconCls: 'add16',
            handler: function(bt,ev){
            	 
            }
        }
        ];
		
		
		
		
		
		
		
		main.items = [main.selectVoters];
		
		this.callParent();
    }
    
});    