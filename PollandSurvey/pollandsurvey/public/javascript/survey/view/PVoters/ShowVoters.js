
Ext.define('survey.view.PVoters.ShowVoters',{
	extend : 'Ext.ux.form.ItemSelector',
	alias: ['widget.selectShowVoters'],
     
	anchor: '100%',
	imagePath: '../ux/images/',
	//allowBlank: false,
	//msgTarget: 'side',
	fromTitle : survey.label.contact,
    toTitle : survey.label.voters,
    store: survey.listVoterData,
    displayField: 'name',
    valueField: 'id_voter',
	initComponent : function(){
		main = this;
		 
		this.callParent();
		
		
	}
});

   