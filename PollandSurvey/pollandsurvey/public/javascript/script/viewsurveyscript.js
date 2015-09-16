
var app = angular.module("poll", ['ui.bootstrap','timer' ]);

/**share Broadcast*/
app.factory('setTimerService', function($rootScope) {
	
    var sharedService = {};
    sharedService.message = '';    
    
    /**used call service*/
    sharedService.prepForBroadcast = function(msg) {
        this.message = msg;
        this.broadcastItem();
    };
    /**broadcast to other controller*/
    sharedService.broadcastItem = function() {
        $rootScope.$broadcast('setTimerBroadcast');
    };
    
    
    /**for time out*/
    sharedService.preTimeOutBroadcast = function(msg){
    	this.message =msg;
    	this.broadcastTimeOut();
    }
    
    /**for time out broadcast to other controller*/
    sharedService.broadcastTimeOut = function() {
        $rootScope.$broadcast('setTimeOutBroadcast');
    };

    /**for Progress */
    sharedService.preProgressBroadcast = function(msg){
    	this.message =msg;
    	this.progressBroadcast();
    }
    
    /**for Progress broadcast to other controller*/
    sharedService.progressBroadcast = function() {
        $rootScope.$broadcast('setProgressBroadcast');
    };
    
    return sharedService;
});
 

/**progressBar*/
app.controller('ProgressBarController', function($scope,$timeout,setTimerService){
		 
	  
	 // $scope.maxValue = 1;
	  
	  $scope.progressValue = 0;
	  
	  
	  $scope.$on('setProgressBroadcast', function() {
		  console.log('plus progess');
	        $scope.message = setTimerService.message;
	        console.log($scope.message.init);
	        console.log($scope.message.total);

	        //set time 
	        $scope.progressValue++;
	        $scope.maxValue = $scope.message.total;
	        
	    });
	   
});

/**Timer Controller*/
app.controller('TimerDemoController',  function ($scope,$log,setTimerService) {
    $scope.linkAnchors = function () {
        $('ul.nav a').click(function (){
            var path = $(this).attr('href');
            if (path != '#') {
                window.location = path;
            }
        });
    };
    
    $scope.callbackTimer={};
    $scope.callbackTimer.status='Running';
    $scope.callbackTimer.callbackCount=0;    
    $scope.callbackTimer.finished=function(){
        $scope.callbackTimer.status='COMPLETE!!';
        $scope.callbackTimer.callbackCount++;
        $scope.$apply();
        
        /**set new timer*/
        console.log('call function timeout ');
    	setTimerService.preTimeOutBroadcast({msg:'Time Out'}); 
        
    };
    
    /**handle setTimerBroadcast*/
    $scope.$on('setTimerBroadcast', function() {
        $scope.message = setTimerService.message;
        //set time 
        
        if(setTimerService.message.init > 0){
        	$scope.$broadcast('timer-set-countdown-seconds', setTimerService.message.init);
     	    $scope.$broadcast('timer-start');
        }
        else{
        	
        	$scope.$broadcast('timer-set-countdown-seconds', 120); 
        	$scope.$broadcast('timer-stop');
        	document.getElementsByTagName('timer')[0].hidden = true;
        }
        
        
    });
    
    
    
    $scope.$on('setTimeOutBroadcast', function() {
        $scope.message = setTimerService.message;
        //set time 
        
    });
} );	 


