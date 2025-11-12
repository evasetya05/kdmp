from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required

# Import views
from apps.core.views.index_views import index as dashboard_index
from apps.core.views.landing_views import LandingPageView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Authentication
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include(('apps.accounts.urls', 'accounts'), namespace='accounts')),
    path('users/', include(('apps.users.urls', 'users'), namespace='users')),
    
    # Main pages
    path('', LandingPageView.as_view(), name='landing-page'),
    path('dashboard/', login_required(dashboard_index), name='dashboard'),
    
    # Third-party apps
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    # Local apps
    path('ledger/', include(('ledger.urls', 'ledger'), namespace='ledger')),
    path('admin-daerah/', include(('apps.modules.admin_daerah.urls', 'admin_daerah'), namespace='admin_daerah')),
]

# Serve media files in development
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
