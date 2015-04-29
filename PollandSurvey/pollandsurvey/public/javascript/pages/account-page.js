var Account = function () {

	

	var handleAccount = function () {
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
		
		
		function formatGender(state) {
            if (!state.id) return state.text; // optgroup
            return "<img class='flag' src='/img/survey/register-gender/" + state.id.toLowerCase() + ".png'/>&nbsp;&nbsp;" + state.text;
        }
		$("#select2_sample5").select2({
		  	placeholder: '<i class="fa fa-user"></i>&nbsp;Select a Gender',
            allowClear: true,
            formatResult: formatGender,
            formatSelection: formatGender,
            escapeMarkup: function (m) {
                return m;
            }
        });
		$('#select2_sample5').change(function () {
            $('.register-form').validate().element($(this)); //revalidate the chosen dropdown value and show error or success message for the input
        });
		
		
			

		 
	}
    
    return {
        //main function to initiate the module
        init: function () {
        	
             
        	handleAccount();        
        	AccountMenu.init();
        }

    };

}();