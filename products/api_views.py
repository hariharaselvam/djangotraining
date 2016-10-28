from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
import json
User = get_user_model()

class UserViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class CategoryViewSet(ModelViewSet):
	queryset = Category.objects.all().filter(status=1)
	serializer_class = CategorySerializer

	def create(self, request, *args, **kwargs):
		#print request.data
		req_data = json.dumps(request.data)
		req_data = json.loads(req_data)
		print req_data['name']
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		if Stat.objects.exists():
			s = Stat.objects.get()
			s.category_count+=1
			s.save()
		else:
			Stat.objects.create(category_count=1)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
	
		self.perform_destroy(instance)

		s = Stat.objects.get()
		s.category_count-=1
		s.save()

		return Response(status=status.HTTP_201_CREATED)

	#def get_queryset(self):
	#	queryset = self.queryset
	#	queryset = queryset.a

class StatViewSet(ModelViewSet):
	queryset = Stat.objects.all()
	serializer_class = StatSerializer

class ProductViewSet(ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	def create(self, request, *args, **kwargs):
		req_data = json.dumps(request.data)
		req_data = json.loads(req_data)
		cat_name = req_data['category_name']
		#serializer = self.get_serializer(data=request.data)

		#serializer.is_valid(raise_exception=True)
		if len(Category.objects.all().filter(name=cat_name))==0:
			Category.objects.create(name=cat_name)
		
		category = Category.objects.all().filter(name=cat_name)[0]

		Product.objects.create(name=req_data['name'],price=req_data['price'],description=req_data['description'],category=category)
			
		
		#headers = self.get_success_headers(serializer.data)
		return Response(status=status.HTTP_201_CREATED)
