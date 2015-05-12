Ext.define('Ext.ux.toolbar.CustomToolBar',{
	extend:'Ext.toolbar.Paging',
	alias: ['widget.customtoolbarfield', 'widget.customtoolbar'],
    alternateClassName: ['Ext.ux.CustomToolBar'],
	
    initComponent: function() {
        var me = this;
       
        //me.ddGroup = me.id + '-dd';
        

        // bindStore must be called after the fromField has been created because
        // it copies records from our configured Store into the fromField's Store
        me.bindStore(me.store);
        
        console.log('Ext.ux.toolbar.CustomToolBar');
        me.callParent();
    }
	/*,
    listeners : {
    	'beforechange' : function(toolbar,storeCurrent){
    		console.log('beforechange');
    		return true;
    	}
    }*/
});