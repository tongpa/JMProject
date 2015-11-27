var Languages = function () {

	
		
		
	var loadLanguage = function(){
		
		 
		var cList = $('li.dropdown-language');
		
		$.getJSON( "/model/getLanguages", function( data ) {
			  var items = [];
			  
			  $.each( data.survey, function( key, val ) {
				  console.log(val.code2  + ' - ' + val.name);
				  
				  
				  items.push(  "<li id='" + key + "'>" );
				  items.push( '<a href="javascript:;"  id="showLanguage" onclick="window.Languages.showLanguage(\'' + val.code2 + '\',\''   + val.name + '\'); return false;" >' );  //onclick="window.lang.change(\'' + val.code2 + '\'); return false;"
				  
			   
			    items.push( '<img class="flag" src="/theme/assets/global/img/flags/' +val.code2.toLowerCase()+ '.png"/>');
			    items.push( val.name +' </a>' );
			    items.push(  ' </li>' );
			    
				
			  });
			 
		 	  $( "<ul/>", {
			    "class": "dropdown-menu",
			    html: items.join( "" )
			  }).appendTo( cList );
			 
		});
		 
		
		
	}
		
		 
	 

	 
    
    return {
        //main function to initiate the module
        init: function () {
        	
        	loadLanguage();
             
             
	       
 
        },
        showLanguage: function(lang,name){
        	
        	lang = lang.toLowerCase();
        	window.lang.change(lang); 
        	
        	console.log(lang); 
        	
        	$( "span.main-language" ).replaceWith(
        			'<span id="main-language" class="main-language">' +
        			'<img class="flag" src="/theme/assets/global/img/flags/'+lang+'.png"/><span class="langname">' + name + ' </span> <i class="fa fa-angle-down"></i> ' +
        			'</span>');
        	
        }

    };

}();