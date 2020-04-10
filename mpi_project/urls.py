from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('blog.urls')),
   	path('', include('pages.urls')),
    url(r'^tinymce/', include('tinymce.urls')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
