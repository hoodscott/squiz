from django.shortcuts import render
from django.http import HttpResponse

# view for the homepage
def index(request):
	return HttpResponse('Homepage')
	
# view for other page
def about(request):
    return HttpResponse('Squid Logistics')
    
# user joins quiz
def join(request):
	return HttpResponse('Joined')
	
# create quiz/round/questions
def create(request):
    return HttpResponse('Created')
    
# display scorebaord/ questions (and answers to host)
def quiz(request, session_id):
	return HttpResponse('Quiz')
	
# shows pup quizzes and times near to the users location
def nearby(request):
    return HttpResponse('Nearby')
