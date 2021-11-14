from django.urls import path
from . import views
from blogs.views import BlogDetailView, BlogListView
urlpatterns = [
    path('list/', BlogListView.as_view(), name='blog-list'),
    path('<int:pk>/<slug:url>/', BlogDetailView.as_view(), name='blog-detail'),
    path('', views.index, name='index'),
]