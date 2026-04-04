"""
WSGI config for receivetion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import gunicorn
from django.core.wsgi import get_wsgi_application

import receivetion

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'receivetion.settings')

application = get_wsgi_application()
WSGI_APPLICATION = 'receivetion.wsgi.application'


