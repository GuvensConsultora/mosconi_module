odoo.define('mosconi_module.hover_modal_define', [], function (require) {
    'use strict';

    $(document).ready(function () {
        $('.hover-modal-trigger').each(function () {
            let $trigger = $(this);
            let modalSelector = $trigger.data('target');
            let timer;
            let countdown = 3;
            let countdownElement = $trigger.find('.hover-countdown');

            function resetCountdown() {
                clearInterval(timer);
                countdown = 3;
                countdownElement.text('');
            }

            $trigger.on('mouseenter', function () {
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

            const $modal = $(modalSelector);
            const $iframe = $modal.find('iframe');

	    $modal.on('shown.bs.modal', function () {
		const updatedVideoUrl = $trigger.data('video-src');  // vuelve a leer el atributo dinámicamente
		$iframe.attr('src', updatedVideoUrl);
	    });

            $modal.on('hidden.bs.modal', function () {
                $iframe.attr('src','');
            });
        });
    });
});
