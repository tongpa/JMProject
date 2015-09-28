
(function() {
     
	var scriptEls = document.getElementsByTagName('script'),
		url_path = scriptEls[scriptEls.length - 1].src,
		i=3;
	//console.log('include-ux');
	//console.log(path);
	while (i--) {
		url_path = url_path.substring(0, url_path.lastIndexOf('/'));
    }
    // path == root of ext
    path = url_path + '/js/ext-ux/graph/'
    
	//console.log(path + 'app.js');
    
   //document.write('<script type="text/javascript" src="/js/extjs/packages/ext-charts/build/ext-charts.js"  charset="UTF-8"></script>');
   /*  
    document.write('<script type="text/javascript" src="' + path + 'model.js"  charset="UTF-8"></script>');
    document.write('<script type="text/javascript" src="' + path + 'addPosition.js"  charset="UTF-8"></script>');
    document.write('<script type="text/javascript" src="' + path + 'listPosition.js"  charset="UTF-8"></script>');
    document.write('<script type="text/javascript" src="' + path + 'listCompany.js"  charset="UTF-8"></script>');

    document.write('<script type="text/javascript" src="' + path + 'listHistory.js"  charset="UTF-8"></script>');
*/
    document.write('<script type="text/javascript" src="' + url_path + '/js/ext-ux/company/model.js"  charset="UTF-8"></script>');
    document.write('<script type="text/javascript" src="' + path + 'report1.js"  charset="UTF-8"></script>');
    document.write('<script type="text/javascript" src="' + path + 'app.js"  charset="UTF-8"></script>');

})();
