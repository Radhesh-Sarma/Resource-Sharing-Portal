from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from captcha.fields import ReCaptchaField
from .models import userdata
class CustomUserCreationForm(UserCreationForm):
	captcha = ReCaptchaField()
	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('email', 'username','mobile_number','address')

class CustomUserChangeForm(UserChangeForm):
	captcha = ReCaptchaField()
	class Meta:
		model = CustomUser
		fields = ('email', 'username','mobile_number','address')

class PostForm(forms.ModelForm):
   class Meta:
        model = userdata
        fields = ('name', 'email','content',)  
