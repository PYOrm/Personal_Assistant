from django.urls import path
from . import views

app_name = 'fileshare'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('download/<str:box_file_id>/', views.download, name='download'),
    path('delete/<str:box_file_id>/', views.delete, name='delete'),
    path('list/', views.file_list, name='file_list'),
    path('update_dev_token', views.update_dev_token)   #remove on production
]
