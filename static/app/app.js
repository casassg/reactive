/**
 * Created by casassg on 12/03/16.
 */
$(function() {
    var intro_section = $('.intro');
    var loading_section = $('.loading');
    var happy_section = $('.happy');
    var noface_section = $('.noface');
    var session_id = null;
    var old_result = 0;
    $('.start').on('click', function() {
        intro_section.hide();
        happy_section.hide();
        noface_section.hide();
        loading_section.show();
        $.ajax({
            url:'picture/take',
            dataType: "json"
        }).done(function (data) {
            loading_section.hide();
            session_id= data.id;
            if (data.result=='NOFACE'){
                noface_section.show();
            }
            else{
                show_result(old_result,data.result)
            }
        })
    });

    function show_result(old_r,new_r) {
        var dif =new_r-old_r;

    }
});