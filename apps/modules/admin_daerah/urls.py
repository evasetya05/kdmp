from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views_dashboard import AdminDaerahDashboardView

app_name = 'admin_daerah'

urlpatterns = [
    # Dashboard
    path('', login_required(AdminDaerahDashboardView.as_view()), name='dashboard'),
    
    # Dusun URLs
    path('dusun/', login_required(views.DusunListView.as_view()), name='dusun_list'),
    path('dusun/tambah/', login_required(views.DusunCreateView.as_view()), name='dusun_create'),
    path('dusun/<int:pk>/edit/', login_required(views.DusunUpdateView.as_view()), name='dusun_update'),
    path('dusun/<int:pk>/hapus/', login_required(views.DusunDeleteView.as_view()), name='dusun_delete'),
    
    # RW URLs
    path('rw/', login_required(views.RWListView.as_view()), name='rw_list'),
    path('rw/tambah/', login_required(views.RWCreateView.as_view()), name='rw_create'),
    path('rw/<int:pk>/edit/', login_required(views.RWUpdateView.as_view()), name='rw_update'),
    path('rw/<int:pk>/hapus/', login_required(views.RWDeleteView.as_view()), name='rw_delete'),
    
    # RT URLs
    path('rt/', login_required(views.RTListView.as_view()), name='rt_list'),
    path('rt/tambah/', login_required(views.RTCreateView.as_view()), name='rt_create'),
    path('rt/<int:pk>/edit/', login_required(views.RTUpdateView.as_view()), name='rt_update'),
    path('rt/<int:pk>/hapus/', login_required(views.RTDeleteView.as_view()), name='rt_delete'),
]
