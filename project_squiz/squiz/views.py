# django imports
from django.shortcuts import render_to_response, redirect, get_object_or_404
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

            # save resource
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
    
# create round
def create_round(request, quiz_id=None):

    # create dictionary to pass data to templates
    context_dict = {}
    context = RequestContext(request)

    if quiz_id != None:
        this_quiz = get_object_or_404(Quiz, id = quiz_id)
        context_dict['quiz'] = this_quiz
    
    # A HTTP POST?
    if request.method == 'POST':
        round_form = RoundForm(request.POST)

        # Have we been provided with a valid form?
        if round_form.is_valid():
            # delay saving the model until we're ready to avoid integrity problems
            this_round = round_form.save(commit=False)
            
            # set foreign key of the creator of the round
            this_round.creator = request.user.host

            # save resource
            this_round.save()
            
            print "saved"
            
            if quiz_id != None:
                # add this new round to the quiz
                round_num = RoundInQuiz.objects.filter(this_quiz = this_quiz).count()
                
                new_record = RoundInQuiz(this_round = this_round, this_quiz = this_quiz, number=round_num)
                new_record.save()
                
                # redirect back to quiz page
                return redirect(reverse('view_quiz', args=[quiz_id]))
            else:
                print quiz_id
                # otherwise show the new round page
                return redirect(reverse('view_round', args=[this_round.id]))
        else:
            # The supplied form contained errors - just print them to the terminal.
            print round_form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        round_form = RoundForm()
    
    context_dict['round_form'] = round_form

    return render_to_response('squiz/create_round.html', context_dict, context)
    
# create question
def create_question(request, round_id=None):

    # create dictionary to pass data to templates
    context_dict = {}
    context = RequestContext(request)

    if round_id != None:
        this_round = get_object_or_404(Round, id = round_id)
        context_dict['round'] = this_round
    
    # A HTTP POST?
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)

        # Have we been provided with a valid form?
        if question_form.is_valid():
            # delay saving the model until we're ready to avoid integrity problems
            question = question_form.save(commit=False)
            
            # set foreign key of the creator of the round
            question.creator = request.user.host

            # save resource before we add tags
            question.save()
            
            if round_id != None:
                # add this new round to the quiz
                question_num = QuestionInRound.objects.filter(this_round = this_round).count()
                
                new_record = QuestionInRound(this_question = question, this_round = this_round, number=question_num)
                new_record.save()
                
                # redirect back to round page
                return redirect(reverse('view_round', args=[round_id]))
            else:
                # otherwise show the new question page
                return redirect(reverse('view_question', args=[question.id]))                   

        else:
            # The supplied form contained errors - just print them to the terminal.
            print question_form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        question_form = QuestionForm()
    
    context_dict['question_form'] = question_form

    return render_to_response('squiz/create_question.html', context_dict, context)

# view a quiz
def view_quiz(request, quiz_id):
    context_dict = {}
    context = RequestContext(request)
    
    try:
      this_quiz = Quiz.objects.get(id=quiz_id)
      context_dict['quiz'] = this_quiz
      context_dict['rounds_in_quiz']  = RoundInQuiz.objects.filter(this_quiz = this_quiz)
    except Quiz.DoesNotExist:
      # no quiz at this url
      pass
      
    return render_to_response('squiz/view_quiz.html', context_dict, context)
    
# view a round
def view_round(request, round_id):
    context_dict = {}
    context = RequestContext(request)
    
    try:
      this_round = Round.objects.get(id=round_id)
      context_dict['round'] = this_round
      context_dict['questions_in_round']  = QuestionInRound.objects.filter(this_round = this_round)
    except Round.DoesNotExist:
      # no round at this url
      pass
      
    return render_to_response('squiz/view_round.html', context_dict, context)
    
# view a question
def view_question(request, question_id):
    context_dict = {}
    context = RequestContext(request)
    
    try:
      this_question = Question.objects.get(id=question_id)
      context_dict['question'] = this_question      

    except Question.DoesNotExist:
      # no round at this url
      pass
      
    return render_to_response('squiz/view_question.html', context_dict, context)

    
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
