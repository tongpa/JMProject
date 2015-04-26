var app = angular.module('listsurvey',['ui.bootstrap', 'ngGrid']);
		 
		
	function listPollSurveyController($scope, $http,$log,$location  ){
		$scope.url = '/getHistoryEmail';
		$scope.content = [];
		
		$scope.firstName= "John";
	    $scope.lastName= "Doe";
		
	    console.log('historyController');
		/**Paging**/
		var getUrl = $location.url();
		var param = $location.search();
		
		console.log(param.id);
		 
		
		 
		$scope.setPage = function (pageNo) {
		    $scope.bigCurrentPage = pageNo;
		  };
		  
		  $scope.pageChanged = function() {
			    $log.log('Page changed to: ' + $scope.bigCurrentPage);
			  };

		  $scope.maxSize = 10;
		  $scope.bigTotalItems = 175;
		  $scope.bigCurrentPage = 1;
	
		/**Paging**/
		
		$scope.fetchContent = function (){
			
			 
			
	        $http.get($scope.url).success(function(response) {
	        	$log.log(response.historys);
	        	$scope.content = response.historys;
	        	//$scope.content = response.questions[0].question;;
	        	// debugger;
	        	}
	        );
		};
	
		$scope.selectedEntity;
		 
		$scope.gridHistrory = { 
				data: 'content',
				jqueryUITheme: true,
				multiSelect: false,
				//keepLastSelected: false, 
				columnDefs: [ 
				             
				             {field:'duration_date', displayName:'date',width :'25%'},
				             {field:'survey_name', displayName:'Name',width :'25%'},
				             {field:'survey_type', displayName:'Type',width :'25%'},
				             {field:'status', displayName:'Status',width :'25%'} 
							],
				/*beforeSelectionChange: function(row) {
					  row.changed = true;
					  return true;
					},
					afterSelectionChange : function (rowItem, event) {
						if (rowItem.changed){
					    	console.log("deal with row " + rowItem.rowIndex);
					    	rowItem.changed=false;
						}
					}
				*/
				afterSelectionChange : function (rowItem, event) {
				 	if(rowItem && rowItem.entity){
					    if(rowItem.selected){
					       $scope.selectedEntity = rowItem.entity;
					       
					       //$log.log($scope.selectedEntity);
					       
					       
					       mySharedService.prepForBroadcast($scope.selectedEntity.id_export_email);
					    }
					  }
				}
		};
		
	    $scope.$on('handleBroadcast', function() {
	        $scope.message = mySharedService.message;
	        
	        $log.log("call to historyController :" + mySharedService.message);
	    });
	    
	    
	    $scope.$on('uploadSuccessBroadcast', function() {
	        $scope.message = uploadSuccessService.message;
	        $scope.fetchContent();
	        $log.log("call to historyController(uploadSuccessBroadcast) :" + uploadSuccessService.message);
	    });
	    
	   $scope.fetchContent();
		}