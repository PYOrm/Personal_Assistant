from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path('', views.contact_list, name='contact_list'),  # Перегляд списку контактів
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),  # Перегляд одного контакту
    path('contact/new/', views.contact_create, name='contact_create'),  # Створення нового контакту
    path('contact/<int:pk>/edit/', views.contact_update, name='contact_update'),  # Редагування контакту
    path('contact/<int:pk>/delete/', views.contact_delete, name='contact_delete'),  # Видалення контакту
]
