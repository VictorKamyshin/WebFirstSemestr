$( ".status-checkbox" ).change(function() {
        var $btn = $(this);
        var aid = $(this).data('a_id');
        var stat = $(this).is(':checked');
       // alert(stat);
        var stat1;
        if(stat) {
            stat1 = "1";
            //alert(stat1);
        } else {
            stat1 = "0";
        }
        my_token = document.cookie.match(/csrftoken=([^;]*)/) && RegExp.$1
        $.ajax({
            type: 'POST',
            url: '/status-change/',
            data: {val: aid, status: stat1, csrfmiddlewaretoken: my_token}
        }).done(function(resp) {
                if(resp.score) {
                var d = document.getElementById("shown-stat-"+aid)
                d.style.display = "block";
                } else {
                //alert("shown-stat-"+aid)
                var d = document.getElementById("shown-stat-"+aid)
                d.style.display = "none";
                }  
            }).fail(function(err){}); 
});
