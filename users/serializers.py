from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('mobile_number','address','email')

