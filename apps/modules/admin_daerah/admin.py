from django.contrib import admin
from .models import Dusun, RW, RT

@admin.register(Dusun)
class DusunAdmin(admin.ModelAdmin):
    list_display = ('nama', 'created_at', 'updated_at')
    search_fields = ('nama', 'keterangan')
    list_per_page = 20

@admin.register(RW)
class RWAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'dusun', 'created_at')
    list_filter = ('dusun',)
    search_fields = ('nomor',)
    list_per_page = 20

@admin.register(RT)
class RTAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'rw', 'created_at')
    list_filter = ('rw__dusun', 'rw')
    search_fields = ('nomor',)
    list_per_page = 20
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('rw__dusun')
