Ext.namespace("survey");

Ext.define('survey.model.listOptionTheme',{
	extend: 'Ext.data.Model',
    idProperty: 'id_question_theme',    
    fields: ['id_question_theme',   'description', 'template', 'active' ] 
});


Ext.define('survey.model.listDifficultyLevel',{
	extend: 'Ext.data.Model',
    idProperty: 'id_fix_difficulty_level',    
    fields: ['id_fix_difficulty_level',   'description' , 'active' ] 
});

Ext.define('survey.model.RandomType',{
	extend: 'Ext.data.Model',
    idProperty: 'id_fix_random_type',    
    fields: ['id_fix_random_type',   'description' , 'active' ] 
});

Ext.define('survey.model.CloseType',{
	extend: 'Ext.data.Model',
    idProperty: 'id_close_type',    
    fields: ['id_close_type',   'description' , 'active' ] 
});


Ext.define('survey.model.listProjectid', {
    extend: 'Ext.data.Model',
    idProperty: 'id_question_project',
    
    fields: ['id_question_project', 'name', 'description', 'user_id', 
             'id_question_project_type','question_project_type',
             'question_project_type.description',
             'header_message','footer_message',
             'welcome_text','end_text',
             'start_date','end_date','active'] 
    
});

Ext.define('survey.model.listQuestionType', {
    extend: 'Ext.data.Model',
    idProperty: 'id_question_type',
    
    fields: ['id_question_type',   'description', 'active' ] 
    
});


Ext.define('survey.model.listAnswerData', {
    extend: 'Ext.data.Model',
    idProperty: 'id_basic_data',    
    fields: ['id_basic_data',   'value','answer','seq','id_question' ,'answer_image','score'] 
    
});

Ext.define('survey.model.listQuestions',{
	extend: 'Ext.data.Model',
    idProperty: 'id_question',    
    fields: ['id_question',   'question','id_qustion_type','help_message','text_label','id_question_project','order','question_type_name','score','id_fix_difficulty_level' ] 
});

Ext.define('survey.model.listOptions',{
	extend: 'Ext.data.Model',
    idProperty: 'id_question_option',    
    fields: ['id_question_option','id_question_project','name_publication',   'header_message','footer_message','welcome_message','end_message','activate_date', 'expire_date',	'create_date','redirect_url','id_question_theme','theme','template','id_question_invitation','send_status' ,'show_score','random_answer','use_question_no','duration_time'] 
});


Ext.define('survey.model.listVoters',{
	extend: 'Ext.data.Model',
    idProperty: 'id_voter',    
    fields: ['id_voter','user_id_owner', 'id_gender','firstname','lastname','prefix','birthdate','email','id_marriage_status'  ] 
});

Ext.define('survey.model.Invitation',{
	extend: 'Ext.data.Model',
    idProperty: 'id_question_invitation',    
    fields: ['id_question_invitation','from_name','name_content', 'subject','id_question_project','content','create_date','update_date'] 
});

Ext.define('survey.model.variable',{
	extend : 'Ext.data.Model',
	idProperty: 'id',
	fields:['id','name']
});

Ext.define('survey.model.InvitationNumber',{
	extend: 'Ext.data.Model',
    idProperty: 'email',    
    fields: ['id_voter','email','name','no_send', 'last_create_date' ] 
});

Ext.define('survey.model.TrackVoter',{
	extend: 'Ext.data.Model',
    idProperty: 'email',    
    fields: ['id_respondents','email','name','response_ip', 'create_date','status','respondent_data','score_exam' ] 
}); 


Ext.define('survey.MasterStore',{
	//extend : 'Ext.panel.Panel', 	 
	extend : 'Ext.data.Store',
	alias: ['widget.MasterStore'],
	autoLoad : false,
	autoSync : false,
	pageSize: 10,
	proxy : {
		reader:{
        	type: 'json',
    		rootProperty : 'survey',
    		totalProperty : 'total'
    	}  ,
		listeners: {
            exception: function(proxy, response, operation){
            	//debugger;
               /* Ext.MessageBox.show({
                    title: 'REMOTE EXCEPTION',
                    msg: operation.getError(),
                    icon: Ext.MessageBox.ERROR,
                    buttons: Ext.Msg.OK
                });
                */
                
            	Ext.MessageBox.alert('Time out','Session Time out', function(){
            		window.location = "/login";
            		
            	});
            	 
                
            } 
        }
	}
});

/*****/
survey.listVariableTemplate = Ext.create('survey.MasterStore',{
	model : 'survey.model.variable',
	storeId : 'listVariableInStore',
	proxy : {
		 
		type: 'ajax',
		url : '/model/getVariableTemplateData',    	
		api: {
            read: '/model/getVariableTemplateData' 
        } ,
        writer: {
        	type: 'json' 
        	 
           // writeAllFields: false ,
           // allowSingle :false 
             
        } 
	},
	autoLoad : true
});

