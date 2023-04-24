from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.db.models import Q
from .models import Post, Comment, Vote
from .forms import PostForm, CommentForm

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
    return render(render, 'posts/post_list.html')