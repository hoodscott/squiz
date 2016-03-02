__author__ = '2027822d'
from django import forms
from models import *


class RegisterHostForm(forms.ModelForm):

    url = forms.URLField(help_text="Enter the url of the pub's website")

    class Meta:
        model = Host
        fields = ('url', )


class RegisterUserForm(forms.ModelForm):

    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.CharField()
    password = forms.CharField()


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')



class QuestionForm(forms.ModelForm):
    
    # question and answer as text
    question = forms.CharField(max_length=128,
                                label = "Question",)
    answer = forms.CharField(max_length=128,
                                label = "Answer",)
    
    # optional image
    image = forms.ImageField(label="Upload Image",
                            required=False,)# can be null
    
    # creator of the question
    creator = forms.IntegerField(widget = forms.HiddenInput(), required=False)
    
    class Meta:
        model = Question
        fields = ('question', 'answer', 'image', 'creator')
        exclude = []
        
class RoundForm(forms.ModelForm):
    
    # question and answer as text
    name = forms.CharField(max_length=128,
                                label = "Round Name",)
    
    # creator of the question
    creator = forms.IntegerField(widget = forms.HiddenInput(), required=False)
    
    class Meta:
        model = Round
        fields = ('name', 'creator')
        exclude = []
        
class QuizForm(forms.ModelForm):
    
    # question and answer as text
    name = forms.CharField(max_length=128,
                                label = "Quiz Name",)
    
    # creator of the question
    creator = forms.IntegerField(widget = forms.HiddenInput(), required=False)
    
    class Meta:
        model = Quiz
        fields = ('name', 'creator')
        exclude = []
    

