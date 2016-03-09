__author__ = '2027822d'
from django import forms
from models import *


class RegisterHostForm(forms.ModelForm):

    url = forms.URLField(help_text="Enter the url of the pub's website")
    
    # add bootstrap class to each field
    def __init__(self, *args, **kwargs):
        super(RegisterHostForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Host
        fields = ('url', )


class RegisterUserForm(forms.ModelForm):

    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    # add bootstrap class to each field
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

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
    
    # add bootstrap class to each field
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
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
    
    # add bootstrap class to each field
    def __init__(self, *args, **kwargs):
        super(RoundForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
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
    
    # add bootstrap class to each field
    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Quiz
        fields = ('name', 'creator')
        exclude = []
        

class LoginForm(forms.Form):

    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
