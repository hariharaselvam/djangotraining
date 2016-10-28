from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username','email')

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id','name','status')

class ProductSerializer(serializers.ModelSerializer):
	category_id = serializers.PrimaryKeyRelatedField(
		write_only = True,
		queryset = Category.objects.all(),
		source = 'category'
	)
	category = CategorySerializer(read_only=True)
	class Meta:
		model = Product
		fields = ('id','name','category_id','category')


class StatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Stat
		fields = ('category_count',)

