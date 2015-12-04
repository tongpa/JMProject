var app = angular.module('listsurvey',['ui.bootstrap','ngTouch', 'ngGrid']);
		 
		
	function listPollSurveyController($scope, $http,$log,$location,$timeout, $interval,$window  ){
		
	    console.log('historyController');
	    
	    $scope.url = '/survey/getProject?page={1}&pagesize={2}';
	    
	    $scope.totalServerItems = 0;
	    $scope.currentURL ="";
		$scope.page = 1;
		$scope.pagesize = 2;
		
		$scope.pagingOptions = {
		        pageSizes: [2, 10, 20],
		        pageSize: $scope.pagesize,
		        currentPage:  $scope.page 
		};
		
		$scope.filterOptions = {
		        filterText: "",
		        useExternalFilter: true
		    }; 
		
		$scope.myData = [{survey_name: "5555", duration_date :   '2015/10/01', survey_type : 'exam', status : 'Finish',url  : 'localhost' },
	                     {survey_name: "5555", duration_date :   '2015/10/01', survey_type : 'exam', status : 'Finish',url  : 'localhost'},
	                     {survey_name: "5555", duration_date :   '2015/10/01', survey_type : 'exam', status : 'Finish',url  : 'localhost'},
	                     {survey_name: "5555", duration_date :   '2015/10/01', survey_type : 'exam', status : 'Finish',url  : 'localhost'},
	                     {survey_name: "5555", duration_date :   '2015/10/01', survey_type : 'exam', status : 'Finish',url  : 'localhost'}];
		
		$scope.setPagingData = function(datas, page, pageSize){	
			console.log(datas);
			data = datas.historys;
	        var pagedData = data//data.slice((page - 1) * pageSize, page * pageSize);
	        $scope.myData = pagedData;
	        $scope.totalServerItems = datas.length;//data.length;
	        if (!$scope.$$phase) {
	            $scope.$apply();
	        }
	    };
	    
	    $scope.getPagedDataAsync = function (pageSize, page, searchText) {
	        setTimeout(function () {
	            var data;
	            if (searchText) {
	                var ft = searchText.toLowerCase();
	                $http.get('/survey/getProject').success(function (largeLoad) {		
	                    data = largeLoad.filter(function(item) {
	                        return JSON.stringify(item).toLowerCase().indexOf(ft) != -1;
	                    });
	                    
	                   
	                    
	                    $scope.setPagingData(data,page,pageSize);
	                });            
	            } else {
	            	
	            	$scope.currentURL = string_inject($scope.url, [  page,pageSize]);
	            	
	            	console.log($scope.currentURL);
	            	
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
	    
	    
	    
		$scope.gridHistrory = { 
				//data: 'content',
				data: 'myData',
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
				             
				             {field:'duration_date', displayName:'Name',width :'35%'},
				             {field:'survey_name', displayName:'project Type',width :'15%'},
				             {field:'survey_type', displayName:'Start Date',width :'20%'},
				             {field:'status', displayName:'Delete',width :'15%' ,cellTemplate : $scope.buttonCellTemplate},
				             {field:'url', displayName:'Edit',width :'15%' ,cellTemplate : $scope.buttonCellTemplate}
				             
				              
							],
				 
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
	 