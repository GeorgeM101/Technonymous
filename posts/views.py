from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.db.models import Q
from .models import Post, Comment, Vote
from .forms import CommentForm, PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    query = request.GET.get('q')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__username__icontains=query)
        ).distinct()
    context = {'posts': posts}
    return render(request, 'posts/post_list.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment was posted successfully.')
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()
    context = {'post': post, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'posts/post_detail.html', context)

@login_required
def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post was created successfully.')
            return redirect('post_detail', post_id=post.id)
    else:
        post_form = PostForm()
    context = {'post_form': post_form}
    return render(request, 'posts/post_create.html', context)

@login_required
def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        messages.error(request, 'You do not have permission to edit this post.')
        return redirect('post_detail', post_id=post.id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'Your post was updated successfully.')
            return redirect('post_detail', post_id=post.id)
    else:
        post_form = PostForm(instance=post)
    context = {'post': post, 'post_form': post_form}
    return render(request, 'posts/post_update.html', context)

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        messages.error(request, 'You do not have permission to delete this post.')
        return redirect('post_detail', post_id=post.id)
    post.delete()
    messages.success(request, 'Your post was deleted successfully.')
    return redirect('post_list')