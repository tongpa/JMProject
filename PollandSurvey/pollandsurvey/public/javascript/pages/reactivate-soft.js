var Reactivate = function () {

	

	var handleRegister = function () {

		function format(state) {
            if (!state.id) return state.text; // optgroup
            return "<img class='flag' src='/theme/metronic/assets/global/img/flags/" + state.id.toLowerCase() + ".png'/>&nbsp;&nbsp;" + state.text;
        }


		 



         $('.reactivate-form').validate({
	            errorElement: 'span', //default input error message container
	            errorClass: 'help-block', // default input error message class
	            focusInvalid: false, // do not focus the last invalid input
	            ignore: "",

	            invalidHandler: function (event, validator) { //display error alert on form submit   

	            },

	            highlight: function (element) { // hightlight error inputs
	                $(element)
	                    .closest('.form-group').addClass('has-error'); // set error class to the control group
	            },

	            success: function (label) {
	                label.closest('.form-group').removeClass('has-error');
	                label.remove();
	            },

	            errorPlacement: function (error, element) {
	                if (element.attr("name") == "tnc") { // insert checkbox errors after the container                  
	                    error.insertAfter($('#register_tnc_error'));
	                } else if (element.closest('.input-icon').size() === 1) {
	                    error.insertAfter(element.closest('.input-icon'));
	                } else {
	                	error.insertAfter(element);
	                }
	            },

	            submitHandler: function (form) {
	            	 
	            	var sPageURL = window.location.pathname.split("/");
	            	if(sPageURL.length == 3){
	            		 
	            		
	            		$(form).append('<input type="hidden" name="activate_code" value="'+ sPageURL[2] + '" />');
	            		form.submit(); 
	            	}
	            	else{
	            		alert("can not to re activate");
	            	}
	            	//submit with
	            	//form.submit();
	            }
	        });

			$('.reactivate-form input').keypress(function (e) {
	            if (e.which == 13) {
	                if ($('.register-form').validate().form()) {
	                    $('.register-form').submit();
	                }
	                return false;
	            }
	        });
		 
	        
			 
	     
	        jQuery('.reactivate-form').show();
	}
    
    return {
        //main function to initiate the module
        init: function () {
        	
             
            handleRegister();        
	       
            
	       	$.backstretch([
		        
    		    "/theme/metronic/assets/admin/pages/media/bg/2.jpg" 
		        ] );
        }

    };

}();