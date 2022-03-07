

from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login",views.login, name="login"),
    path("logout",views.logout,name="logout"),
    path("result",views.result,name="result"),
    path("Home",views.Home,name="Home"),
    path("contact",views.contact,name="contact")
    ]

