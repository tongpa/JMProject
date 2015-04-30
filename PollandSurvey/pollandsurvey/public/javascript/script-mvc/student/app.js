Ext.Loader.setConfig({ enabled: true });

Ext.application({
	appFolder: '/javascript/script-mvc/student/app',
    requires: ['Ext.container.Viewport'],
    name: 'School',
    views: ['School.view.StudentMaster' ],
    //controllers: ['StudentMaster','UserMasterController'],
    controllers: ['StudentMaster' ],
    launch: function () {
        Ext.create('Ext.container.Viewport', {
            layout: 'fit',
            items: [
            {
                xtype: 'StudentMaster'
            }
            /*,{
            	 xtype: 'UserMasterView'
            }*/
            ]
        });
    }
});