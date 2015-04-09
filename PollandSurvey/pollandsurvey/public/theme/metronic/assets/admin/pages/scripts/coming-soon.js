var ComingSoon = function () {

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
    		          duration: 10000
    		    });

            var austDay = new Date();
            austDay = new Date(austDay.getFullYear() + 1, 1 - 1, 26);
            $('#defaultCountdown').countdown({until: austDay});
            $('#year').text(austDay.getFullYear());
        }

    };

}();