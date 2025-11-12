from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView




from django.contrib.auth.decorators import login_required
from apps.core.views.index_views import index as dashboard_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include(("apps.accounts.urls", "accounts"), namespace="accounts")),
    path("", login_required(dashboard_index), name="home"),  # root URL points to dashboard
    path('dashboard/', login_required(dashboard_index), name="dashboard"),  # dashboard URL also points to the same view
    
    # Third-party apps
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    # Local apps with namespaces
    path('post_media/', include(('post_media.urls', 'post_media'), namespace='post_media')),
    path('ledger/', include(('ledger.urls', 'ledger'), namespace='ledger')),
    path('leads/', include(('leads.urls', 'leads'), namespace='leads')),
    path('lean/', include(('lean.urls', 'lean'), namespace='lean')),
]
