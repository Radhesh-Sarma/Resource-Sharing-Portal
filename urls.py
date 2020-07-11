from django.urls import path
from . import views
urlpatterns = [
    path('users/', views.SnippetList.as_view()),
    path('users/<int:pk>/', views.SnippetDetail.as_view()),
]

from rest_framework.urlpatterns import format_suffix_patterns