/**controller***/
	app.controller("pollController", function($rootScope,$scope, $http,$window,$log,setTimerService) {
		console.log("pollController");
		
		
		//$scope.url = '/ang/getQuestion';
		$scope.url = 'preview/getDataPreview?idProject=2';
		$scope.idProject = '';
		$scope.idResp = '';
		$scope.content = [];
		
		
		$scope.selectedData={};
		
		/**count select Question**/
		$scope.countQuestion = [];
		
		$scope.lastQuestion =  [];
		
		
		/**for paging**/
		$scope.bigCurrentPage =1;
		/**max for next page**/
		$scope.maxSize =3;
		/**for item per page**/
		$scope.itemPerPage= 1;
		
		/**total of question**/
		$scope.bigTotalItems = 0;
		/**sum question answerd*/
		$scope.numberQuestion =0;
		
		$scope.selected_radio = 1;
		
		$scope.selectAnswer = false;
		
		$scope.init = function(url,idproject,idresp){
			$scope.url = url;
			$scope.idProject = idproject;
			$scope.idResp = idresp;
			
			//console.log(url);
			//console.log(idproject);
			
			$scope.fetchContent();
		}

		
		
		
		/**function for this controller update Question attempted**/
		$scope.updateQuestionsAttemptedCount = function() {
		    $scope.numberQuestion++;
		  };
		
		/**function for this controller for next Question **/
		$scope.setNextQuestion = function (){
			//next Question 
			
			//check Validate before next Question
			//$log.log('selected_radio : ' + ($scope.selectAnswer ) );
			if ($scope.selectAnswer){
			 
				
				//$log.log('Page changed to : ' + ($scope.bigCurrentPage ) );
				//$log.log('Page total to : ' + ($scope.bigTotalItems ) );
				
				$scope.numberQuestion = $scope.numberQuestion +1;
				if( $scope.bigCurrentPage < $scope.bigTotalItems)
				{	$scope.bigCurrentPage = $scope.bigCurrentPage +1;
				 	$scope.pageChanged();
				}
				else{
					if ($scope.bigCurrentPage >= $scope.bigTotalItems){
						$scope.bigCurrentPage = $scope.bigCurrentPage +1;
						$scope.pageChanged();
					}
					
				}
				
				
				$scope.selectAnswer = false;
			}
		}
		
		/**function for this controller for next Question **/
		$scope.setPage = function (pageNo) {
		    $scope.bigCurrentPage = pageNo;
		  };
		  
		  /**function for this controller for next Question **/
		$scope.pageChanged = function() {
		  	
		   // $log.log('Page changed to : ' + ($scope.bigCurrentPage -1) );
		    $scope.contentQuestion = [];
		    $scope.contentQuestion.push($scope.content[($scope.bigCurrentPage-1) ]);
		    
		  //  $log.log($scope.contentQuestion);
		    
		  //  $log.log('countQuestion : ' );
		  //  $log.log($scope.countQuestion);
		    
		  //  $log.log('last data ');
		      console.log($scope.lastQuestion);
		  
		     
		    if( $scope.lastQuestion.length > 0 ){
		    
		    	 
		    	
			    var data = {value : $scope.lastQuestion  };
		    	
		    	
			    
			    //var data ={value : $scope.lastQuestion  }; 
			    
			    data.finished =  ($scope.bigCurrentPage > $scope.bigTotalItems) ||  ($scope.lastQuestion.length == $scope.bigTotalItems);
			    
			    console.log(data);
			    
			    
			    $http.post("/ans/saveQuestion",data).success(function(data,status,heafers, config){
			   
			    	 
			    	if (status == 200 && data.success == true){
			    		value = $scope.lastQuestion.pop(); //remove data;
			    		
			    		console.log('set progress');
			    		setTimerService.preProgressBroadcast({init:1,total:$scope.bigTotalItems}); 
			    		if(data.finished){
			    			//$scope.bigCurrentPage = $scope.bigCurrentPage - 1;
			    			$window.location.href = data.redirect;
			    			
			    		}
			    	}
			    	 
			    }).error(function(data, status, headers, config) {
			    	alert("error");
			        // called asynchronously if an error occurs
			        // or server returns response with an error status.
			      });
			    
			 //   $log.log("save to server:");
			    
		    }
		    
		   // debugger;
		  };
		/**function validate answer */
		$scope.chooseAnswer = function(value) {
			    $scope.selectAnswer = value;
			     
	    }; 
		  
	
		/**Paging**/
		
		/**Query data */
		$scope.fetchContent = function (){
		//	console.log($scope.url);
	        $http.get($scope.url).success(function(response) {
	        	$scope.content = response.questions[0].question;
	        	
	        	$scope.duration_time = response.timer*60;
	        	
	        	$scope.contentQuestion = [];
	        	
	        	$scope.contentQuestion.push($scope.content[0]);
	        	
	        	$scope.bigTotalItems= $scope.content.length;
	        	$scope.maxSize =$scope.bigTotalItems;
	        	if($scope.bigTotalItem >10){
	        		$scope.maxSize = 5
	        	}
	        	//$log.log('Nomber to: ' + $scope.bigTotalItems);
	        	
	        	/**set new timer*/
	        	setTimerService.prepForBroadcast({init:$scope.duration_time}); 
	        	
	        	/**set new progressbar*/
	        	setTimerService.preProgressBroadcast({init:1,total:$scope.bigTotalItems}); 
	
	        	 
	        });
		};
	
	/*	$scope.selectedScore  = function(idQuestion){
			$log.log('Page changed to: ' + idQuestion);
		};
		*/

		/**handle setTimerBroadcast*/
		$scope.$on('setTimerBroadcast', function() {
	        $scope.message = setTimerService.message;
	       
	    });
		
		$scope.$on('setTimeOutBroadcast', function() {
	        $scope.message = setTimerService.message;
	        //set time 
	        $log.log('Time Out!');
	        $scope.bigCurrentPage =   $scope.bigTotalItems +1;
	        //$scope.bigTotalItems = 
	        
	        var qnaObj = new Object();
	        
	        
	        $scope.lastQuestion.push(qnaObj);
	        
	        console.log("time out close");
	       // $scope.pageChanged();
	        
	    });
	    
	   
	});
	

	

