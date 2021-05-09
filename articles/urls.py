from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.article_list),
    path('<slug:slug>/', views.article_detail)
]
