from django.urls import path
from inventaris import views

urlpatterns = [
    path('inventaris/', views.inventaris_list),
]