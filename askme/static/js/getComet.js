function getComet() {
        var qid = $('.btn-like').data('q_id');
        $.ajax({
            type: 'GET',
            url: '/jsonp/'+qid,
            data: {chanel_id: qid},
        }).success(function(resp) {
            var div = clearanswer.cloneNode(true);
            div.querySelector(".answer-text").innerHTML = resp.text;
            div.querySelector(".profile-avatar-mainpage-question").src = '/static/media/images/80.jpeg';
            div.querySelector(".btn-like-answ").setAttribute('data-a_id', resp.id);
            div.querySelector(".like-counter").setAttribute('id', 'answ-like-counter-'+resp.id);
            div.querySelector(".btn-dislike-answ").setAttribute('data-a_id', resp.id); 
            div.querySelector(".btn-dislike-answ").className = "btn-like-answ";
            myanswers.appendChild(div, document.body.firstChild);
            getComet();
        }).error( function() {
            setTimeout(getComet, 5000);
        });
}
getComet();
