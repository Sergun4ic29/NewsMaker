from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from datetime import datetime
from .filters import PostFilter
from django.shortcuts import render
from .forms import  PostForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

class PostList(ListView):
    model = Post
    ordering = 'date'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

class DetailPost(DetailView):
    model = Post
    template_name = 'flatpages/new.html'
    context_object_name = 'new'

def create_post(request,form):
    form = PostForm()
    if request.method =='POST':
        form = PostForm(request.POST)
        #if 'nw/create/' in request.path:
            #post = form.save(commit=False)
            #post.rulobject = 'NW'
            #return super().form_valid(form)
        #else:
            #post = form.save(commit=False)
           # post.rulobject = 'AR'
            #return super().form_valid(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/news/')

    return render(request,'post_edit.html',{'form':form})




class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        if 'nw/create/' in self.request.path:
            post = form.save(commit=False)
            post.rulobject = 'NW'
        else:
            post = form.save(commit=False)
            post.rulobject = 'AR'

        return super().form_valid(form)




class PostUpdate(UpdateView,LoginRequiredMixin):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


    def form_valid(self, form):
        if f'nw/{self.pk}/update/' in self.request.path:
            post = form.save(commit=False)
            post.rulobject = 'NW'
        else:
            post = form.save(commit=False)
            post.rulobject = 'AR'

        return super().form_valid(form)


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_detail')