/**directive***/	 
	 
	app.directive('contentItem', function ($compile, $templateCache) {
	    /* EDITED FOR BREVITY */

	     console.log("show");
	     
	
	     var radioTemplateFile = '/template/radiotpl.html';
	     var checkboxTemplateFile = '/template/checkboxtpl.html';
	     var imageTemplateFile = '/template/imagetpl.html';
	     
	     var viewimageTemplageFile = '/template/viewradiotpl.html';
	      
	     
	     var getTemplate = function(contentType) {
	         var template = '';
	          
	         switch(contentType) {
	             case 'radio':
	                 template = radioTemplateFile;
	                 
	                 
	                 break;
	             case 'check':
	                 template = checkboxTemplateFile;
	                 break;
	             case 'image':
	                 template = imageTemplateFile;
	                 break;
	             case 'viewradio' :
	            	 template = viewimageTemplageFile;
	            	 break;
	         }

	         return template;
	     }
	     
	      

	    /* EDITED FOR BREVITY */
	     
	     var directive = {};
	     directive.restrict = 'E';
	     directive.scope  =  { content:'=' };
	     directive.template =  '<ng-include src="getTemplateUrl()"/>';
	     
	     directive.link =    function($scope, $element, $attrs) {
	    	 var same = false;
	    	 var qnaObj = new Object();
	    	 $scope.selectedScore = function(id, value, type, object){
	    		    //Click answer
	    		 	$scope.$parent.chooseAnswer(true); 
	    		 	
	    		 	
	    		 	qnaObj = new Object();
	    		 	qnaObj.id = id;
	    		 	qnaObj.idproject = $scope.$parent.idProject;
	    		 	qnaObj.idresp = $scope.$parent.idResp;
	    		 	qnaObj.value = [];
	    		 	qnaObj.value.push(value);
	    		 	qnaObj.type = type;
	    		 	
	    		 	console.log(qnaObj);
	    		 	
	    		 	 
	    		 	same = false;
	    		 	angular.forEach( $scope.$parent.countQuestion, function(qna) {
	    		          if( qna.id === id ) {
	    		        	  same =true;
	    		        	  
	    		        	  switch(type) {
	    			             case 'radio':
		    			            	 qna.value = [];
		    			            	 qna.value.push(value);
	    			            	 	break;
	    			             case 'check':
	    			            	 	var s = false;
	    			            	 	 console.log("check box");
	    			            	 	 for(var i in qna.value){
	    			            	         if(qna.value[i]==value){
	    			            	        	 console.log("same value and remove " + value);
	    			            	        	 qna.value.splice(i,1);
	    			            	        	 s =true;
	    			            	             break;
	    			            	         }
	    			            	     }	    			            	 	
	    			            	 	 
	    			            	 	if (!s){
	    			            	 		qna.value.push(value);
	    			            	 	}
	    			            	 	break;
	    			             case 'image':
	    			            	 qna.value = [];
	    			            	 qna.value.push(value);
	    			                 break;
	    			         } 
	    		        	  
	    		        	  
	    		          }   
	    		 	});	    		 	
	    		 	if (!same) {
	    		 		$scope.$parent.countQuestion.push(qnaObj);
	    		 		
	    		 		$scope.$parent.updateQuestionsAttemptedCount();
	    		 	}
	    	//	 	console.log($scope.$parent.countQuestion);
	    		 	
	    		 	$scope.$parent.lastQuestion.push(qnaObj);
	    	//	 	console.log($scope.$parent.lastQuestion);
	    		 	
	    		 	
	    		 	//debugger;
	    	   };
	    	
	     };
	     
	     
	     directive.controller = function($scope) {
	         $scope.getTemplateUrl = function() {  
	        	 console.log('gettemplate');
	        	  
	        	 if($scope.content == null)
	        	 {
	        		 return getTemplate('radio');
	        	 }
	        	 else{
	        		 return  getTemplate($scope.content.type);
	        	 }
	           
	         }
	       }
	     
	     
	 
	     
	     return directive;
	   
	});
	
 