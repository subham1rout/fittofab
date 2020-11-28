from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


def blog(request):
    content={'posts': Post.objects.all() }
    return render(request,'blog/connectt.html',content)

class PostListView(ListView):
    model=Post
    template_name='blog/connectt.html'
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post
    #automatically search for <app>/<model>_<viewtype>.html i.e. blog/post_detail.html

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
