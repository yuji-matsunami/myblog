from django.contrib.messages.api import success, warning
from django.forms import widgets
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.base import TemplateView
from blogs.models import Blog
from django.utils import timezone
from django.contrib import messages
from markdownx.widgets import MarkdownxWidget
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

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

class BlogListView(ListView):
    model = Blog
    template_name = "blogs/list.html"

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        context['title'] = Blog.title
        context['published'] = Blog.published
        context['count'] = Blog.objects.all().count()
        return context

class EditListView(ListView):
    model = Blog
    template_name = "blogs/edit_list.html"

    # データベースの値を取得してフロントに送る
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Blog.title # titleを入れる
        return context

class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    fields = ['title', 'blog_text', 'url']
    widgets = {
        'blog_text': MarkdownxWidget(),
    }
    template_name = "blogs/create.html"
    success_url = reverse_lazy('blog-list')
    def form_valid(self, form):
        # 成功したとき
        messages.success(self.request, "保存しました")
        return super().form_valid(form)
    def form_invalid(self, form):
        # 失敗したとき
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ['title', 'blog_text', 'url']
    widgets = {
        'blog_text': MarkdownxWidget(),
    }
    template_name = "blogs/update.html"
    success_url = reverse_lazy('blog-list') # ページ遷移（listのページ）に移動させる
    # 成功したとき
    def form_valid(self, form) -> HttpResponse:
        messages.success(self.request, "保存しました")
        return super().form_valid(form)
    # 失敗したとき
    def form_invalid(self, form) -> HttpResponse:
        messages.warning(self.request, "保存出来ませんでした")
        return super().form_invalid(form)

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog-create')
        else:
            return render(request, 'blogs/login.html', {'context': 'ログインできません'})
    return render(request, 'blogs/login.html', {})

