from django.urls import path
from . import views
from django.contrib import admin

# URLConf
urlpatterns = [
    path('', views.get_data),
    path('get_data/', views.get_data),
    path('input/', views.input),
    path('results/', views.results),
    path("admin/", admin.site.urls)
]