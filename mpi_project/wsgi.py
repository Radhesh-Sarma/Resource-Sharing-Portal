"""
WSGI config for mpi_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
htt
ps://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mpi_project.settings')

application = get_wsgi_application()
