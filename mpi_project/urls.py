from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from schema_graph.views import Schema
from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('blog.urls')),
    path('', include('users.urls')),
   	path('', include('pages.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    path("schema/", Schema.as_view()),
    url(r"^account/", include("account_post.urls")),
    url(r"^", include("postman.urls", namespace="postman")),
    url(r'^$', TemplateView.as_view(template_name="site_base.html"), name="home"),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
