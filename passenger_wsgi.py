import os
import sys

# Tambahkan path project agar Python tahu di mana kode Django kamu
sys.path.append('/home/teknusas/kdmpsumberoto')
sys.path.append('/home/teknusas/kdmpsumberoto/kdmp')

# Gunakan environment variable DJANGO_SETTINGS_MODULE dari server
# Kalau tidak ada, fallback ke production (default aman di hosting) coba lagi
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    os.getenv('DJANGO_SETTINGS_MODULE', 'kdmp.settings.production')
)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
