from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from blogs.models import BlogPost
from blogs.forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def check_post_author(request,post):
    return request.user==post.author

def index(request):
    return render(request, 'blogs/index.html')

def posts(request):
    posts = BlogPost.objects.order_by('date_added').filter(audited=True)
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

def post(request,post_id):
    post = BlogPost.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post.html', context)
@login_required
def edit_post(request,post_id):
    post = BlogPost.objects.get(id=post_id)
    if not check_post_author(request,post):
        raise Http404
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:post',args=[post.id]))
    context = {'post':post,'form':form}
    return render(request,'blogs/edit_post.html',context)
@login_required
def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:posts'))
    context = {'form':form}
    return render(request,'blogs/new_post.html',context)
@login_required
def delete_post(request,post_id):
    post = BlogPost.objects.get(id=post_id)
    if not check_post_author(request,post):
        raise Http404
    else:
        post.delete()
        return HttpResponseRedirect(reverse('blogs:posts'))