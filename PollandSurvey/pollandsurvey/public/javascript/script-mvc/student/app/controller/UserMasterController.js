Ext.define('School.controller.UserMasterController', 
{
    extend : 'Ext.app.Controller',
    models : ['School.model.Student'],
    views : ['School.view.UserMasterView'],
    
    refs : [{
        ref : 'userMasterForm',
        selector : 'viewport > UserMasterView'
    }],
    
    init : function(){
        this.control({
            'viewport > UserMasterView button[itemId=btnCreateUser]' : 
            {
                click : this.onCreateClick
            },
            'viewport > UserMasterView button[itemId=btnResetUser]' : 
            {
                click : this.onResetClick
            } 
        });
    },
    onCreateClick : function(){
    	
    	
        var stdMaster = this.getStudentMasterForm();
        
        if( ! stdMaster.isDirty()){
            Ext.Msg.alert('Status', 'No new data to create.');
            return;
        }
        else if( ! stdMaster.isValid()){
            Ext.Msg.alert('Status', 'Invalid data.');
            return;
        }
        
        var student = Ext.create('School.model.Student'), data,
        url = '/ExtJS4Training/DemoService.svc/createstudent/';
        
        student.set(stdMaster.getValues());
        data = student.getData();
        
        Ext.Ajax.request({
            url : url,
            method : 'POST',
            jsonData : data,
            headers : 
            {
                'Content-Type' : 'application/json'
            },
            success : function(response){
                // process server response here
                //re-load student data with id to set dirty = false, if trackResetOnLoad is true
                var student = Ext.create('School.model.Student');
                var resp = Ext.decode(response.responseText);
                
                if(resp.success){
                    // addstudent returns student model with Id so we can re-load model into form so form will have isDirty false
                    student.set(resp.data[0]);
                    stdMaster.loadRecord(student);
                }
                else{
                    
                    Ext.Msg.alert('Status', resp.message);
                }
                
                Ext.Msg.alert('Status', 'Saved successfully.');
            },
            failure : function(response){
                Ext.Msg.alert('Status', 'Save Failed.');
                
            }
        });
    },
     
    
    onResetClick : function(){
        this.getUserMasterForm().getForm().reset();
    },
    
    onClearClick : function(){
        this.getUserMasterForm().clearForm();
    }
});