import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_squiz.settings')

import django
django.setup()

from squiz.models import *
from datetime import datetime

def populate():
    # add users
    david = add_Host('david', 'http://www.tangowithdjango.com/')
    dovid = add_Host('david', 'http://www.tangowithdjango.com/')
    leifos = add_Host('leifos', 'http://www.tangowithdjango.com/')
    
    squiz = add_Host('squiz', 'http://squidl.pythonanywhere.com/')
    
    
    # create categories
    sport = add_cat('Sports')
    general = add_cat('General')
    spongebob = add_cat('Spongebob')
    
    # create questions
    sb1 = add_question('Who lives in a pineapple under the sea?', 'Spongebob Squarepants', squiz)
    add_question_has_category(sb1, spongebob)
    
    sb2 = add_question('Who lives in a moai under the sea?', 'Squidward Tentacles', squiz)
    add_question_has_category(sb2, spongebob)
    
    sb3 = add_question('Who lives under a rock under the sea?', 'Patrick Star', squiz)
    add_question_has_category(sb3, spongebob)
    
    sp1 = add_question('What is the only sport to have been played on the surface of the moon?', 'Golf', squiz)
    add_question_has_category(sp1, sport)
    
    sp2 = add_question(' What is the highest possible break in snooker?', '147', squiz)
    add_question_has_category(sp2, sport)
    
    sp3 = add_question('Which English premier league team was once known as "The Biscuit Men"?', 'Reading', squiz)
    add_question_has_category(sp3, sport)
    
    gk1 = add_question('Who is the only British Prime Minister to be assassinated?', 'Spencer Percival', squiz)
    add_question_has_category(gk1, general)
    
    gk2 = add_question('Who was the father of Ham, Shem and Japheth in the bible?', 'Noah', squiz)
    add_question_has_category(gk2, general)
    
    gk3 = add_question('What name is given to a cross fruit of tangerines and grapefruits?', 'Ugli Fruit', squiz)
    add_question_has_category(gk3, general)
    
    # create rounds
    sb_round = add_round('Spongebob', squiz)
    sp_round = add_round('Sport', squiz)
    gk_round = add_round('General Knowledge', squiz)
    
    # create quizzes
    all_rounds = add_quiz('Big Quiz', squiz)
    sponge_sport = add_quiz('Spongbob Sportspants', squiz)
    
    # quizzes in roudns
    add_question_in_round(sb_round, sb1, 0)
    add_question_in_round(sb_round, sb2, 1)
    add_question_in_round(sb_round, sb3, 2)
    
    add_question_in_round(sp_round, sp1, 0)
    add_question_in_round(sp_round, sp2, 1)
    add_question_in_round(sp_round, sp3, 2)
    
    add_question_in_round(gk_round, gk1, 0)
    add_question_in_round(gk_round, gk2, 1)
    add_question_in_round(gk_round, gk3, 2)    
    
    # rounds in quizzes
    add_round_in_quiz(all_rounds, sb_round, 0)
    add_round_in_quiz(all_rounds, sp_round, 1)
    add_round_in_quiz(all_rounds, gk_round, 2)
    
    add_round_in_quiz(sponge_sport, sb_round, 0)
    add_round_in_quiz(sponge_sport, sp_round, 1)
    
    # time for quiz
    sat = add_Quiz_Time('Saturday')
    sun = add_Quiz_Time('Sunday')
    mon = add_Quiz_Time('Monday')
    tue = add_Quiz_Time('Tuesday')
    wed = add_Quiz_Time('Wednesday')
    thu = add_Quiz_Time('Thursday')
    fri = add_Quiz_Time('Friday')
    
    # venue for quiz
    add_Venue('Tennants', 55.8814512, -4.3187813, squiz, thu)
    add_Venue('Bunker', 55.863779, -4.2643217, squiz, fri)


# add methods
def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c
    
def add_question(q, a, host):
    print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    question = Question.objects.get_or_create(question = q, answer = a, creator=host)[0]
    return question
    
def add_round(name, host):
    r = Round.objects.get_or_create(name=name, creator = host)[0]   
    return r
    
def add_quiz(name, host):
    q = Quiz.objects.get_or_create(name=name, creator = host)[0]   
    return q
    
def add_round_in_quiz(quiz, this_round, num):
    riq = RoundInQuiz.objects.get_or_create(this_quiz=quiz, this_round=this_round, number=num)[0]
    return riq
    
def add_question_in_round(this_round, question, num):
    qir = QuestionInRound.objects.get_or_create(this_round=this_round, this_question=question, number=num)[0]
    return qir
    
def add_question_has_category(question, cat):
    qas = QuestionHasCategory.objects.get_or_create(this_question = question, this_category = cat)[0]
    return qas
    
def add_Host(username, url):
    user = User.objects.get_or_create(username=username)[0]
    user.set_password(username)
    user.save()
    host = Host.objects.get_or_create(url=url, user=user)[0]
    return host    
    
def add_Venue(name, lat, lon, host, time):
    venue = Venue.objects.get_or_create(name=name, lon=lon, lat=lat, time=time, host=host)[0]
    return venue
    
def add_Quiz_Time(day):
    qt = QuizTime.objects.get_or_create(day=day, time=datetime.now())[0]
    return qt    
    

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()
