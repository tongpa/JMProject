var app = angular.module('listsurvey',['ui.bootstrap','ngTouch', 'ngGrid']);
		 
		
	function listPollSurveyController($scope, $http,$log,$location,$timeout, $interval,$window  ){
		$scope.url = '/getHistoryEmail?page={1}&pagesize={2}';
		$scope.urlReply = '/ans/reply/{1}.{2}.{3}.0.html';
		$scope.currentURL ='';
		$scope.content = [];
		
		$scope.firstName= "John";
	    $scope.lastName= "Doe";
		
	    console.log('historyController');
		/**Paging**/
		var getUrl = $location.url();
		var param = $location.search();
		
		
		$scope.editTeam = function(entity){
			//console.log(entity);
			urlReply = string_inject($scope.urlReply, [  entity.id_question_project,entity.id_question_option,entity.id_voter]);
			 
			$window.open(urlReply, '_blank','toolbar=no, scrollbars=no, resizable=no');
			
		}
		 
	
		$scope.buttonCellTemplate = '<div class=\"ngCellText\" ng-class=\"col.colIndex()\">'+
			'<div ng-edit-cell-if=\"(row.entity.status==0 )\">' +   
				 
				'<button id="editBtn" type="button" class="btn green btn-xs" ng-click="$parent.$parent.editTeam(row.entity)" >Do it </button>' +
			'</div>' +
			'<div ng-edit-cell-if=\"(row.entity.status==1 )\">' +   
				'<span class="label label-sm label-warning"> Finished </span>' +
			'</div>' +
			'</div>'
			;
		 
		
		$scope.filterOptions = {
		        filterText: "",
		        useExternalFilter: true
		    }; 
		
		$scope.totalServerItems = 0;
		
		$scope.page = 1;
		$scope.pagesize = 2;
		
		$scope.pagingOptions = {
		        pageSizes: [2, 10, 20],
		        pageSize: $scope.pagesize,
		        currentPage:  $scope.page 
		};	
		
		$scope.setPagingData = function(data, page, pageSize){	
			 	console.log(data.historys);
			 	data = data.historys;
		        var pagedData = data.slice((page - 1) * pageSize, page * pageSize);
		        $scope.myData = pagedData;
		        $scope.totalServerItems = data.length;
		        if (!$scope.$$phase) {
		            $scope.$apply();
		        }
		        $scope.page = page;
				$scope.pagesize = pageSize;
		    };
		    $scope.getPagedDataAsync = function (pageSize, page, searchText) {
		        setTimeout(function () {
		            var data;
		            if (searchText) {
		                var ft = searchText.toLowerCase();
		                console.log(ft);
		                $http.get($scope.url).success(function (largeLoad) {		
		                    data = largeLoad.filter(function(item) {
		                        return JSON.stringify(item).toLowerCase().indexOf(ft) != -1;
		                    });
		                    $scope.setPagingData(data,page,pageSize);
		                });            
		            } else {
		            	console.log('prev and next');
		            	console.log('page :' + page);
		            	console.log('pageSize :' + pageSize);
		            	
		            	$scope.currentURL = string_inject($scope.url, [  page,pageSize]);
		            	
		                $http.get($scope.currentURL).success(function (largeLoad) {
		                	
		                    $scope.setPagingData(largeLoad,page,pageSize);
		                });
		            }
		        }, 100);
		    };
			
		    $scope.getPagedDataAsync($scope.pagingOptions.pageSize, $scope.pagingOptions.currentPage);
			
		    $scope.$watch('pagingOptions', function (newVal, oldVal) {
		        if (newVal !== oldVal && newVal.currentPage !== oldVal.currentPage) {
		          $scope.getPagedDataAsync($scope.pagingOptions.pageSize, $scope.pagingOptions.currentPage, $scope.filterOptions.filterText);
		        }
		    }, true);
		    $scope.$watch('filterOptions', function (newVal, oldVal) {
		        if (newVal !== oldVal) {
		          $scope.getPagedDataAsync($scope.pagingOptions.pageSize, $scope.pagingOptions.currentPage, $scope.filterOptions.filterText);
		        }
		    }, true);
			
		 

		   
		  
		  
	
		/**Paging**/
		
		$scope.fetchContent = function (){
			
			$scope.currentURL = string_inject($scope.url, [  $scope.page, $scope.pagesize]);
			console.log( $scope.currentURL);
	        $http.get($scope.currentURL).success(function(response) {
	        	$log.log(response.historys);
	        	$scope.content = response.historys;
	        	//$scope.content = response.questions[0].question;;
	        	// debugger;
	        	}
	        );
		};
		
		
		 var start = new Date();
		  var sec = $interval(function () {
		    var wait = parseInt(((new Date()) - start) / 1000, 10);
		    $scope.wait = wait + 's';
		  }, 1000);
		  
		function rowTemplate() {
		    return $timeout(function() {
		      $scope.waiting = 'Done!';
		      $interval.cancel(sec);
		      $scope.wait = '';
		      return '<div ng-class="{ \'my-css-class\': grid.appScope.rowFormatter( row ) }">' +
		                 '  <div ng-repeat="(colRenderIndex, col) in colContainer.renderedColumns track by col.colDef.name" class="ui-grid-cell" ng-class="{ \'ui-grid-row-header-cell\': col.isRowHeader }"  ui-grid-cell></div>' +
		                 '</div>';
		    }, 6000);
		  } 
	
		$scope.selectedEntity;
		 
		$scope.gridHistrory = { 
				data: 'content',
				enablePaging: true,
				showFooter: true,
				jqueryUITheme: true,
				multiSelect: false,
				enableRowSelection: false,
				totalServerItems: 'totalServerItems',
				pagingOptions: $scope.pagingOptions,
		        filterOptions: $scope.filterOptions,
		        //rowTemplate: rowTemplate(),
				//keepLastSelected: false, 
				columnDefs: [ 
				             
				             {field:'duration_date', displayName:'date',width :'25%'},
				             {field:'survey_name', displayName:'Name',width :'25%'},
				             {field:'survey_type', displayName:'Type',width :'25%'},
				             {field:'status', displayName:'Status',width :'25%' ,cellTemplate : $scope.buttonCellTemplate} 
				              
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
					       
					       
					      // mySharedService.prepForBroadcast($scope.selectedEntity.id_export_email);
					    }
					  }
				}
		};
		
		$scope.cumulative = function( grid, myRow ) {
			console.log(myRow);
			 
		    return "1222";
		}
		
		
		
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
	
	
	
	 
	
	function string_inject(sSource, aValues) {
	    var i = 0;
	 
	    if (aValues && aValues.length) {
	        return sSource.replace(/\{\d+\}/g, function(substr) {
	            var sValue = aValues[i];
	 
	            if (sValue) {
	                i += 1;
	                return sValue;
	            }
	            else {
	                return substr;
	            }
	        })
	    }
	 
	    return sSource;
	}; 