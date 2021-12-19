from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from . forms import PostForm
from . models import Post

# Create your views here.

@staff_member_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail_post', id=post.id)
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'post/add_post.html', context)

def detail_post(request, id):
    post = Post.objects.get(id = id)
    context = {'post': post,}
    return render(request, 'post/detail_post.html', context)

@staff_member_required
def edit_post(request, id):
    post = Post.objects.get(id = id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail_post', id=post.id)
    else:
        form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'post/edit_post.html', context)

@staff_member_required
def delete_post(request, id):
    post = Post.objects.get(id = id)
    post.delete()
    return redirect('/')

@staff_member_required
def publish_post(request, id):
    post = Post.objects.get(id = id)
    post.publish()
    return redirect('detail_post', id=post.id)

@staff_member_required
def unpublish_post(request, id):
    post = Post.objects.get(id = id)
    post.unpublish()
    return redirect('unpublished_posts')

@staff_member_required
def unpublished_posts(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    context = {'posts': posts}
    return render(request, 'post/unpublished_posts.html', context)

