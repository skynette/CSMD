
// You can also use "$(window).load(function() {"
		$(function () {
			// Slideshow 4
			$("#slider3").responsiveSlides({
				auto: true,
				pager: true,
				nav: false,
				speed: 500,
				namespace: "callbacks",
				before: function () {
					$('.events').append("<li>before event fired.</li>");
				},
				after: function () {
					$('.events').append("<li>after event fired.</li>");
				}
			});

		});

$(function () {
	SyntaxHighlighter.all();
});
$(window).load(function () {
	$(".flexslider").flexslider({
		animation: "slide",
		start: function (slider) {
			$("body").removeClass("loading");
		},
	});
});

jQuery(document).ready(function ($) {
	$(".counter").counterUp({
		delay: 100,
		time: 1000,
	});
});

$(function () {
	// Slideshow 4
	$("#slider3").responsiveSlides({
		auto: true,
		pager: true,
		nav: false,
		speed: 500,
		namespace: "callbacks",
		before: function () {
			$(".events").append("<li>before event fired.</li>");
		},
		after: function () {
			$(".events").append("<li>after event fired.</li>");
		},
	});
});

jQuery(document).ready(function ($) {
	$(".scroll").click(function (event) {
		event.preventDefault();
		$("html,body").animate({ scrollTop: $(this.hash).offset().top }, 1000);
	});
});

$(document).ready(function () {
	/*
				var defaults = {
				containerID: 'toTop', // fading element id
				containerHoverID: 'toTopHover', // fading element hover id
				scrollSpeed: 1200,
				easingType: 'linear' 
				};
			*/

	$().UItoTop({ easingType: "easeOutQuart" });
});

