from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
import json
import urllib2

def login_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	response_data = {}
	if user is not None:
		login(request, user)
		html = render_to_string('navbar.html', {'user': user})
		return HttpResponse(html)
	else:
		response_data = {}
		response_data['result'] = 'Fail'
		response_data['message'] = 'Username and/or password were incorrect.'
		return HttpResponse(json.dumps(response_data), content_type="application/json")

def logout_view(request):
	logout(request)
	response_data = {}
	response_data['result'] = 'Success!'
	response_data['message'] = 'You"re logged out'
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def home(request):
	json_ig_feed = urllib2.urlopen("https://www.instagram.com/rci_studios/media/").read()
	ig_posts = json.loads(json_ig_feed)['items'][:3]
	return render(request, 'home.html', {'page': 'home', 'ig_posts': ig_posts})

def about(request):
	return render(request, 'about.html', {'page': 'about'})

def clients(request):
	index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
	clients = ["So Last Year", "Ice Nine Kills", "Southshore", "Aphasia",
		"Unwill", "Apex", "Ryan Delp", "Adam Simmons", "California Cousins",
		"Divinex", "The Discord", "Skylime", "Sideline", "Misled", "New Mtn",
		"Yeyowolf"
	]
	genres = ["Pop/Rock", "Metalcore", "Metalcore", "Metalcore", "Hardcore",
		"Mathcore", "Singer/Songwriter", "Hip-Hop", "Pop-Punk", "Prog-Metal",
		"Metalcore", "Pop-Punk", "Hardcore", "Hardcore", "Post-Hardcore",
		"Mathcore"
	]
	return render(request, 'clients.html', {'page': 'clients','clients': zip(index, clients, genres)})
