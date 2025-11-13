import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# Add the apps directory to the Python path
BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = os.path.join(BASE_DIR, 'apps')
if APPS_DIR not in sys.path:
    sys.path.append(APPS_DIR)

# Deteksi apakah server sedang dijalankan via LiteSpeed
server_software = os.getenv('SERVER_SOFTWARE', '').lower()

# Tentukan settings module berdasarkan environment
if 'litespeed' in server_software or 'lsws' in server_software:
    settings_module = 'kdmp.settings.production'
else:
    settings_module = 'kdmp.settings.development'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
