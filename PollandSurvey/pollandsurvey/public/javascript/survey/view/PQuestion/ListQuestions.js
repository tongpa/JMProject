
Ext.define ('survey.view.PQuestion.ListQuestions',{
	extend : 'Ext.grid.Panel',
	alias: ['widget.ListQuestions'],
     
	anchor: '100%',
	width : '100%',
	height :  '100%',
	 
	store : survey.listQuestionsData,
	bufferedRenderer: false,
	loadMask: true,
	invalidateScrollerOnRefresh: false,
	forceFit: true,
	frame: true,
	hideHeaders : true,
	multiSelect: true,
	itemSelector: 'div.patient-source',
     overItemCls: 'patient-over',
     selectedItemClass: 'patient-selected',
     enableDragDrop: true,
     selType: 'rowmodel',
     stripeRows: true,
    reloadGrid : function(){
    	var main = this;
    	
    },
    htmlTemplate : function(){
 	   return '<tpl for=".">' +
        				'<div class="patient-source"><table><tbody>' +
        				'<tr><td class="patient-label">'+ survey.label.question +'</td><td class="patient-name">{question}</td></tr>' +
        				'<tr><td class="patient-label">'+ survey.label.question_type +'</td><td class="patient-name">{question_type_name}</td></tr>' + 
     
        				'</tbody></table></div>' +
        		'</tpl>';
    },
    getHeaderColumn : function(){
    	var main = this;
    	return [
				 
    	        {
	            	xtype: 'templatecolumn',
	            	tpl: main.htmlTemplate(),
			        listeners: {
			             
			            click: function (g, td) {			            	
			            	var record = main.getSelectionModel().getSelection()[0];			            	
			            	 main.clickOpenQuenstion();
			            },
			            afterrender : function( g, eOpts ){
			            	 
			            	//console.log('afterrender');
			            },
			            move: function( g, component, prevIndex, newIndex, eOpts ){
			            	//console.log('move template column');
			            	//debugger;
			            	
			            	//main.viewConfig.plugins.dragText = g.tpl;
			            }
	                	  
			        } 
		 	        
	            },
				{
		            xtype: 'actioncolumn', 
		            autoSizeColumn : true,
		            menuDisabled:true,
				    sortable: false,
				    renderer: function(a,css,row,d,f,d){}, 
		            layout: {
		            	 type: 'hbox',
		                 align: 'stretch'
		            }, 
		            items: [{ // Delete button
		                iconCls : 'icon-delete'
		                ,tooltip: 'Delete' 
		                ,text : survey.label.delete
		                , flex: 1
		                , handler: function(grid, rowIndex, colindex) {
		                      
		                    var record = grid.getStore().getAt(rowIndex);
		                    
		                    
		                    var datajson = Ext.encode(record.data);
		                    
		                    //console.log(record);
		                    Ext.Msg.show({
		    				    title: survey.message.confirm_delete,
		    				    message: survey.message.confirm_delete + record.data.question,
		    				    buttons: Ext.Msg.YESNO,
		    				    icon: Ext.Msg.QUESTION,
		    				    fn: function(btn) {
		    				        if (btn === 'yes') {
		    				        	 
		    				        	Ext.Ajax.request({
		    			              		url		: '/survey/deleteQuestion',
		    			                	method  : 'POST',
		    			                	jsonData: datajson,	
		    			                	success: function(response, opts){
		    			                		var resp = Ext.decode(response.responseText); 	
		    			                		//console.log(resp);
		    			                		if(resp.success){
		    			                			grid.getStore().remove(record);
		    			                			//main.resetData();
		    			                		}
		    			                		else{
		    			                			Ext.Msg.alert(survey.message.failed, resp.message);
		    			                		}
		    			                			
		    			                			 
		    			                		},
		    			                	failure: function(response, opts) {
		    			                		console.log('server-side failure with status code ' );
		    			                	}
		    			                	
		    				        	});
		    				        	 
		    				        	 
		    				        }  
		    				    }
		    				});
		                    
		                     
		                } 
		            },  '->',
		            { // Save Button
		            	iconCls : 'icon-edit'					                
		                , style: 'margin-left: 5px;'
		                ,text : survey.label.edit
		                ,tooltip: survey.label.edit
		                , flex: 1
		                , handler: function(grid, rowIndex, colindex) {
		                     
		                    var record = grid.getStore().getAt(rowIndex);
		                    main.fireEvent('showEditQuestion', this,record);
		                    
		                    //Ext.Msg.alert('Save', 'Save user: ' + record.data.question);
		                }  
		            }, '->',
		            {
		                iconCls: 'move-up',
		                tooltip: survey.label.move_up,
		                handler: function(grid,index,c,d,f,row){
		                    if(index < 1) return;
		                    var id = row.data.id;
		                    var old = index ;
		                    console.log('orig : ' + (old +1)  );
		                    //index--;
		                    index = index -1;
		                    console.log('new  : ' + (index+1));
		                     
		                    grid.store.remove(row, true);
		                    grid.getStore().insert(index, row);
		                    
		                    //row.set('order',10);
		                    grid.getStore().data.items[old].set('order', (old+1));
		                    grid.getStore().data.items[index].set('order', (index+1) );
		                    grid.getStore().sync();
		                    console.log (id + ' is move up from ' + row.data.order + ' to ' + (index+1));
		                }
		            }, '->',
		            {
		                iconCls: 'move-down',
		                tooltip: survey.label.move_down,
		                handler: function(grid,index,c,d,f,row)
		                {
		                    if(index >= grid.all.endIndex)  return;
		                    //index++;
		                    var old = index ;
		                    console.log('orig : ' + index);
		                    index = index +1;
		                    console.log('new  : ' + index);
		                    
		                    grid.store.remove(row, true);
		                    grid.getStore().insert(index, row);
		                    
		                    grid.getStore().data.items[old].set('order', (old+1));
		                    grid.getStore().data.items[index].set('order', (index+1) );
		                    grid.getStore().sync();
		                    console.log (id + ' is move down from ' + row.data.order + ' to ' + (index-1));
		                }
		            }]
		        } 
				 
        ];
    } ,
	initComponent: function() {
		var main = this;
		
		var group1 = this.id + 'group1' ;
		main.viewConfig =  {
			    plugins: {
			        ptype: 'gridviewdragdrop',
			        containerScroll: true,
			        enableDrop: true,
			          enableDrag: true,
			        dragGroup: 'groupQuestion1',
			        dropGroup: 'groupQuestion1' 
			       /*, dragText: '<tpl for=".">' +
				                '<div class="patient-source"><table><tbody>' +
			                    '<tr><td class="patient-label">Question</td><td class="patient-name">test</td></tr>' +
			                    '<tr><td class="patient-label">Question Type</td><td class="patient-name">Single Choice</td></tr>' + 
			                 
				                '</tbody></table></div>' +
				             '</tpl>'*/
			        	//'Drag and drop to reorganize'
			    },
		           
	             listeners: {
	            	 refresh : function(dataview){
	             		Ext.each(dataview.panel.columns, function (column) {
	             		       if (column.autoSizeColumn === true)
	             		        column.autoSize();
	             		      })
	             	},
	                 drop: function(node, data, overModel, dropPosition, eOpts) {
	                	 //console.log('drop');
	                	
	                	
	                	if(dropPosition == 'before'){
	                		//console.log('before');
	                	}
	                	else {
	                		if (dropPosition == 'after'){
	                			//console.log('after');
	                		}
	                	}
	                	count_order =1;
	                	this.store.each(function(record){ 
	           			 
	            			 
	            			record.set('order', count_order);
	            			count_order =count_order+1;
	            			
	            		});
	                	
	                	this.store.sync();
	            		console.log('count_order : '+ count_order);
	                	
	                	
	                	 
	                	 
	                	 //if(data.records[0].isLeaf()){ 	                		 if(data.records[0].parentNode.data.id!=overModel.parentNode.data.id) 	                		              return false;}
	                	 
	                     //var dropOn = dropRec ? ' ' + dropPosition + ' ' + dropRec.get('question') : ' on empty view';
	                     //Ext.example.msg("Drag from left to right", 'Dropped ' + data.records[0].get('question') + dropOn);
	                 } 
	             }
		
		};
		main.columns = main.getHeaderColumn();
		
		
		this.callParent(arguments);  
	},
	clickOpenQuenstion : function(){
		//console.log('click1'); 
		
		survey.listQuestionsData.each(function(record){ 
			 
			//console.log(record) ; 
		});
		
		survey.listQuestionsData.sync();
		//debugger;
	},
    listeners: {
    	render: function(c,m){
    	//	initializePatientDragZone(c);
        	//console.log('render');
        },
        beforeselect : function(c,record,index,eOpts){
        	//console.log('beforeselect');
        	//debugger;
        	
        	
        }
         
    }
});

   