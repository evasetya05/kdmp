from django.db import models
from django.utils.translation import gettext_lazy as _

class Dusun(models.Model):
    """Model untuk data Dusun"""
    nama = models.CharField(_('Nama Dusun'), max_length=100, unique=True)
    keterangan = models.TextField(_('Keterangan'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'admin_daerah'
        verbose_name = _('Dusun')
        verbose_name_plural = _('Daftar Dusun')
        ordering = ['nama']

    def __str__(self):
        return self.nama

class RW(models.Model):
    """Model untuk data RW"""
    nomor = models.PositiveSmallIntegerField(_('Nomor RW'))
    dusun = models.ForeignKey(
        Dusun, 
        on_delete=models.CASCADE, 
        related_name='daftar_rw',
        verbose_name=_('Dusun')
    )
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'admin_daerah'
        verbose_name = _('RW')
        verbose_name_plural = _('Daftar RW')
        ordering = ['dusun', 'nomor']
        unique_together = ['dusun', 'nomor']

    def __str__(self):
        return f"RW {self.nomor} - {self.dusun.nama}"

class RT(models.Model):
    """Model untuk data RT"""
    nomor = models.PositiveSmallIntegerField(_('Nomor RT'))
    rw = models.ForeignKey(
        RW, 
        on_delete=models.CASCADE, 
        related_name='daftar_rt',
        verbose_name=_('RW')
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'admin_daerah'
        verbose_name = _('RT')
        verbose_name_plural = _('Daftar RT')
        ordering = ['rw__dusun', 'rw', 'nomor']
        unique_together = ['rw', 'nomor']

    def __str__(self):
        return f"RT {self.nomor} - RW {self.rw.nomor} - {self.rw.dusun.nama}"

    @property
    def dusun(self):
        return self.rw.dusun