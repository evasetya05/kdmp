from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .models import Dusun, RW, RT

# Dusun Views
class DusunListView(ListView):
    model = Dusun
    template_name = 'admin_daerah/dusun_list.html'
    context_object_name = 'dusun_list'

class DusunCreateView(CreateView):
    model = Dusun
    fields = ['nama', 'keterangan']
    template_name = 'admin_daerah/dusun_form.html'
    success_url = reverse_lazy('admin_daerah:dusun_list')
    
    def form_valid(self, form):
        messages.success(self.request, _('Dusun berhasil ditambahkan'))
        return super().form_valid(form)

class DusunUpdateView(UpdateView):
    model = Dusun
    fields = ['nama', 'keterangan']
    template_name = 'admin_daerah/dusun_form.html'
    success_url = reverse_lazy('admin_daerah:dusun_list')
    
    def form_valid(self, form):
        messages.success(self.request, _('Dusun berhasil diperbarui'))
        return super().form_valid(form)

class DusunDeleteView(DeleteView):
    model = Dusun
    template_name = 'admin_daerah/dusun_confirm_delete.html'
    success_url = reverse_lazy('admin_daerah:dusun_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Dusun berhasil dihapus'))
        return super().delete(request, *args, **kwargs)

# RW Views
class RWListView(ListView):
    model = RW
    template_name = 'admin_daerah/rw_list.html'
    context_object_name = 'rw_list'
    
    def get_queryset(self):
        return RW.objects.select_related('dusun').order_by('dusun__nama', 'nomor')

class RWCreateView(CreateView):
    model = RW
    fields = ['dusun', 'nomor']
    template_name = 'admin_daerah/rw_form.html'
    success_url = reverse_lazy('admin_daerah:rw_list')
    
    def form_valid(self, form):
        messages.success(self.request, _('Data RW berhasil ditambahkan'))
        return super().form_valid(form)

class RWUpdateView(UpdateView):
    model = RW
    fields = ['dusun', 'nomor']
    template_name = 'admin_daerah/rw_form.html'
    success_url = reverse_lazy('admin_daerah:rw_list')
    
    def form_valid(self, form):
        messages.success(self.request, _('Data RW berhasil diperbarui'))
        return super().form_valid(form)

class RWDeleteView(DeleteView):
    model = RW
    template_name = 'admin_daerah/rw_confirm_delete.html'
    success_url = reverse_lazy('admin_daerah:rw_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Data RW berhasil dihapus'))
        return super().delete(request, *args, **kwargs)

# RT Views
class RTListView(ListView):
    model = RT
    template_name = 'admin_daerah/rt_list.html'
    context_object_name = 'rt_list'
    
    def get_queryset(self):
        return RT.objects.select_related('rw__dusun', 'rw').order_by('rw__dusun__nama', 'rw__nomor', 'nomor')

class RTCreateView(CreateView):
    model = RT
    fields = ['rw', 'nomor']
    template_name = 'admin_daerah/rt_form.html'
    success_url = reverse_lazy('admin_daerah:rt_list')
    
    def form_valid(self, form):
        messages.success(self.request, _('Data RT berhasil ditambahkan'))
        return super().form_valid(form)

class RTUpdateView(UpdateView):
    model = RT
    fields = ['rw', 'nomor']
    template_name = 'admin_daerah/rt_form.html'
    success_url = reverse_lazy('admin_daerah:rt_list')
    
    def form_valid(self, form):
        messages.success(self.request, _('Data RT berhasil diperbarui'))
        return super().form_valid(form)

class RTDeleteView(DeleteView):
    model = RT
    template_name = 'admin_daerah/rt_confirm_delete.html'
    success_url = reverse_lazy('admin_daerah:rt_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Data RT berhasil dihapus'))
        return super().delete(request, *args, **kwargs)
