from django.shortcuts import render
from django.http import HttpResponse

# view for the homepage
def index(request):
	return HttpResponse('Homepage')
	
# view for other page
def about(request):
    return HttpResponse('Squid Logistics')
