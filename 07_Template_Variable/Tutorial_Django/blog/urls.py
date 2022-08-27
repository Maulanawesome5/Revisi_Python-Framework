from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="blog"),
    path('news/', views.news, name="news"),
    path('cerita/', views.cerita, name="cerita"),
]
