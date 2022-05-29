from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog/<slug:slug>/', views.post_detail_view, name='post_detail'),
    path('category/', views.category_list, name='category_list'),
    path('category/<slug:slug>/', views.category_post_list, name='category_post_list'),
]