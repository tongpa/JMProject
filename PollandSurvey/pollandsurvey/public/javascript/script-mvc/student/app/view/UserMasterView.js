Ext.define('School.view.UserMasterView', {

	extend: 'Ext.Panel',
    //extend: 'Ext.form.Panel',
    alias: 'widget.UserMasterView',
    config: {},
    constructor: function (config) {
        this.initConfig(config);
        return this.callParent(arguments);
    },
    
    clearForm: function () {
        this.getForm().getFields().each(function (field) {
            field.validateOnChange = false;
            field.setValue('');
            field.resetOriginalValue();
        });
    },
    initComponent: function () {
        var required = '<span style="color:red;font-weight:bold" data-qtip="Required">*</span>';

        var firstName = Ext.create('Ext.form.field.Text',{
        	name: 'first_name',
        	fieldLabel : 'First Name',
        	allowBlank : false
        });
        var lastName = Ext.create('Ext.form.field.Text',{
        	name: 'last_name',
        	fieldLabel : 'Last Name',
        	allowBlank : false
        });
        
        Ext.apply(this, {
            id: 'UserMasterId',
            title: 'User Information',
            resizable: false,
            collapsible: true,
            bodyPadding: '5',
            buttonAlign: 'center',
            border: false,
            trackResetOnLoad: true,
            layout: {
                type: 'vbox'
            },
            defaults: {
                xtype: 'textfield',
                msgTarget: 'side',
                labelAlign: 'top',
                labelStyle: 'font-weight:bold'
            },
            items: [{
                xtype: 'fieldcontainer',
                layout: 'hbox',
                defaultType: 'textfield',
                width: '100%',
                fieldDefaults: {
                    labelAlign: 'top',
                    labelStyle: 'font-weight:bold'
                },
                items: [ firstName,lastName],
            buttons: [
                { text: 'Ok',
                    itemId: 'btnCreateUser'
                },
                { text: 'Reset',
                    itemId: 'btnResetUser'
                }]
            }]
        });
        this.callParent(arguments);
    }
});