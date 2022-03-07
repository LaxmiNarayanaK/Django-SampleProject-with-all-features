from django.urls import path,include

from . import views

urlpatterns = [
    path("", views.scrap_list.as_view()),
    path("hi", views.scrap_detail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    # path("cmlt",views.cmlt,name="cmlt"),
    path("download",views.download,name="download")
]