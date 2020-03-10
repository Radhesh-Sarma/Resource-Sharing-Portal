from django import forms
from .models import Task
from captcha.fields import ReCaptchaField
from tinymce.widgets import TinyMCE
class PostForm(forms.ModelForm): 
	captcha = ReCaptchaField()
	content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
	class Meta:
		model = Task
		fields = ('content','resource_type')