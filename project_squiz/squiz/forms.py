__author__ = '2027822d'
from django import forms
from models import Host, User


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





