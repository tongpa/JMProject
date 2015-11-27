Ext.define('survey.view.customs.CustomCombobox',{
	extend : 'Ext.form.field.ComboBox',
	alias: ['widget.CustomCombobox'],
	pageSize: 5,
	queryMode: 'local',
	editable : false,
    width : 450,
    forceSelection: true, 
	initComponent: function() { 
		this.callParent();
		 
	},
	/**override*/
	onPageChange: function(toolbar, newPage){
		 
		this.fireEvent('changeDataValue',  toolbar, newPage);
		return false;
	}
	 
});