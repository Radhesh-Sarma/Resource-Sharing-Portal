from django import forms
from .models import Task
from captcha.fields import CaptchaField
class PostForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = Task
		fields = ('content','resource_type')