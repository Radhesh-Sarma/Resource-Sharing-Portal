from rest_framework import serializers
from .models import Task

class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('content')
