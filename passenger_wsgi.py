import os
import sys

# Add the project directory to the Python path
project_home = '/home/teknusas/kdmpsumberoto'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Add the kdmp directory to the Python path
project_app = '/home/teknusas/kdmpsumberoto/kdmp'
if project_app not in sys.path:
    sys.path.insert(0, project_app)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'kdmp.settings.production'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()