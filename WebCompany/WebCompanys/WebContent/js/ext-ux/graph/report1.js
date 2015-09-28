Ext.define('graph.Sample',{
	//extend : 'Ext.panel.Panel', 	 
	extend: 'Ext.Panel',
    xtype: 'basic-column',

    // <example>
    // Content between example tags is omitted from code preview.
    bodyStyle: 'background: transparent !important',
    layout: {
        type: 'vbox',
        pack: 'center'
    },

    exampleDescription: [
        'A basic column chart is a chart with vertical bars of lengths proportional to the magnitudes of the data it represents. Basic columns are useful for showing data changes over a period of time or for illustrating comparisons among items. Categories are typically organized along the horizontal axis and values along the vertical axis.'
    ],

    themes: {
        classic: {
            percentChangeColumn: {
                width: 75
            }
        },
        neptune: {
            percentChangeColumn: {
                width: 100
            }
        }
    },
    // </example>

    initComponent: function() {
        var me = this;

     

        //<example>
        me.dockedItems = [{
            xtype: 'toolbar',
            dock: 'top',
            items: [
                '->',
            {
                text: 'Save Chart',
                handler: function() {
                    Ext.MessageBox.confirm('Confirm Download', 'Would you like to download the chart as an image?', function(choice){
                        if(choice == 'yes'){
                            me.down('chart').save({
                                type: 'image/png'
                            });
                        }
                    });

                }
            }]
        }];
        //</example>

        me.items = [{
            xtype: 'chart',
            width: '100%',
            height: 410,
            style: 'background: #fff',
            padding: '10 0 0 0',
            insetPadding: 40,
            animate: true,
            shadow: false,
            store: company.listHistorys,
            items: [{
                type  : 'text',
                text  : 'Column Charts',
                font  : '22px Helvetica',
                width : 100,
                height: 30,
                x : 40, //the sprite x position
                y : 12  //the sprite y position
            }, {
                type: 'text',
                text: 'Data: Browser Stats 2012',
                font: '10px Helvetica',
                
                x: 12,
                y: 380
            }, {
                type: 'text',
                text: 'Source: http://www.w3schools.com/',
                font: '10px Helvetica',
                x: 12,
                y: 390
            }],
            axes: [{
                type: 'Numeric',
                position: 'left',
                minimum: 0,
                adjustMinimumByMajorUnit: 0,
                fields: ['num'] ,
                increment :10,
               label: {
                    renderer: function(v) {
                    		var value = v+"";
                    		if(value.indexOf('.') == -1){
                    			console.log(value);
                    			return  value  ;
                    		}
                    		return '';
                    }
                },
                grid: true
                
            }, {
                type: 'Category',
                position: 'bottom',
                fields: ['date_string'],
                grid: true,
                label: {
                    rotate: {
                        degrees: -45
                    }
                }
            }],
            series: [{
                type: 'column',
                axis: 'left',
                xField: 'date_string',
                yField: 'num',
                style: {
                    opacity: 0.80
                },
                highlight: {
                    fill: '#000',
                    'stroke-width': 20,
                    stroke: '#fff'
                },
                tips: {
                    trackMouse: true,
                    style: 'background: #FFF',
                    height: 20,
                    renderer: function(storeItem, item) {
                        this.setTitle(storeItem.get('date_string') + ': ' + storeItem.get('num') + '');
                    }
                }
            }]
        //<example>
        } ];
        
        console.log("list Historys");
        company.listHistorys.load();
        
        this.callParent();
    }
});


