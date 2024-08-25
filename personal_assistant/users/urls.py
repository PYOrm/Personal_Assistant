
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path('/login', auth_views.LoginView.as_view(template_name="login.html", next_page="news:index"), name="login"),
]
