from django.urls import path
from . import views
urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.task_list, name='task_list'),
    path('task_list/', views.task_list, name='task_list'),
    path('remove/<int:item_id>/', views.remove), 
    path('home/', views.home,name ='home'),
]