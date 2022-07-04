from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import BlogPostForm, BlogEditForm
from django.urls import reverse_lazy

# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = BlogPostForm
    template_name = 'add_post.html'
    #fields = ['title', 'author', 'title_tag', 'body']      # Don't need to designate fields since done in BlogPostForm class
    #fields = '__all__'                                     # Will include all fields by default

class UpdatePostView(UpdateView):
    model = Post
    form_class = BlogEditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    #fields = ['title', 'title_tag', 'body']