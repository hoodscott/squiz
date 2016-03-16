from django.conf.urls import url

from . import views

urlpatterns = [

	  url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),    
    
    url(r'^create/quiz$', views.create_quiz, name='create_quiz'),# create quiz
    url(r'^create/round/$', views.create_round, name='create_round'),# create round
    url(r'^create/round/(?P<quiz_id>\w+)$', views.create_round, name='create_round'),# create round
    url(r'^create/question/$', views.create_question, name='create_question'),# create question    
    url(r'^create/question/(?P<round_id>\w+)$', views.create_question, name='create_question'),# create question    
    
    url(r'^quiz/(?P<quiz_id>\w+)$', views.view_quiz, name='view_quiz'),# view quiz
    url(r'^round/(?P<round_id>\w+)$', views.view_round, name='view_round'),# view round
    url(r'^question/(?P<question_id>\w+)$', views.view_question, name='view_question'),# view question
    
    url(r'^join/$', views.join, name='join'),#user joins quiz
    url(r'^play/(?P<session_id>\w+)$', views.play, name='play'),# display scoreboard/ questions (and answers to host)
    url(r'^start/(?P<quiz_id>\w+)$', views.start, name='start'),# start a quiz, create a quiz instance
    
    url(r'^nearby/$', views.nearby, name='nearby'),  #shows pup quizzes and times near to the users location
    
    url(r'^get_question/$', views.get_question, name='get_question'),#ajax call to get the current question

    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.user_logout, name='logout'),
]
