from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from .modles import Post


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    
class PostDetailView(DetailView):
        template_name = "posts/detail.html"
        model = Post
        
class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "author", "body"]


# Create your views here.
