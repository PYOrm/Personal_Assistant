from django.urls import path
from . import views

app_name = "contacts"  # Простір імен для вашого додатка

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('<int:pk>/', views.contact_detail, name='contact_detail'),
    path('create/', views.contact_create, name='contact_create'),
    path('<int:pk>/edit/', views.contact_update, name='contact_update'),
    path('<int:pk>/delete/', views.contact_delete, name='contact_delete'),
    path('upcoming-birthdays/<int:days>/', views.upcoming_birthdays, name='upcoming_birthdays'),

]
