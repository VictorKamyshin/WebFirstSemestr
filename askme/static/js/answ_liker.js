$('body').on('click','.btn-like-answ', function() {
        var $btn = $(this);
        var aid = $(this).data('a_id');
        var c_type = $(this).data('type');
        my_token = document.cookie.match(/csrftoken=([^;]*)/) && RegExp.$1
        $.ajax({
            type: 'POST',
            url: '/answ_like/',
            data: {val: aid, csrfmiddlewaretoken: my_token, type : c_type}
        }).done(function(resp) {
            $("#answ-like-counter-"+aid).html(resp.val);    
            }).fail(function(err){});  
    });
