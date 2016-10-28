from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import TwitterForm
from .models import *
from .tasks import get_tweets
#from twython import Twython

# Create your views here.

def twitter_view(request):
	if request.method == 'GET':
		form = TwitterForm()
		return render(
			request, 
			'tweets.html',
			{
				
				'twitter_form':form
			}
		)

	if request.method == 'POST':
		form = TwitterForm(request.POST)
		if form.is_valid():
			hashtag=form.cleaned_data['hashtag']
			hashtag= "hariharaselvam"
			tweets = get_tweets.delay(hashtag)
			#product = form.save()
			#tw = Twython(
			#	"yJ9GXtYiLH2yMXukUijR6R3dH",
			#	"Ad8ZMpJNZvYe1CulUDUHPJiw1lg9pgalcLSFdWUQQRemP7jKhz",
			#	"239795044-XqQ5P6tYWIZJip5EaWWO2Q8mPVwJVZ6hWJ4N9pEO",
			#	"uC9cjPyNtUPg1ekJvWZCCMwtLojpFA7d6dyzoMAyfIlQQ"

			#)
			
			#tweets = tw.search(q=hashtag,count=10)
			print tweets
			return redirect('timeline_view')
			#return HttpResponse(tweets)

def timeline_view(request):
	if request.method == 'GET':
		statuses = Status.objects.all()
		return render(
			request, 
			'timeline.html',
			{
				
				'status_list':statuses
			}
		)