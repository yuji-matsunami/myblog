from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from blogs.models import Blog

# Create your views here.
def index(request):
    return HttpResponse("Hello, woeld. You're at the polls index.")

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogs/detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Blog.title
        context['blog_text'] = Blog.blog_text
        return context