survey.listVariable = Ext.create('survey.MasterStore',{
	model : 'survey.model.variable',
	storeId : 'listVariableInStore',
	proxy : {
		 
		type: 'ajax',
		url : '/model/getVariableTemplateData',    	
		api: {
            read: '/model/getVariableTemplateData' 
        } ,
        writer: {
        	type: 'json' 
        	 
           // writeAllFields: false ,
           // allowSingle :false 
             
        } 
	},
	autoLoad : false
});
/*****/


survey.listProject = Ext.create('survey.MasterStore', {
	model : 'survey.model.listProjectid',
	storeId:'listBookSendInStore',
	 
	proxy : {
		 
		type: 'ajax',
		url : '/model/getProjectByUser',    	
		api: {
            read: '/model/getProjectByUser',
            create: '/model/getProjectByUser',
            update: '/survey/updateProject',
            destroy: '/survey/deleteProject'
        } ,
        writer: {
        	type: 'json' 
        	 
           // writeAllFields: false ,
           // allowSingle :false 
             
        } 
	},
	autoLoad : true
});

survey.listBasicData = Ext.create('survey.MasterStore', {
	model : 'survey.model.listAnswerData',
	storeId:'listBasicDataInStore',
	 
	proxy : {
		 
		type: 'ajax',
		url : '/model/getBasicData',    	
	
        reader:{
        	type: 'json',
    		rootProperty : 'survey',
    		totalProperty : 'total'
    	},
        writer: {
        	type: 'json' ,
        	writeAllFields: true
        	 
           // writeAllFields: false ,
           // allowSingle :false 
             
        } 
	} 
});
/*
survey.listQuestionsData = Ext.create('survey.MasterStore', {
	model : 'survey.model.listQuestions',
	storeId : 'listQuestionsDataInStore',
	 
	proxy : {
		 
		type: 'ajax',
		url : '/model/getQuestionsData',    	
		api: {
            read: '/model/getQuestionsData',
            create: '/survey/createQuestionData',
            update: '/survey/updateQuestionData',
            destroy: '/survey/deleteQuestionData'
        }, 
         
        writer: {
        	type: 'json' 
        	 
           // writeAllFields: false ,
           // allowSingle :false 
             
        } 
	}, 
	autoLoad : true
});
*/

Ext.define('survey.listQuestionsData',{
	//extend : 'Ext.panel.Panel', 	 
	extend : 'survey.MasterStore',
	alias: ['widget.survey.listQuestionsData'],
	model : 'survey.model.listQuestions',
	storeId : 'listQuestionsDataInStore', 
	proxy : {
		 
		type: 'ajax',
		url : '/model/getQuestionsData',    	
		api: {
            read: '/model/getQuestionsData',
            create: '/survey/createQuestionData',
            update: '/survey/updateQuestionData',
            destroy: '/survey/deleteQuestionData'
        }, 
         
        writer: {
        	type: 'json' 
        	 
           // writeAllFields: false ,
           // allowSingle :false 
             
        } 
	}
});




survey.listQuestionType = Ext.create('survey.MasterStore', {
	model : 'survey.model.listQuestionType',
	storeId : 'listQuestionTypeInStore',
	 
	proxy : {
		type : 'ajax',
		url : '/model/getQuestionType',
		reader : {
			type : 'json',
			rootProperty : 'survey'
		}
	} 
});

 
survey.listOptionTheme  = Ext.create('survey.MasterStore', {
	model : 'survey.model.listOptionTheme',
	storeId : 'listOptionThemeInStore',
	 
	proxy : {
		type : 'ajax',
		url : '/model/getOptionTheme',
		reader : {
			type : 'json',
			rootProperty : 'survey'
		}
	} 
});

survey.listDifficultyLevel  = Ext.create('survey.MasterStore', {
	model : 'survey.model.listDifficultyLevel',
	storeId : 'listDifficultyLevelInStore',
	 
	proxy : {
		type : 'ajax',
		url : '/model/getDefficultyLevel',
		reader : {
			type : 'json',
			rootProperty : 'survey'
		}
	} 
});

survey.listRandomType  = Ext.create('survey.MasterStore', {
	model : 'survey.model.RandomType',
	storeId : 'listRandomTypeInStore',
	 
	proxy : {
		type : 'ajax',
		url : '/model/getRandomType',
		reader : {
			type : 'json',
			rootProperty : 'survey'
		}
	} 
});
 
