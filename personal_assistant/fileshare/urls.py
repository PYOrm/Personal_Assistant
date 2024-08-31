from django.urls import path
from . import views

app_name = 'fileshare'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('download/<int:file_id>/', views.download, name='download'),
    path('delete/<int:file_id>/', views.delete, name='delete'),
]
