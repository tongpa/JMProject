var Register = function () {

	

	var handleRegister = function () {

		function format(state) {
            if (!state.id) return state.text; // optgroup
            return "<img class='flag' src='/theme/metronic/assets/global/img/flags/" + state.id.toLowerCase() + ".png'/>&nbsp;&nbsp;" + state.text;
        }


		$("#select2_sample4").select2({
		  	placeholder: '<i class="fa fa-map-marker"></i>&nbsp;Select a Country',
            allowClear: true,
            formatResult: format,
            formatSelection: format,
            escapeMarkup: function (m) {
                return m;
            }
        });


			$('#select2_sample4').change(function () {
                $('.register-form').validate().element($(this)); //revalidate the chosen dropdown value and show error or success message for the input
            });



         $('.register-form').validate({
	            errorElement: 'span', //default input error message container
	            errorClass: 'help-block', // default input error message class
	            focusInvalid: false, // do not focus the last invalid input
	            ignore: "",
	            rules: {
	                
	                fullname: {
	                    required: true
	                },
	                fulllastname: {
	                    required: true
	                },
	                email: {
	                    required: true,
	                    email: true,
	                    remote : {
	                    	url : '/register/checkUserEmail',
	                    	type : 'post'
	                    }
	                },
	                address: {
	                    required: true
	                },
	                city: {
	                    required: true
	                },
	                country: {
	                    required: true
	                },

	                 
	                password: {
	                    required: true
	                },
	                rpassword: {
	                    equalTo: "#register_password"
	                },

	                tnc: {
	                    required: true
	                }
	            },

	            messages: { // custom messages for radio buttons and checkboxes
	                tnc: {
	                    required: "Please accept TNC first."
	                },
	                fullname : {
	                	 required: "Please Enter Your Name."
	                },
	                email :{
	                	required : "Please Enter Email!",
	                    email: "This is not a valid email!",
	                    remote: "Email already in use!"
	                }
	            },

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
	            	 
	            	
	            	            	 
	            	 
	            	
	            	$.ajax({
	   			     type     : "POST",
	   			     cache    : false,
	   			     url      : '/register/create',//form.attr('action'),
	   			     data     : $(form).serialize(),//form.serializeArray(),
	   			     success  : function(data) {
	   			    	 if(data.success == true){
	   			    		 
	   			    		 $(location).attr('href',"/register/registerSuccess"); 
	   			    	 }
	   			    	 else {
	   			    		 
	   			    		 
	   			    		 return false;
	   			    	 }
	   			     },
	   			    error: function (responseData) {
	                    console.log('Ajax request not recieved!');
	                }
	   			    });
	            	//form.submit();
	            }
	        });

			$('.register-form input').keypress(function (e) {
	            if (e.which == 13) {
	                if ($('.register-form').validate().form()) {
	                    $('.register-form').submit();
	                }
	                return false;
	            }
	        });
			
			/*$('#register-form').submit(function (event ) {
				alert("test");
				event.preventDefault();
				return false;
	        });
			
			$("#register-form").submit(function(){
			    var $form = $(this);
			    
			    if(! $form.valid()) return false;
			     
			    $.ajax({
			     type     : "POST",
			     cache    : false,
			     url      : $form.attr('action'),
			     data     : $form.serializeArray(),
			     success  : function(data) {
			    	 if(data.success == true){
			    		 $(location).attr('href',"/register/registerSuccess"); 
			    	 }
			    	 else {
			    		 return false;
			    	 }
			     }
			    });
			 });
			*/
			/*
			$('#register-submit-btn').click(function(){
				alert("test btn");
				
				$('#register-form').submit( );
		 
			});*/

	        jQuery('#register-back-btn').click(function () {
	        	console.log('register back');
	        	//$('.register-form')[0].reset();
	        	$('.register-form').clearForm();
	        	/* 
	        	$('.register-form input').each(function(){
					$(this).val('');
	        		
	        	});*/
	        });
	        
			 
	     
	        jQuery('.register-form').show();
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