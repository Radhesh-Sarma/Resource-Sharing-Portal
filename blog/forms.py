from django import forms
from .models import Task
from captcha.fields import ReCaptchaField
class PostForm(forms.ModelForm): 
	captcha = ReCaptchaField()
	class Meta:
		model = Task
		fields = ('content','resource_type')