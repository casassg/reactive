/**
 * Created by casassg on 12/03/16.
 */
$(function () {
    const IMAGE_NUMBER = 8;
    var intro_section = $('.intro');
    var loading_section = $('.loading');
    var happy_section = $('.happy');
    var noface_section = $('.noface');
    var sad_section = $('.sad');
    var session_id = null;
    var old_result = 0;
    $('.start').on('click', function () {
        intro_section.hide();
        happy_section.hide();
        noface_section.hide();
        sad_section.hide();
        loading_section.show();
        $.ajax({
            url: 'picture/take',
            dataType: "json"
        }).done(function (data) {
            loading_section.hide();
            session_id = data.id;
            if (data.result == 'NOFACE') {
                noface_section.show();
            }
            else {
                show_result(old_result, data.result)
            }
        }).error(function () {
            setTimeout(react,3000)
        })
    });

    function react() {
        sad_section.hide();
        loading_section.show();
        $.ajax({
            url: 'picture/react/' + session_id,
            dataType: "json"
        }).done(function (data) {
            show_result(old_result, data.result)
        });
    }

    function show_result(old_r, new_r) {
        intro_section.hide();
        happy_section.hide();
        noface_section.hide();
        sad_section.hide();
        loading_section.hide();
        if (new_r == 'NOFACE') {
            noface_section.show();
            return;
        }
        if (new_r > 0) {
            var dif = new_r - old_r;
            happy_section.show()
        } else {
            old_result = new_r;
            var gif_id = Math.round(Math.random() * IMAGE_NUMBER);
            console.log(gif_id);
            $('#sad_image').attr('src', 'static/resources/gif/' + gif_id + '.gif');
            sad_section.show();
            setTimeout(react, 3500);

        }
    }
});