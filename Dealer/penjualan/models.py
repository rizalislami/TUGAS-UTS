from django.db import models

class penjualan(models.Model):
    pelanggan = models.CharField(max_length=255)
    penjualan = models.TextField()
    laporan = models.DecimalField(max_digits=10, decimal_places=2)
