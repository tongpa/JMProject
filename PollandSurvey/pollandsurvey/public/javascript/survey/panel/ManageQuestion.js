
 


Ext.define('survey.panel.ManageQuestion',{
	//extend : 'Ext.panel.Panel', 	 
	extend : 'Ext.form.Panel',
	layout: 'fit',
	alias: ['widget.ManageQuestion'],
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
    setLoad : function (projectRecord){
    	
    	this.projectid = '';
    	this.record = projectRecord;
    	if (projectRecord != null && projectRecord.id != null) {
    		
    		this.projectid = projectRecord.id;
	    	survey.listQuestionsData.load({
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
		
		main.projectid = Ext.create('Ext.form.field.Hidden',{name : 'id_question_project'});
		 
		
		
		main.winAddQuestion = Ext.create('survey.view.pquestion.WinQuestionsView',{
			url : '/survey/addQuestion',
			title : survey.label.create_question,
			titleAlign : 'left',
			listeners : {
				refreshOther : function(cmp) {
					//survey.listProject.reload();
					main.setLoad(main.record);
		        }
			}
			
		});
		
		main.SplitBt = Ext.create('Ext.button.Split',{
			text : survey.label.create_question,
			//iconCls: 'add16',
			iconCls : 'project-add',
			floating: false
		});
		
		
		
		main.tbar = [main.SplitBt];
		
		
 
		
		main.gridQuestion = Ext.create('survey.view.pquestion.ListQuestions',{
			listeners : {
				showEditQuestion : function(cmp,record) {
					
					main.winAddQuestion.show();
					//console.log(record);
					main.winAddQuestion.setLoadData(main.record,  record, null);
					//survey.listProject.reload();
		        }
			}
		}); 
	 
		
		
		
		main.items = [main.projectid,  main.gridQuestion];
		
		
		//refresh menu
		survey.listQuestionType.load({
			callback :  function(records, operation, success) {
		    	
		    	  
		    	 menus = Ext.create('Ext.menu.Menu');
		    	  
		         if(success){
		        	 for (var i =0;i< records.length ; i++){
		        		 
		        		 menus.add({
		        			 text: records[i].data.description 
		        			 ,record : records[i]
		        			 ,idx: records[i].id 
		        			 ,parentForm : main
		        			 ,handler: main.createQuestion 
		        			 });
		        	 }
		         }
		         
		         main.SplitBt.menu = menus;
		         
		    },
			parent : main,
			scope:this
		});
		
		this.callParent();
    },
    createQuestion : function(bt,ev){
    	 
    	bt.parentForm.winAddQuestion.setTitle( survey.label.create_question + '-' + bt.record.data.description);
    	 
    	bt.parentForm.winAddQuestion.show();
    	
    	//console.log('Add Question');
    	 
    	 
    	bt.parentForm.winAddQuestion.setLoadData(bt.parentForm.record, null, bt.record,bt.parentForm.gridQuestion.getStore().data.length +1);
    }
    
});    