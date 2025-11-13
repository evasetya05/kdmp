import os
import sys

# Pastikan Python tahu di mana proyek kamu
sys.path.append('/home/teknusas/kdmpsumberoto')
sys.path.append('/home/teknusas/kdmpsumberoto/kdmp')

# Gunakan production settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'kdmp.settings.production'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
