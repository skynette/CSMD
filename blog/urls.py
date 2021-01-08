from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.blog_list, name='blog'),
	path('single/', views.blog_detail, name='blog_detail'),
	path('search/', views.search, name='blog_search'),
]
