from django.contrib import admin
from models import *

admin.site.register(Question)
admin.site.register(Round)
admin.site.register(Quiz)
admin.site.register(QuestionInRound)
admin.site.register(RoundInQuiz)
admin.site.register(Category)
admin.site.register(QuestionHasCategory)
admin.site.register(RoundHasCategory)
admin.site.register(Player)
admin.site.register(Venue)
admin.site.register(QuizInstance)
admin.site.register(QuizTime)
admin.site.register(Host)
