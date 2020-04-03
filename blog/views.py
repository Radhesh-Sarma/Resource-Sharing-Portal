from django.shortcuts import render
from .models import Task
from .forms import PostForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from ipware import get_client_ip
import datetime
from django.core.mail import send_mail
from mpi_project.settings import EMAIL_HOST_USER
from users.models import CustomUser
# Create your views here.


def home(request):
    print(request.user_agent.browser)
    print(request.user_agent.os)
    return redirect('home')


@login_required
def task_list(request):
    if request.method == "POST":
        me = get_user_model().objects.get(username=request.user.get_username())
        currentDT = datetime.datetime.now()
        usercontent = request.POST.get('content')
        emailcontent = request.user.get_username() + str(" posted ") + str(usercontent) + str(" on ") + str(currentDT)
       # print(emailcontent)
        recipient_list = CustomUser.objects.values_list('email',flat=True)
        #print(recipient_list)
        #send_mail('Post Notification',emailcontent,EMAIL_HOST_USER,['radheshsarma29@gmail.com'])
        form = Task(author=me, content=request.POST.get('content'))
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

