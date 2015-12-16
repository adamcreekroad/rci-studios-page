from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import json

def home(request):
	return render_to_response('home.html', {'page': 'home'})

def about(request):
	return render_to_response('about.html', {'page': 'about'})
