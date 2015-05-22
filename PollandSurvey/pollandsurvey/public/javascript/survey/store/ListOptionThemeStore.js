Ext.define('survey.store.ListOptionThemeStore',{
	extend: 'survey.store.MasterStore',
	model : 'Survey.model.listOptionTheme',
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

