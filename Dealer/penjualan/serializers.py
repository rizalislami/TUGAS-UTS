from rest_framework import serializers
from .models import penjualan


class PenjualanSerializer(serializers.ModelSerializer):
    class Meta:
        model = penjualan
        fields = ['pelanggan', 'penjualan', 'laporan',]