from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.blog_list, name='blog'),
	path('search/', views.search, name='blog_search'),
	path('comment/', views.commentView, name="comment"),
	path('blog_detail/<str:url>/', views.blog_detail, name='blog_detail'),
]
