Ext.define('survey.store.MasterStore',{
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