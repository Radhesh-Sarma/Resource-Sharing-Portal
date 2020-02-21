from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from captcha.fields import CaptchaField
class CustomUserCreationForm(UserCreationForm):
	captcha = CaptchaField()
	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('email', 'username','mobile_number','address')

class CustomUserChangeForm(UserChangeForm):
	captcha = CaptchaField()
	class Meta:
		model = CustomUser
		fields = ('email', 'username','mobile_number','address')