$('.btn-like').click(function() {
        var $btn = $(this);
        var qid = $(this).data('q_id');
        var c_type = $(this).data('type');
        my_token = document.cookie.match(/csrftoken=([^;]*)/) && RegExp.$1
        $.ajax({
            type: 'POST',
            url: '/like/',
            data: {val: qid, csrfmiddlewaretoken: my_token, type : c_type}
        }).done(function(resp) {
            $("#like-counter-"+qid).html(resp.val);    
            }).fail(function(err){});  
    });
