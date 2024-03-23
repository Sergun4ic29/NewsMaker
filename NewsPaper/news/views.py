from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
from datetime import datetime
# Create your views here.
class PostList(ListView):
    model = Post
    ordering = 'date'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

class DetailPost(DetailView):
    model = Post
    template_name = 'flatpages/new.html'
    context_object_name = 'new'
