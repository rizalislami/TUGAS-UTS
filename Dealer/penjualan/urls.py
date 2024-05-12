from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('penjualan/<int:pk>/', views.penjualan_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)