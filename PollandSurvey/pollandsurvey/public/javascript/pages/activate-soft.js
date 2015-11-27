var Activate = function () {

	

	var handleActivate = function () {
 


         $('.activate-form').validate({
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
	               
	            },

	            submitHandler: function (form) {
	            	 
	            	
	            }
	        });

			$('.activate-form input').keypress(function (e) {
	            if (e.which == 13) {
	                if ($('.activate-form').validate().form()) {
	                    $('.activate-form').submit();
	                }
	                return false;
	            }
	        });
		 
	        
			 
	     
	        jQuery('.activate-form').show();
	}
    
    return {
        //main function to initiate the module
        init: function () {
        	
             
            handleActivate();        
	       
            
	       	$.backstretch([
		        
    		    "/theme/assets/global/pages/media/bg/2.jpg" 
		        ] );
        }

    };

}();