"""
WSGI config for receivetion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'receivetion.settings')

<<<<<<< HEAD
application = get_wsgi_application()
WSGI_APPLICATION = 'receivetion.wsgi.application'



=======
application = get_wsgi_application()
>>>>>>> 3f4274d (fixed settings and wsgi)
