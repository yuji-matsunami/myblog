from django.urls import path
from . import views
from blogs.views import BlogDetailView, BlogListView, BlogCreateView, login, loginfunc
urlpatterns = [
    path('list/', BlogListView.as_view(), name='blog-list'),
    path('<int:pk>/<slug:url>/', BlogDetailView.as_view(), name='blog-detail'),
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('login/', loginfunc, name='login'),
    path('', views.index, name='index'),
]