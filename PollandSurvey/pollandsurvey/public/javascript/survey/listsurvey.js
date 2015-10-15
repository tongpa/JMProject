Ext.namespace("survey");
//Ext.Loader.setConfig({enabled: true});
//Ext.Loader.setPath('survey', '/javascript/survey');

Ext.Loader.setConfig({
    enabled: true,
    paths: {
    	'Ext.ux': '/javascript/extjs-extend/ux',
    	'survey': '/javascript/survey',
    	
        
    }
});

//Ext.Loader.setPath('Ext.ux', '/ux');

Ext.require([
             'Ext.*',
             'Ext.form.*',
             'Ext.layout.container.Column',
             'Ext.tip.QuickTipManager',           
             'Ext.window.MessageBox',
             'Ext.util.Observable',
             'Ext.grid.*',
             'Ext.data.*',
             'Ext.util.*',
             'Ext.state.*', 
             'Ext.Msg.*', 
             'Ext.ux.form.ItemSelector', 
             'Ext.ux.grid.column.UploadFile',
             
             //'survey.model.ListOptionTheme',
             
             //'survey.store.MasterStore',
             //'survey.store.ListOptionThemeStore',
             
             'survey.view.pvoters.ListVoters',
             'survey.view.pvoters.SelectVoters',
             'survey.view.pvoters.VotersView',
             'survey.view.pemailtemplate.ListEmailTemplate',
             'survey.view.pemailtemplate.EmailTemplateView',
             'survey.view.pemailtemplate.WinEmailTemplateView',
             
             'survey.view.poption.ListPublicationOption',
             'survey.view.poption.PublicationOptionView',
             'survey.view.poption.WinPublicationOptionView',
             
             
             'survey.view.pquestion.questiontype.imagepanel.UploadImagePanel',
             'survey.view.pquestion.questiontype.QuestionImageAnswerPanel',
             'survey.view.pquestion.questiontype.QuestionListAnswerPanel',
             'survey.view.pquestion.questiontype.CardQuestionTypePanel',
             'survey.view.pquestion.ListQuestions',
             'survey.view.pquestion.ImageView',
             'survey.view.pquestion.QuestionsView',
             'survey.view.pquestion.WinQuestionsView',
             
             'survey.view.pproject.ProjectView',
             'survey.view.pproject.ListProject',
             'survey.view.pproject.WinProjectView',
             
             'survey.view.pvariable.ListVariableTemplateView',
             'survey.view.pvariable.ListVariableView',
             'survey.view.pvariable.VariableView',
             
             'survey.view.ptrack.ListManageTrackRespondents',
             'survey.view.ptrack.ListManageTrackInvitation',
           //  'survey.view.ptrack.ListPublication',
             
             'survey.panel.ManageTrackInvitation',
             
             'survey.panel.ManageVoters',
             'survey.panel.ManageEmailTemplate',
             'survey.panel.ManagePublicationOption',
             'survey.panel.ManageVariable',
             'survey.panel.ManageQuestion',
             'survey.panel.ManageProject',
             'survey.panel.ManageTrackRespondents'
             
             
            
             
         ]);
 
Ext.tip.QuickTipManager.init(); 


