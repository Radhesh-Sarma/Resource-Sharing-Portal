from django.urls import path
from . import views
urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.task_list, name='task_list'),
    path('task_list/', views.task_list, name='task_list'),
    path('remove/<int:item_id>/', views.remove), 
    path('home/', views.home,name ='home'),
    path('blog/', views.SnippetList.as_view()),
    path('blog/<int:pk>/', views.SnippetDetail.as_view()),
]

from rest_framework.urlpatterns import format_suffix_patterns

