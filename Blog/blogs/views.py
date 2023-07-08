from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from blogs.models import BlogPost
from blogs.forms import PostForm
# Create your views here.
def index(request):
    return render(request, 'blogs/index.html')
def posts(request):
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)
def post(request,post_id):
    post = BlogPost.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post.html', context)
def edit_post(request,post_id):
    post = BlogPost.objects.get(id=post_id)
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:post',args=[post.id]))
    context = {'post':post,'form':form}
    return render(request,'blogs/edit_post.html',context)

def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:posts'))
    context = {'form':form}
    return render(request,'blogs/new_post.html',context)
