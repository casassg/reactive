/**
 * Created by casassg on 12/03/16.
 */
$(function() {
    var intro_section = $('.intro');
    var loading_section = $('.loading');
    var happy_section = $('.happy');
    var session_id = null;
    var old_result = -12;
    intro_section.find('button').on('click', function() {
        intro_section.hide();
        loading_section.show()
        $.ajax({
            url:'picture/take',
            dataType: "json"
        }).done(function (data) {
            loading_section.hide();
            session_id= data.id;
            if(data.result>0){
                happy_section.show();
            }
        })
    });

    function show_result(old_r,new_r) {

    }
});