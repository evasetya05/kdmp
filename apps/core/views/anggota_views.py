from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.core.models.anggota import AnggotaKoperasi

class AnggotaListView(LoginRequiredMixin, ListView):
    model = AnggotaKoperasi
    template_name = 'anggota/anggota.html'
    context_object_name = 'anggota_list'
    paginate_by = 20

    def get_queryset(self):
        return AnggotaKoperasi.objects.all().order_by('-tanggal_daftar')