Ext.application({
    name: 'survey',
   
    launch: function() {
    	Ext.tip.QuickTipManager.init();
    	
    	
    	
    	
    	survey.listOptionTheme.load();
    	survey.listDifficultyLevel.load();
    	survey.listRandomType.load();
    	survey.listCloseType.load();
    	
    	//survey.listProject.load();
    	var contact_view = Ext.create('Ext.form.Panel',{
    		title : survey.label.contact,//'Contacts',
    		width: '100%',
    		html : 'Hello !'
    	});
    	
    	
    	var project_view = Ext.create('survey.view.pproject.ListProject',{//'survey.view.list.Project',{   		 
    		flex: 1,
    	    hidden : false,
    	    
    	   // width  : '50%',
    	    height : 800,
			listeners : {
				showManage : function(current,record) {
					
					var tabId =   'tab-' + record.id;
					var title = record.data.name  + " (" + record.data.question_project_type.description + ")";
					var count = tab_project.items.length;
					 
					var addAlready = false;
					
					for (var i = 0 ;i < count ;i++){
						if( tab_project.items.items[i].id == tabId){
							 
							tab_project.setActiveTab(tab_project.items.items[i]);
							addAlready = true;
							break;
						}
					}
					
					if (!addAlready){
					 
						
						var listInvitationData = Ext.create('survey.listInvitationData'); 
						var listQuestionsData = Ext.create('survey.listQuestionsData');
						var listOptionsData = Ext.create('survey.listOptionsData');
						var listInvitationNumberData = Ext.create('survey.listInvitationNumberData');
						var listTrackVoterData = Ext.create('survey.listTrackVoterData');
						var listVoterData = Ext.create('survey.listVoterData');
						
						//manage project 
				    	var manage_project = Ext.create('survey.panel.ManageProject',{   		 
				    		width: '100%',				    	     
				    	    url : '/survey/updateProject'
				    	});
				    	
				    	manage_project.setLoad(record); 
				    	
				    	var manage_question = Ext.create('survey.panel.ManageQuestion',{
				    		width: '100%',   		
				    		title : survey.label.create_question,
				    		store : listQuestionsData,
				    		iconMask: true,
			        		iconCls: "icon-question"
				    	});
				    	
				    	var manage_variable = Ext.create('survey.panel.ManageVariable',{
				    		width: '100%',   		
				    		title : survey.label.create_variable,
				    		iconMask: true,
			        		iconCls: "icon-demographic"
				    	});
				    	
				    	var manage_option = Ext.create('survey.panel.ManagePublicationOption',{
				    		width: '100%',   		
				    		title : survey.label.create_publication,
				    		store : listOptionsData,
				    		store1 : listInvitationData,
				    		store2 : listQuestionsData,
				    		iconMask: true,
				    		iconCls: "icon-publication"
				    	});
				    	
				    	var manage_invitation = Ext.create( 'survey.panel.ManageEmailTemplate',{
				    			//'survey.view.list.Project.PManageInvitations',{
				    		width: '100%',   		
				    		title : survey.label.create_invitation,
				    		store : listInvitationData,
				    		iconMask: true,
			        		iconCls: "icon-invitation"
				    	});
				    	
				    	manage_invitation.loadData(record); 
				    	
				    	var manage_voter = Ext.create('survey.panel.ManageVoters',{
				    		width: '100%',   		
				    		title : survey.label.create_voter,
				    		store : listVoterData,
				    		iconMask: true,
			        		iconCls: "icon-list-voter"
				    	});
				    	
				    	var manage_sendInvitation = Ext.create('survey.panel.ManageTrackInvitation',{
				    		width: '100%',   		
				    		title : survey.label.viewed_invitation,
				    		store : listInvitationNumberData,
				    		store1 : listOptionsData,
				    		iconMask: true,
			        		iconCls: "icon-send-invitation"
				    	});
				    	
				    	
				    	var manage_trackRespondets = Ext.create('survey.panel.ManageTrackRespondents',{
				    		width : '100%',
				    		title : survey.label.track_result,
				    		store : listTrackVoterData,
				    		store1 : listOptionsData,
				    			iconMask: true,
				        		iconCls: "icon-send-invitation"	
				    	});
				    	
				    	
				    	
				    	var tab_manage = Ext.create('Ext.tab.Panel', {
				    	    width: '100%',   
				    	    
				    	    defaults: {
					        	 
					            labelWidth: 120,
					            anchor: '100%',
					            layout: {   type: 'fix' }
					        },
				    	    items: [manage_question,
				    	            manage_variable,
				    	            manage_voter,
				    	            manage_invitation,
				    	            manage_option,
				    	            manage_sendInvitation,
				    	            manage_trackRespondets]
				    	});
				    	
				    	var panel_manage = Ext.create('Ext.panel.Panel',{
				    		closable: true,
				    		frame : true,
				    		bodyPadding: 10,
				    		id : tabId,
				    		title : title,
				    		
				    		items : [manage_project,tab_manage]
				    	});
						
				    	
				    	//var id = Ext.id();
				    	 
				    	 
				    	
				    	manage_question.setLoad(record);
				    	manage_option.setLoad(record);
				    	
						tab_project.add(panel_manage).show();
					
					}

				//	tab_project.setActiveTab(tab);
					
					
					
					 
					
					
		        }
			}
    	} );
    	
    	var mainPanelTab = Ext.create('Ext.form.Panel',{
     
    	    iconMask: true,
    		iconCls: "icon-survey",
    		title : survey.label.poll_survey,
    		width: '100%',
    		height : 800,
    		bodyPadding: 10,
    		//frame : true,
    		 
    	    items :  [project_view ]
    	});
    	
    	var tab_project = Ext.create('Ext.tab.Panel', {
    	    width: '100%',  
    	    height : 800,
    	    title : survey.label.project,
    	    
    	    
    	    layout: {
                type: 'fix'
            }, 
    	    items: [mainPanelTab ]
    	});
    	
    	var tab_main_project = Ext.create('Ext.tab.Panel', {
    	    width: '100%',  
    	    height : 800,
    	   
    	    layout: {                 type: 'fix'             }, 
    	    items: [tab_project,contact_view ]
    	});
    	 
 
    	
    	 Ext.create('Ext.panel.Panel', {
    	// Ext.create('Ext.container.Container', {
    		 renderTo : 'maintenance-app' ,
    		 width : '100%',
    		 
    		 height : 1000,
    		 layout:'fit',
             defaults: {
                 collapsible: true,
                 split: true,
                 bodyStyle: 'padding:15px'
             },
              
             items: [ 
               
             {
                // title: 'Center Region',
                 region: 'center',
                // split: false,
                 xtype: 'panel',
                 layout: 'fit',
                 margins: '5 5 0 0' ,
                 collapsible:false  
                ,items: [tab_main_project ]
                  
             }
             ]
     	});
      
  
    	 
	  
    }

	
});
 
