from django.urls import path
from . import views
urlpatterns = [
    path('userapi/', views.UserList.as_view()),
    path('userapi/<int:pk>/', views.UserDetail.as_view()),
]

from rest_framework.urlpatterns import format_suffix_patterns

