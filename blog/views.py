from django.shortcuts import render
from .models import Task
from .forms import PostForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from ipware import get_client_ip
import datetime
# Create your views here.


def home(request):
    print(request.user_agent.browser)
    print(request.user_agent.os)
    return redirect('home')


@login_required
def task_list(request):
    print(request.user_agent.browser)
    print(request.user_agent.os)
    if request.method == "POST":
        me = get_user_model().objects.get(username=request.user.get_username())
        form = Task(author=me, content=request.POST['content'])
        form.save()
        return redirect('task_list')
    else:
        tasks = Task.objects.filter().order_by('date_created')
        return render(request, 'blog/task_list.html', {'tasks': tasks})

@login_required
def remove(request,item_id):
	try:	
		form = Task.objects.get(id = item_id)
	except Task.DoesNotExist:
		form  = None
	form.delete()

	return redirect('task_list')

