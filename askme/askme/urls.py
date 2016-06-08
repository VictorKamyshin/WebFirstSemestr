from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from ask import views as ask_views
from ask.views import index
urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/.*', ask_views.my_logout, name = "logout"),
    url(r'^hot/', ask_views.hot, name = "hot"),
    url(r'^tag', ask_views.tag, name ="tag"),
    url(r'^(?P<question_id>[0-9]+)/$', ask_views.tag, name ="tag"),
    url(r'^login/.*', ask_views.login, name = "login"),
    url(r'^answ_like/.*', ask_views.answ_like, name = "answ_like"),
    url(r'^like/.*', ask_views.like, name = "like"),
    url(r'^give_me_amswer/.*', ask_views.give_me_answer, name = "give_me_answer"),
    url(r'^status-change/.*', ask_views.answ_status_change, name = "status-change"),
    url(r'^another_user/', ask_views.another_user, name = "another_user"),
    url(r'^ask/', ask_views.ask, name = "ask_question"),
    url(r'^profile/', ask_views.profile, name = "profile"),
    url(r'^registration.*', ask_views.registration, name = "registration"),
    url(r'^question/', ask_views.question, name = "question_answers"),
    url(r'^hello/', ask_views.hello, name='hello'),
    url(r'^paramtest/', ask_views.paramtest, name='test'),
    url(r'^$', ask_views.index, name = "index"),

)
