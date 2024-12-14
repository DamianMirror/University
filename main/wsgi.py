import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application

settings_module = "main.deployment" if 'WEBSITE_HOSTNAME' in os.environ else 'main.settings'

print(f'Using settings module: {settings_module}')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
