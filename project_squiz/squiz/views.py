from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

# view for the homepage
def index(request):
    context_dict = {}
    context = RequestContext(request)
    return render_to_response('squiz/home.html', context_dict, context)
	
# view for other page
def about(request):
    context_dict = {}
    context = RequestContext(request)
    return render_to_response('squiz/about.html', context_dict, context)
    
# user joins quiz
def join(request):
	  return HttpResponse('Joined')
	
# create quiz/round/questions
def create(request):
    context_dict = {}
    context = RequestContext(request)
    return render_to_response('squiz/create_quiz.html', context_dict, context)
    
# display scoreboard/ questions (and answers to host)
def quiz(request, session_id):
	  return HttpResponse('Quiz')
	
# shows pup quizzes and times near to the users location
def nearby(request):
    return HttpResponse('Nearby')

def register(request):
    context_dict = {}
    context = RequestContext(request)
    return render_to_response('squiz/registration.html', context_dict, context)
