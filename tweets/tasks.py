from celery import task
import json
import datetime
from twython import Twython
from .models import *

@task
def add(x,y):
	return (x+y)

@task
def get_tweets(hashtag):
	tw = Twython(
				"yJ9GXtYiLH2yMXukUijR6R3dH",
				"Ad8ZMpJNZvYe1CulUDUHPJiw1lg9pgalcLSFdWUQQRemP7jKhz",
				"239795044-XqQ5P6tYWIZJip5EaWWO2Q8mPVwJVZ6hWJ4N9pEO",
				"uC9cjPyNtUPg1ekJvWZCCMwtLojpFA7d6dyzoMAyfIlQQ"

			)
	tweets = tw.search(q=hashtag,count=100)
	statuses = tweets['statuses']
	for status in statuses:
		text = status['text']
		created_at = datetime.datetime.strptime(
			status['created_at'], '%a %b %d %H:%M:%S +0000 %Y'
		)
		user = status['user']['screen_name']
		a,created = Account.objects.get_or_create(name=user)
		Status.objects.get_or_create(text=text,created_at=created_at,user=a)
		#Status.objects.create(text=text,user=user,created_at=created_at)
	print tweets

	return tweets
