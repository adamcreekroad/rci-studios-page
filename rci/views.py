from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from instagram.client import InstagramAPI
import json
import urllib2

def home(request):
	json_ig_feed = urllib2.urlopen("https://www.instagram.com/rci_studios/media/").read()
	ig_posts = json.loads(json_ig_feed)['items'][:3]
	return render_to_response('home.html', {'page': 'home', 'ig_posts': ig_posts})

def about(request):
	return render_to_response('about.html', {'page': 'about'})

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
	return render_to_response('clients.html', {'page': 'clients','clients': zip(index, clients, genres)})
