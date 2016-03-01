# django imports
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template import RequestContext

# import forms and models of this project
from squiz.forms import *
from squiz.models import *

# view for the homepage
def index(request):
    context_dict = {}
    context = RequestContext(request)
    
    # if user is authenticated
        # add their quizzes to context_dict['my_quizzes']
        
        # add top quizzes to context_dict['top_quizzes']
        
        # add some more quizzes to context_dict['more_quizzes']
        
    return render_to_response('squiz/home.html', context_dict, context)
	
# view for other page
def about(request):
    context_dict = {}
    context = RequestContext(request)
    return render_to_response('squiz/about.html', context_dict, context)
    
# user joins quiz
def join(request):
	  return HttpResponse('Joined')
	
# create quiz
def create_quiz(request):
    
    # A HTTP POST?
    if request.method == 'POST':
        quiz_form = QuizForm(request.POST)

        # Have we been provided with a valid form?
        if quiz_form.is_valid():
            # delay saving the model until we're ready to avoid integrity problems
            quiz = quiz_form.save(commit=False)
            
            # set foreign key of the creator of the quiz
            quiz.creator = request.user.host

            # save resource before we add tags / set tree
            quiz.save()           
            
            # Now show the new materials page
            return redirect(reverse('view_quiz', args=[quiz.id]))
        else:
            # The supplied form contained errors - just print them to the terminal.
            print quiz_form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        quiz_form = QuizForm()
    
    # create dictionary to pass data to templates
    context_dict = {}
    context = RequestContext(request)
    context_dict['quiz_form'] = quiz_form

    return render_to_response('squiz/create_quiz.html', context_dict, context)

# view a quiz
def view_quiz(request, quiz_id):
    context_dict = {}
    context = RequestContext(request)
    
    try:
      context_dict['quiz'] = Quiz.objects.get(id=quiz_id)
    except Quiz.DoesNotExist:
      # no quiz at this url
      pass
      
    return render_to_response('squiz/view_quiz.html', context_dict, context)

    
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
