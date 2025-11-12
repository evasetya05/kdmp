from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db.models import Count
from .models import Dusun, RW, RT

class AdminDaerahDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_daerah/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get counts for each model
        context['dusun_count'] = Dusun.objects.count()
        context['rw_count'] = RW.objects.count()
        context['rt_count'] = RT.objects.count()
        
        # Get recent entries (increased from 5 to 10)
        context['recent_dusun'] = Dusun.objects.all().order_by('-created_at')[:10]
        context['recent_rw'] = RW.objects.select_related('dusun').order_by('-created_at')[:10]
        context['recent_rt'] = RT.objects.select_related('rw', 'rw__dusun').order_by('-created_at')[:10]
        
        return context
