/** @odoo-module */

$(document).ready(function () {
    console.log("hover_modal.js cargado con cuenta regresiva");

    $('.hover-modal-trigger').each(function () {
        const $element = $(this);
        const target = $element.data('target');
        let timeout;
        let interval;
        let countdown = 3;

        // Crear el contador visual si no existe
        const $counter = $('<div class="hover-countdown" style="position:absolute; top:10px; right:10px; background:#000; color:#fff; padding:5px; border-radius:5px; display:none; z-index:999;"></div>');
        $element.css('position', 'relative').append($counter);

        $element.on('mouseenter', function () {
            countdown = 3;
            $counter.text(countdown).show();

            interval = setInterval(() => {
                countdown -= 1;
                $counter.text(countdown);
                if (countdown <= 0) clearInterval(interval);
            }, 1000);

            timeout = setTimeout(() => {
                $counter.hide();
                $(target).modal('show');
            }, 3000);
        });

        $element.on('mouseleave', function () {
            clearTimeout(timeout);
            clearInterval(interval);
            $counter.hide();
        });
    });
});
