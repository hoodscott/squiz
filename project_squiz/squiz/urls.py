from django.conf.urls import url

from . import views

urlpatterns = [

	  url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),    
    
    url(r'^create/$', views.create_quiz, name='create'),# create quiz
    
    
    url(r'^quiz/(?P<quiz_id>\w+)$', views.view_quiz, name='view_quiz'),# create quiz    
    
    url(r'^join/$', views.join, name='join'),#user joins quiz
    url(r'^play/(?P<session_id>\w+)$', views.quiz, name='quiz'),# display scoreboard/ questions (and answers to host)
    
    url(r'^nearby/$', views.nearby, name='nearby'),  #shows pup quizzes and times near to the users location

    url(r'^register/$', views.register, name='register'),
]
