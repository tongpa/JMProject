Ext.namespace("graph");
Ext.Loader.setConfig({enabled: true});


Ext.require([
	'Ext.*',
    'Ext.grid.*',
    'Ext.data.*',
    'Ext.panel.*',
    'Ext.chart.*',
    'Ext.chart.Chart',
    'Ext.layout.container.Border',
    'Ext.layout.container.Column',
    'Ext.util.*',
    'Ext.state.*',
    'Ext.view.View',
    'Ext.form.*',    
    'Ext.tip.QuickTipManager',           
    'Ext.window.MessageBox',
    'Ext.Msg.*'
]);

//Ext.Loader.setPath('company', '../../../company');


Ext.application({
    name: 'graph',
    launch: function() {
    	Ext.tip.QuickTipManager.init();
    	
    	
    	var showGraph = Ext.create('graph.Sample');
    	
    	Ext.create('Ext.container.Viewport', {
            layout: {
            	type : 'border'
            }, 
            renderTo: Ext.getBody(),
            defaults: {
                collapsible: false,
                split: true 
            },
            
            items: [ {
            	region: 'west',
        		//layout: 'fit',
     	        height : '100%',
     	       xtype: 'panel',
     	        width: 170
    	         
    	        
    	    },     {
    	        region: 'center',
    	        xtype: 'panel', // TabPanel itself has no title
    	        activeTab: 0,      // First tab active by default
    	        layout: 'fit' ,
    	        items : [showGraph]
    	         
    	        
    	    }]
        });
   
    	
    	 
    	
    }
});