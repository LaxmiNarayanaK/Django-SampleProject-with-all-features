from django.urls import path

from . import views

urlpatterns = [
    path("Destination/", views.DestinationList.as_view(),name="Destination"),
    path('Destination/<int:pk>/', views.UserDetail.as_view()),
    path('', views.index),
    path("inner",views.example)

]
