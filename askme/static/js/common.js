$(document).ready(function() {
    $("button").on("click", function() {
        var $form = $(this).parents('form');
        $.ajax({
            url: '/login/',
            method: 'post',
            dataType: 'json',
            data: {
                username: $form.find('input[name=username]').val(),
                password: $form.find('input[name=password]').val(),
                csrfmiddlewaretoken: $form.find('input[name=csrfmiddlewaretoken]').val(),
            }
        }).done(function (resp) {
            console.log(rest);
        });
        return false;
    });
    var modified = ""
    var request = function() {
        var $body = $('body');
        $.ajax({
            url: 'http://127.0.0.1:7777/sub',
            cache: false,
        }).done(function (resp, status, http_resp) {
            $body.append(resp);
            setTimeout(request, 4000);
        });

    };
    request();
});
