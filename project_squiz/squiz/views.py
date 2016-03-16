# django imports
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers

import json

# import forms and models of this project
from forms import *
from models import *


# view for the homepage
def index(request):
    context_dict = {}
    context = RequestContext(request)

    if request.method == 'POST':

        login_form = LoginForm(request.POST)

        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user: # if user is not none then authentication has been successful
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # Then We'll send the user back to the homepage.
                login(request, user)
                return redirect(reverse('index'))
            else:
                # An inactive account was used - no logging in!
                context_dict['disabled_account'] = True
        else:
            # Bad login details were provided. So we can't log the user in.
            context_dict['bad_details'] = True

    else:
        login_form = LoginForm

    quizzes = Quiz.objects.all()
    #todo, append count of rounds, count of plays
    context_dict['quizzes'] = quizzes

    context_dict['login_form'] = login_form


    return render_to_response('squiz/home.html', context_dict, context)
	
# view for other page
def about(request):
    context_dict = {}
    context = RequestContext(request)
    return render_to_response('squiz/about.html', context_dict, context)
    
# user joins quiz
def join(request):
    context_dict = {}
    context = RequestContext(request)
    
    if request.method == 'POST':

        # Gather the teamname and sessionid provided by the user.
        # This information is obtained from the join form.
        teamname = request.POST['teamname']
        sessionid = request.POST['sessionid']
        
        # check that the session exists
        try:
            print sessionid
            quiz_inst = QuizInstance.objects.get(id = sessionid)
            # check that the session is still joinable
            if quiz_inst.state == 'joinable':
                # then join the quiz
                player = Player(name = teamname, score = 0, quiz_instance = quiz_inst)
                player.save()
                
                # redirect to the quiz page
                return redirect(reverse('play', args=[quiz_inst.id]))
            else:
                # this quiz is in progress or over so cannot be joined
                context_dict['closed_session'] = True
        except QuizInstance.DoesNotExist:
            # an invalid session id was entered so we return an error message to the form
            context_dict['invalid_session'] = True

    return render_to_response('squiz/join.html', context_dict, context)
	
# create quiz
@login_required
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
@login_required
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
@login_required
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
@login_required
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
@login_required
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
@login_required
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
def play(request, session_id):
	context_dict = {}
	context = RequestContext(request)
	context_dict['instance'] = get_object_or_404(QuizInstance, id = session_id)
	return render_to_response('squiz/play.html', context_dict, context)

# return current question
def get_question(request):

  # get current question session and current question number
  quiz_inst = QuizInstance.objects.get(id = request.GET['quizID'])  
  current_q = quiz_inst.current_question
  
  # if the quiz is over, get the scoreboard (ordered by score)
  if quiz_inst.state == 'over':
      print "over"
      context_dict = {}
      context = RequestContext(request)
      cereal = serializers.serialize('json', Player.objects.filter(quiz_instance = quiz_inst).order_by('score'))
      return HttpResponse(json.dumps({'scoreboard':cereal}))

  # if the question has updated, then return the new question
  if request.GET['question'] == current_q:
      # return empty response if there has been no update
	    return HttpResponse()
  else:
      # get quiz
      quiz = quiz_inst.quiz

      # get round from roundinquiz
      this_round = RoundInQuiz.objects.filter(this_quiz=quiz).get(number=current_q.split('q')[0]).this_round

      # get question from questioninround
      this_question = QuestionInRound.objects.filter(this_round=this_round).get(number=current_q.split('q')[1]).this_question
      
      
      data = {'question': this_question.question, 'current_q':current_q}
      #return this_question
      return HttpResponse(json.dumps(data))

@login_required
def advance_question(request, instance_id):
    context = RequestContext(request)
    context_dict = {}
    
    quiz_inst = QuizInstance.objects.get(id = instance_id)
    
    # if quiz is over, we cannto do anything
    if quiz_inst.state == 'over':
        return HttpResponse()
  
    current_q = quiz_inst.current_question    
    
    # get quiz
    quiz = quiz_inst.quiz

    # get round from roundinquiz
    try:
        this_round = RoundInQuiz.objects.filter(this_quiz=quiz).get(number=current_q.split('q')[0]).this_round
    except RoundInQuiz.DoesNotExist:
        # we have reached the end of the quiz
        print "in here"
        quiz_inst.state = 'over'
        quiz_inst.save()
        return HttpResponse()        
    
    # split round and question num from unicode string
    current_questionnum = int(current_q.split('q')[1])
    current_roundnum = int(current_q.split('q')[0])
    
    # check if there is another question in this round
    try:
        
        this_question = QuestionInRound.objects.filter(this_round=this_round).get(number=current_questionnum+1)
        # if it exists, increment questionnumber
        quiz_inst.current_question = str(current_roundnum)+'q'+str(current_questionnum+1)
    except QuestionInRound.DoesNotExist:
        # there is not another question in the round, so set end of round case
        
        quiz_inst.current_question = str(current_roundnum+1)+'q0'
    
    # save new pointer in this instance
    quiz_inst.save()
    
    # return empty response
    return HttpResponse()

	
# shows pup quizzes and times near to the users location
def nearby(request):
    context_dict = {}
    context = RequestContext(request)
    lat = float(request.GET.get('lat'))
    lon = float(request.GET.get('lon'))
    
    max_lat = lat + 0.001
    min_lat = lat - 0.001
    max_lon = lon + 0.001
    min_lon = lon - 0.001

    try:
      context_dict['venues'] = Venue.objects.filter(lat__gt=min_lat, lat__lt=max_lat, lon__gt=min_lon, lon__lt=max_lon)
    except Venue.DoesNotExist:
      # no venue at this url
      pass
      
    return render_to_response('squiz/nearby.html', context_dict, context)

def register(request):
    # A HTTP POST?
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        host_form = RegisterHostForm(request.POST)

     # Have we been provided with a valid form?
        if user_form.is_valid() and host_form.is_valid():
            # delay saving the model until we're ready to avoid integrity problems
            user = user_form.save()
            # hash password
            user.set_password(user.password)
            user.save()
            
            host = host_form.save(commit=False)

            # set the onetoOne field of host to be the user
            host.user = user

            # save resource
            host.save()

            return redirect(reverse('index'))

        else:
            # The supplied form contained errors - just print them to the terminal.
            print user_form.errors

    else:
        # If the request was not a POST, display the form to enter details.
        user_form = RegisterUserForm()
        host_form = RegisterHostForm()

    context_dict = {}
    context_dict['user_form'] = user_form
    context_dict['host_form'] = host_form
    context = RequestContext(request)
    return render_to_response('squiz/registration.html', context_dict, context)

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('index'))
    
@login_required
def start(request, quiz_id):
    context_dict = {}
    context = RequestContext(request)
    
    # get the quiz object, 404 if not there
    this_quiz = get_object_or_404(Quiz, id = quiz_id)
    
    # get the current user
    this_host = request.user.host
    
    # create a new quiz instance
    quiz_inst = QuizInstance(quiz = this_quiz, host = this_host, current_question = '0q-1', state='joinable')
    quiz_inst.save()
    
    print quiz_inst.current_question
    
    # redirect user to the play page
    return redirect(reverse('play', args=[quiz_inst.id]))
