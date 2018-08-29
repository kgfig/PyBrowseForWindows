// On DOM ready
function ready(fn) {
	if (document.treadyState != 'loading') {
		fn();
	} else if (document.addEventListener) {
		document.addEventListener('DOMContentLoaded', fn);
	} else {
		document.attachEvent('onreadystatechange', function() {
			if (document.readystate == 'complete') {
				fn();
			}
		});
	}
}


// App

var app = function() {
	// Add onClick event handler on btn-return buttons
	var elements = document.querySelectorAll('.btn-return');
	Array.prototype.forEach.call(elements, function(el, i) {
		el.addEventListener('click', function(e) {
			var instanceId = el.getAttribute('data-target');
			var request = new XMLHttpRequest();

			request.open('GET', '/catalog/bookinstance/'+ instanceId +'/return', true);
			request.onload = function() {
				alert('instance id: ' + instanceId);
				if (request.status >= 200 && request.status < 400) {
					location.reload();
				} else {
					alert('Return denied');
				}
			};

			request.onerror = function() {
				alert('Return failed!');
			};

			request.send();
		});
	});

	
};

ready(app);

