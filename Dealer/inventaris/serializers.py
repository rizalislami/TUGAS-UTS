from rest_framework import serializers
from .models import inventaris


class inventarisSerializer(serializers.ModelSerializer):
    class Meta:
        model = inventaris
        fields = ['harga', 'pembelian', 'peringatan',]