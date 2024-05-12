from django.db import models

class inventaris(models.Model):
    harga = models.CharField(max_length=25)
    pembelian = models. TextField()
    peringatan = models. DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.harga
