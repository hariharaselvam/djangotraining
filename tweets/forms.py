from django import forms
from .models import Twitter

class TwitterForm(forms.ModelForm):
	class Meta:
		model = Twitter
		fields = ('tweet','hashtag','account')