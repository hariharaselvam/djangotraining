from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.views import View

from .forms import ProductForm
from .models import Product
# Create your views here.

def hello_world(request):
	if request.method == 'GET':
		print dir(request)
		value = request.GET.get('value',None)
		return render(
			request, 
			'hello_world.html',
			{
				'value_inside_template':value
			}
		)
	#return HttpResponse("Hello, World!")

def list_products(request):
	if request.method == 'GET':
		products = Product.objects.all()
		form = ProductForm()
		return render(
			request, 
			'product_list.html',
			{
				'product_list':products,
				'product_form':form
			}
		)

	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			product = form.save()
			return redirect('list_products')
			#return HttpResponse("Created Product!")


class HelloWorld(View):
	def get(self, request):
		value = request.GET.get('value',None)
		return render(
			request, 
			'hello_world.html',
			{
				'value_inside_template':value
			}
		)
