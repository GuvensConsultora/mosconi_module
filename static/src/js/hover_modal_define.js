odoo.define('mosconi_module.hover_modal_define', [], function (require) {
    'use strict';

    $('.hover-modal-trigger').each(function () {
        let $trigger = $(this);
        let modalSelector = $trigger.data('target');
        let timer;
        let countdown = 3;
        let countdownElement = $trigger.find('.hover-countdown');
	const $modal = $(modalSelector);
        const $iframe = $modal.find('iframe');
        let originalSrc = null; // ← solo en memoria


	
        function resetCountdown() {
            clearInterval(timer);
            countdown = 3;
            countdownElement.text('');
        }

        $trigger.on('mouseenter', function () {
	    if (!originalSrc) {
		originalSrc = $iframe.attr('src'); // guardo en memoria el video
	    }
	    if (!originalSrc) return;
	    
            countdownElement.text(countdown);
            timer = setInterval(function () {
                countdown -= 1;
                countdownElement.text(countdown);
                if (countdown <= 0) {
                    clearInterval(timer);
                    $(modalSelector).modal('show');
                    countdownElement.text('');
                }
            }, 1000);
        });

        $trigger.on('mouseleave', function () {
            resetCountdown();
        });

        //const $modal = $(modalSelector);
        //const $iframe = $modal.find('iframe');
        //const updatedVideoUrl = $iframe.attr('src');
        $modal.on('shown.bs.modal', function () {
	    if (originalSrc) {
                const autoplayUrl = originalSrc.includes('?')
                    ? `${originalSrc}&autoplay=1`
                    : `${originalSrc}?autoplay=1`;
                $iframe.attr('src', autoplayUrl);
            }  //$iframe.attr('src', updatedVideoUrl);
        });

        $modal.on('hidden.bs.modal', function () {
            $iframe.attr('src', "");
        });
    });
});
