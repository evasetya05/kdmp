import os
import sys

# Pastikan Python tahu di mana proyek kamu
sys.path.append('/home/teknusas/kdmpsumberoto')
sys.path.append('/home/teknusas/kdmpsumberoto/kdmp')

# Paksa Django untuk pakai settings dari kdmp
os.environ['DJANGO_SETTINGS_MODULE'] = 'kdmp.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
