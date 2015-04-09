var Lock = function () {

    return {
        //main function to initiate the module
        init: function () {

             $.backstretch([
		        "/theme/metronic/assets/admin/pages/media/bg/1.jpg",
    		    "/theme/metronic/assets/admin/pages/media/bg/2.jpg",
    		    "/theme/metronic/assets/admin/pages/media/bg/3.jpg",
    		    "/theme/metronic/assets/admin/pages/media/bg/4.jpg"
		        ], {
		          fade: 1000,
		          duration: 8000
		      });
        }

    };

}();