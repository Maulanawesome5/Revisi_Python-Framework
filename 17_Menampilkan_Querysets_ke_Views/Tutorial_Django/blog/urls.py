from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('jurnal/', views.jurnal, name="jurnal"),
    path('berita/', views.berita, name="berita"),
    path('gosip/', views.gosip, name="gosip"),
]
