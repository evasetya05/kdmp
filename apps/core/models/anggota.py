from django.db import models

class AnggotaKoperasi(models.Model):
    JENIS_KELAMIN = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]
    STATUS = [
        ('pending', 'Pending'),
        ('verified', 'Verified'),
    ]

    nik = models.CharField(max_length=16, unique=True)
    nama_lengkap = models.CharField(max_length=200)
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN)
    email = models.EmailField()
    no_hp = models.CharField(max_length=20)
    rt = models.CharField(max_length=5)

    tanggal_daftar = models.DateTimeField(auto_now_add=True)
    status_verifikasi = models.CharField(max_length=10, choices=STATUS, default='pending')

    def __str__(self):
        return f"{self.nama_lengkap} ({self.nik})"