Ext.define('graph.report1',{
	extend : 'Ext.panel.Panel',
	bodyPadding: 10,
	defaults: {
        anchor: '100%',
        labelWidth: 80,
        layout: {   type: 'fix' }
    },
	initComponent: function() {
		
		var main = this;
		
		var states = Ext.create('Ext.data.Store', {
		    fields: ['abbr', 'name'],
		    data : [
		        {"abbr":"AL", "name":"Alabama"},
		        {"abbr":"AK", "name":"Alaska"},
		        {"abbr":"AZ", "name":"Arizona"}
		        //...
		    ]
		});
		
		
		main.typeSelect = Ext.create('Ext.form.ComboBox', {
		    fieldLabel: 'Choose State',
		    store: states,
		    queryMode: 'local',
		    displayField: 'name',
		    valueField: 'abbr' ,
		    columnWidth : 0.3
		});
		
		main.selectDate = Ext.create('Ext.form.Label',{
			xtype: 'label',
	        forId: 'myFieldId',
	        text: 'Select Date',
	        margin: '4 0 0 10',
	        columnWidth : 0.20
		});
		main.startDate = Ext.create('Ext.form.field.Date',{
			fieldLabel : 'From',
			maxValue : new Date(),
			columnWidth : 0.4
		});
		main.stopDate = Ext.create('Ext.form.field.Date',{
			fieldLabel : 'To',
			value : new Date(),
			margin: '0 0 0 10',
			columnWidth : 0.4
		});
		
		main.panelSelectDate = Ext.create('Ext.panel.Panel',{
			layout: 'column',
			defaults : {
				labelWidth : 50
			} ,
			columnWidth : 0.7,
			items : [main.selectDate,main.startDate,main.stopDate]
		});
		
		//-------------------------------------------------
		var store = Ext.create('Ext.data.Store', {
            autoLoad : true,
            
            fields : [
                {name : 'id', type : 'int'},
                {name : 'month', type : 'string'}
            ],
            data : [
                {"id" : 0, "month" : "January"},
                {"id" : 1, "month" : "February"},
                {"id" : 2, "month" : "March"},
                {"id" : 3, "month" : "April"},
                {"id" : 4, "month" : "May"},
                {"id" : 5, "month" : "June"},
                {"id" : 6, "month" : "July"},
                {"id" : 7, "month" : "August"},
                {"id" : 8, "month" : "September"},
                {"id" : 9, "month" : "October"},
                {"id" : 10, "month" : "November"},
                {"id" : 11, "month" : "December"}
            ]
        });


        main.startMonth = Ext.create('Ext.form.ComboBox', {
            forceSelection : true,
            columnWidth : 0.4,
            fieldLabel : 'Start',
            store : store,
            queryMode : 'local',
            displayField : 'month',
            valueField : 'id',
            
            listeners : {
                'change' : function(combo, newvalue, oldvalue)
                {
                    
                }
            }
        });
        main.stopMonth = Ext.create('Ext.form.ComboBox', {
            forceSelection : true,
            columnWidth : 0.4,
            fieldLabel : 'To',
            store : store,
            queryMode : 'local',
            displayField : 'month',
            valueField : 'id',
            margin: '0 0 0 10',
            listeners : {
                'change' : function(combo, newvalue, oldvalue)
                {
                    
                }
            }
        });
        main.panelMonthDate = Ext.create('Ext.panel.Panel',{
			layout: 'column',
			defaults : {
				labelWidth : 50
			} ,
			columnWidth : 0.7,
			items : [main.selectDate,main.startMonth,main.stopMonth]
		});
		//-------------------------------------------------
		
        main.btsave = Ext.create('Ext.Button',{		 
			text : 'Search',
			 
			iconCls : 'img-save',
			formBind: true,  
	        disabled: true,
			handler : function(bt,ev){
				var form = this.up('form').getForm();
	            if (form.isValid()) {
	             
	            	var values = form.getValues();
	            	Ext.Ajax.request({
	              		url		: '/WebCompanys/jobs/addJobs',
	                	method  : 'POST',
	                	jsonData: values,	
	                	success: function(response){
	                	    	//store.load();
	                			//company.listPosition();
	                		 main.fireEvent('refreshOther', this);
	                		 
	                		 main.closeWindow(main,bt);
	                		},
	                	failure: function(response) {
	                		alert('error');
	                		//console.log('server-side failure with status code ' + response.status);
	                		
	                		}
	                	});
	             
	          
	            }
	            
			}
		});
		
		
        
		main.fieldSet = Ext.create('Ext.form.Panel',{
			anchor : '100%',
			layout: 'column',
			buttonAlign :'center',
			margin: '0 0 10 0',
			buttons : [ main.btsave],
			items : [main.typeSelect,  main.panelMonthDate]
		});
		
		graph =   Ext.create('graph.Sample');
		
		main.items = [main.fieldSet ,graph];
		
		
		
		
		this.callParent();
	}
});
 
