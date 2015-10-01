
Ext.define('survey.view.pvoters.SelectVoters',{
	extend : 'Ext.ux.form.ItemSelector',
	alias: ['widget.SelectVoters'],
     
	anchor: '100%',
	imagePath: '../ux/images/',
	//allowBlank: false,
	//msgTarget: 'side',
	fromTitle : survey.label.contact,
    toTitle : survey.label.voters,
     
    displayField: 'name',
    valueField: 'id_voter',
	initComponent : function(){
		main = this;
		 
		this.callParent();
		
		
	}
});

   