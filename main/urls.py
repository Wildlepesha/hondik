from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('shop/', views.Show.as_view(), name='shop'),
    path('search/', views.search, name='search'),
    path('create/', views.CreatePost, name='create'),
    path('detail/<slug>', views.ProductDetail.as_view(), name='detail'),
    path('category/<str:cats>', views.CategoryView, name='category'),
]
