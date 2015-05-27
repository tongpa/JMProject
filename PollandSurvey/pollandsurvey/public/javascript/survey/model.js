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

 


Ext.define('survey.MasterStore',{
	//extend : 'Ext.panel.Panel', 	 
	extend : 'Ext.data.Store',
	alias: ['widget.MasterStore'],
	autoLoad : false,
	autoSync : false,
	pageSize: 50,
	proxy : {
		reader:{
        	type: 'json',
    		rootProperty : 'survey',
    		totalProperty : 'total'
    	}  ,
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
	}
});

survey.listProject = Ext.create('survey.MasterStore', {
	model : 'survey.model.listProjectid',
	storeId:'listBookSendInStore',
	 
	proxy : {
		 
		type: 'ajax',
		url : '/survey/getProjectByUser',    	
		api: {
            read: '/survey/getProjectByUser',
            create: '/survey/getProjectByUser',
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

survey.listOptions = Ext.create('survey.MasterStore', {
	model : 'survey.model.listOptions',
	storeId:'listOptionsInStore',	 
	proxy : {
		 
		type: 'ajax',
		url : '/model/getOptionsProject',    	
		api: {
            read: '/model/getOptionsProject'
            //,create: '/survey/createBasicData'
            //,update: '/model/createBasicData'
            //,destroy: '/model/deleteBasicData'
        } ,
        writer: {
        	type: 'json' ,
        	writeAllFields: true
        	 
           // writeAllFields: false ,
           // allowSingle :false 
             
        } 
	} 
});

survey.listVoterData = Ext.create('survey.MasterStore', {
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

survey.listInvitationData = Ext.create('survey.MasterStore', {
	model : 'survey.model.Invitation',
	storeId:'listInvitationDataInStore',
	proxy : {
		 
		type: 'ajax',
		url : '/model/getInvitationData',    	
		api: {
            read: '/model/getInvitationData',
            destroy: '/voter/deleteInvitation' 
           
        } 
	},
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