survey.listCloseType  = Ext.create('survey.MasterStore', {
	model : 'survey.model.CloseType',
	storeId : 'listCloseTypeInStore',
	 
	proxy : {
		type : 'ajax',
		url : '/model/getCloseType',
		reader : {
			type : 'json',
			rootProperty : 'survey'
		}
	} 
});

survey.listBasicMediaData = Ext.create('survey.MasterStore', {
	model : 'survey.model.listAnswerData',
	storeId:'listBasicMediaDataInStore',
	 
	proxy : {
		 
		type: 'ajax',
		url : '/model/getBasicMediaData',    	
		api: {
            read: '/model/getBasicMediaData',
            create: '/survey/createBasicMediaData',
            update: '/model/createBasicMediaData',
            destroy: '/model/deleteBasicMediaData'
        }, 
        
        writer: {
        	type: 'json' ,
        	writeAllFields: true
        	 
           // writeAllFields: false ,
           // allowSingle :false 
             
        } 
	} 
});

/**-------------------------------------------------------------**/ 

Ext.define('survey.listOptionsData',{	 
	extend : 'survey.MasterStore',
	alias: ['widget.survey.listOptionsData'],
	model : 'survey.model.listOptions',
	storeId:'listOptionsDataInStore',	 
	proxy : {
		 
		type: 'ajax',
		url : '/model/getOptionsProject',    	
		api: {
            read: '/model/getOptionsProject'
           
        } ,
        writer: {
        	type: 'json' ,
        	writeAllFields: true 
        }
	}
});



Ext.define('survey.listVoterData',{ 
	extend : 'survey.MasterStore',
	alias: ['widget.survey.listVoterData'],
	model : 'survey.model.listVoters',
	storeId:'listVoterDataInStore',
	proxy : {		 
		type: 'ajax',
		url : '/model/getVotersData',    	
		api: {
            read: '/model/getVotersData',
            destroy: '/voter/deleteVoter'            
        }
	}
});

Ext.define('survey.listInvitationData',{
	extend : 'survey.MasterStore',
	alias: ['widget.survey.listInvitationData'],
	model : 'survey.model.Invitation',
	storeId : 'listInvitationDataInStore', 
	proxy : {		 
		type: 'ajax',
		url : '/model/getInvitationData',    	
		api: {
            read: '/model/getInvitationData',
            destroy: '/voter/deleteInvitation'            
        } 
	}
});


Ext.define('survey.listInvitationNumberData',{ 	 
	extend : 'survey.MasterStore',
	alias: ['widget.survey.listInvitationNumberData'],
	model : 'survey.model.InvitationNumber',
	storeId:'listInvitationNumberData',
	proxy : {		 
		type: 'ajax',
		url : '/model/getInvitationNumberData',    	
		api: {
            read: '/model/getInvitationNumberData'            
        } 
	}
});



Ext.define('survey.listTrackVoterData',{ 	 
	extend : 'survey.MasterStore',
	alias: ['widget.survey.listInvitationNumberData'],
	model : 'survey.model.TrackVoter',
	storeId:'listTrackVoterData',
	proxy : {		 
		type: 'ajax',
		url : '/model/getListTrackVosterData',    	
		api: {
            read: '/model/getListTrackVosterData'            
        } 
	}
});

/*
survey.listInvitationData = new Ext.data.Store({
	model : 'survey.model.Invitation',
	storeId:'listInvitationDataInStore',
	pageSize: 50,
	proxy : {
		 
		type: 'ajax',
		url : '/model/getInvitationData',    	
		api: {
            read: '/model/getInvitationData',
            destroy: '/voter/deleteInvitation' 
           
        }, 
        reader:{
        	type: 'json',
    		rootProperty : 'survey',
    		totalProperty : 'total'
    	} ,
        listeners: {
            exception: function(proxy, response, operation){
                Ext.MessageBox.show({
                    title: 'REMOTE EXCEPTION',
                    msg: operation.getError(),
                    icon: Ext.MessageBox.ERROR,
                    buttons: Ext.Msg.OK
                });
            } 
        }
	},
	autoSync: false,
	autoLoad : false
	
});

*/


/*
Ext.define('survey.store.listProjectid', {
    extend: 'Ext.data.Store',
    requires: 'survey.model.listProjectid',
    model: 'survey.model.listProjectid',
    id : 'storelistProjectid',
    leadingBufferZone : 300,
    pageSize : 50,
    proxy :{
    	type : 'jsonp',
    	url : '/survey/getProjectByUser',
    	reader:{
    		rootProperty : 'survey',
    		totalProperty : 'total'
    	}
    	//simpleSortModel true,
    	//simpleGroupMode: true,
    },
    autoLoad : true
});*/