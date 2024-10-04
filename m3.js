$(function() {

    function initFullPage() {
        const fullPageInstance = new fullpage('#fullpage-wrapper', {
            licenseKey: 'gplv3-license',
            scrollBar: false,
            scrollingSpeed: 1000,
            navigation: true,
            navigationPosition: 'right',
            navigationTooltips: ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Credits'],
            css3: true,
            autoScrolling: true,
            fitToSection: true,
            scrollOverflow: true,  // Handle overflow for sections
            sectionSelector: '.js-main-slide',
            normalScrollElements: '.fancybox-container',
            afterLoad: function(origin, destination, direction) {
                // When arriving back to Mercury, force it to re-render
                if (destination.index === 0) {
                    $('#fullpage-wrapper .c-main-slide:first-child').css('display', 'none');  // Hide temporarily
                    setTimeout(function(){
                        $('#fullpage-wrapper .c-main-slide:first-child').css('display', 'block');  // Force display again
                    }, 100);  // Small delay to force a repaint
                }
            },
        });
    }

    initFullPage();

});




// Particle js stars
particlesJS("particle-js", {
	"particles": {
		"number": {
			"value": 200,
			"density": {
				"enable": true,
				"value_area": 100
			}
		},
		"color": {
			"value": ["#fff", "#eee"],
		},
		"shape": {
			"type": "circle",
			"stroke": {
				"width": 0,
				"color": "#000",
			}
		},
		"opacity": {
			"value": 0.8,
			"random": true,
			"anim": {
				"enable": true,
				"speed": 1,
				"opacity_min": 0.1,
				"sync": false,
			}
		},
		"size": {
			"value": 1.5,
			"random": true,
			"anim": {
				"enable": true,
				"speed": 1,
				"size_min": 0.2,
				"sync": false
			}
		},
		"line_linked": {
      "enable": false,
      "distance": 100,
      "color": "#000d1f",
      "opacity": 1,
      "width": 0.5
    },
		"move": {
			"enable": false,
			"speed": 3,
			"direction": "none",
			"random": true,
		},
		"interactivity": {
			 "detect_on": "none",
			 "events": {
				 "onhover": {
				 "enable": false,
			 		},
				 "onclick": {
				 "enable": false,
			 		}
			 }
		},
		"retina_detect": true
	}
});