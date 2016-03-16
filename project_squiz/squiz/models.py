from django.db import models
from django.contrib.auth.models import User # use built in django user

# model for the users / teachers
class Host(models.Model):
    # Links host to a User model instance.
    user = models.OneToOneField(User)
    
    # hosts website
    url = models.URLField()
	
    def __unicode__(self):
        return "%s" % (self.user)

# Model to hold a question
class Question(models.Model):
    # question and answer as text
    question = models.CharField(max_length=128)
    answer = models.CharField(max_length=128)
    # optional image
    image = models.ImageField(null=True, blank=True)# can be null
    # creator of the question
    creator = models.ForeignKey(Host)
    
    def __unicode__(self):
        return "%s" % (self.question)

# Model to hold a riound (collection of questions)
class Round(models.Model):
    # name of round
    name = models.CharField(max_length=128)
    # creator of the question
    creator = models.ForeignKey(Host)
    
    def __unicode__(self):
        return "%s" % (self.name)    

# Model to hold a quiz (collection of rounds)
class Quiz(models.Model):
    # name of quiz
    name = models.CharField(max_length=128)
    # creator of the question
    creator = models.ForeignKey(Host)
    
    def __unicode__(self):
        return "%s" % (self.name)    
    
# Model used to link questions to rounds
class QuestionInRound(models.Model):
    # link to question
    this_question = models.ForeignKey(Question)
    # link to round
    this_round = models.ForeignKey(Round)
    # what question number is this in the round?
    number = models.IntegerField()
    
    def __unicode__(self):
        return "%s in %s" % (self.this_question, self.this_round)

# Model used to link rounds to quizzes
class RoundInQuiz(models.Model):
    # link to question
    this_round = models.ForeignKey(Round)
    # link to round
    this_quiz = models.ForeignKey(Quiz)
    # what round number is this in the quiz?
    number = models.IntegerField()
    
    def __unicode__(self):
        return "%s in %s" % (self.this_round, self.this_quiz)    

# Model to hold the naem of categories
class Category(models.Model):
    name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return "%s" % (self.name)
    
# Model used to link questions to categories
class QuestionHasCategory(models.Model):
    # link to question
    this_question = models.ForeignKey(Question)
    # link to category
    this_category = models.ForeignKey(Category)
    
    def __unicode__(self):
        return "%s has %s" % (self.this_question, self.this_category)    

# Model used to link rounds to categories
class RoundHasCategory(models.Model):
    # link to question
    this_round = models.ForeignKey(Round)
    # link to category
    this_category = models.ForeignKey(Category)
    
    def __unicode__(self):
        return "%s has %s" % (self.this_round, self.this_category)      
    
# Model used to link the current quiz and it's host to the players
class QuizInstance(models.Model):
    # link to quiz
    quiz = models.ForeignKey(Quiz)
    # link to host
    host = models.ForeignKey(Host)
    
    # joinable - 0, in progress 1, over - 2
    PROGRESS_CHOICES = (
        ('joinable', 'joinable'),
        ('inprogress', 'inprogress'),
        ('over', 'over'),
    )
    state = models.CharField(max_length=32, choices=PROGRESS_CHOICES)    
    
    # string to hold current quesion and round, can be used to poll if next question in ajax
    current_question = models.CharField(max_length=128)
    
    def __unicode__(self):
        return "%s hosting %s" % (self.host, self.quiz)

# model to store the players of a specific quizinstance
class Player(models.Model):
    # string of the teamname
    name = models.CharField(max_length=128)
    # the players score in this quiz
    score = models.IntegerField()
    # the curerent quiz instance the team is playing in
    quiz_instance = models.ForeignKey(QuizInstance)
    
    def __unicode__(self):
        return "%s" % (self.name)    
    
# Model to store the times when a quiz is on
class QuizTime(models.Model):
    # define days of the week
    DAYSOFTHEWEEK = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thurssday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    # store the day the quiz is on
    day = models.CharField(max_length=32, choices=DAYSOFTHEWEEK)
    # store ther time that the quizx starts at
    time  = models.TimeField()
    
    def __unicode__(self):
        return "%s @%s" % (self.day, self.time)
    

# Model to store the venue for quizzes
class Venue(models.Model):
    # name of venue
    name = models.CharField(max_length=128)
    # location of venue
    lat = models.FloatField()
    lon = models.FloatField()
    # host related to this venue
    host = models.ForeignKey(Host)
    # quiztime
    time = models.ForeignKey(QuizTime)
    
    def __unicode__(self):
        return "%s" % (self.name)    
