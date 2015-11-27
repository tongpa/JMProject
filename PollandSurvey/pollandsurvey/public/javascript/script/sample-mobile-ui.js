var app = angular.module('AngularUIBucket', [
  'ngRoute',
  "ngTouch",
  'mobile-angular-ui',
  
  // touch/drag feature: this is from 'mobile-angular-ui.gestures.js'
  // it is at a very beginning stage, so please be careful if you like to use
  // in production. This is intended to provide a flexible, integrated and and 
  // easy to use alternative to other 3rd party libs like hammer.js, with the
  // final pourpose to integrate gestures into default ui interactions like 
  // opening sidebars, turning switches on/off ..
  'mobile-angular-ui.gestures'
]);


app.config(function($routeProvider, $locationProvider) {
	
	 console.log("route ");
    $routeProvider.when('/', function() {
    	console.log('reload template');
    	return {
            templateUrl: "/template/mobile_signIn.html", reloadOnSearch: false
        };
    	
    });
    
    $routeProvider.when('/samplejs', function() {
    	console.log('reload samplejs');
    	return {
            templateUrl: "/template/mobile_signIn.html", reloadOnSearch: false
        };
    	
    });
});


app.controller('MainController', function($rootScope, $scope){
	
	var scrollItems = [];

	  for (var i=1; i<=100; i++) {
	    scrollItems.push('Item' + i);
	  }

	  $scope.scrollItems = scrollItems;
	  
	  $scope.bottomReached = function() {
		    /* global alert: false; */
		    alert('Congrats you scrolled to the end of the list!');
		  };
});