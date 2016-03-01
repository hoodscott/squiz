from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    
    url(r'^join/$', views.join, name='join'),#user joins quiz
    
    url(r'^create/$', views.create, name='create'),# create quiz/round/questions
    
    url(r'^quiz/(?P<session_id>\w+)$', views.quiz, name='quiz'),# display scorebaord/ questions (and answers to host)
    
    url(r'^nearby/$', views.nearby, name='nearby'),  #shows pup quizzes and times near to the users location

    url(r'^register/$', views.register, name='register'),
]
