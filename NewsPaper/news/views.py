from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category
from datetime import datetime
from .filters import PostFilter
from django.shortcuts import render
from .forms import  PostForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail

# Create your views here.


class PostList(LoginRequiredMixin,ListView):
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

class DetailPost(LoginRequiredMixin,DetailView):
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




class PostCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.add_post',
                           'news.change_post',)

    def form_valid(self, form):
        if 'nw/create/' in self.request.path:
            post = form.save(commit=False)
            post.rulobject = 'NW'
        else:
            post = form.save(commit=False)
            post.rulobject = 'AR'

        return super().form_valid(form)




class PostUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.add_post',
                           'news.change_post',)

    def form_valid(self, form):
        if f'nw/{self.pk}/update/' in self.request.path:
            post = form.save(commit=False)
            post.rulobject = 'NW'
        else:
            post = form.save(commit=False)
            post.rulobject = 'AR'

        return super().form_valid(form)


class PostDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_detail')
    permission_required = ('news.add_post',
                           'news.change_post',)


class BaseRegistrForm(UserCreationForm):
    name = forms.CharField(label='Имя')
    email = forms.EmailField(label='email')
    class Meta:
        model = User
        fields =(
           'username',
           'email',
            'password1',
            'password2',
        )
class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_auther'] = not self.request.user.groups.filter(name ='authors').exists()
        return context

@login_required
def upgrade_me(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)
    return redirect('/')

def subsribe_me(request):
    user = request.user
    page_catygory = request.GET('postcategory')
    #subscribers_catygory = Category.subscribers.filter(name=page_catygory).all()
    if page_catygory != None:
        catygory_objects = Category.objects.get(name=page_catygory)
        catygory_objects.subscribers.add(user)

