from django.urls import path
from . import views
from blogs.views import BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView, EditListView, login, loginfunc
urlpatterns = [
    path('list/', BlogListView.as_view(), name='blog-list'),
    path('detail/<slug:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('update/<slug:pk>/', BlogUpdateView.as_view(), name='blog-update'),
    path('login/', loginfunc, name='login'),
    path('update/', EditListView.as_view(), name='edit-list'),
    path('', views.index, name='index'),
]