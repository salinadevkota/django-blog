from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator

from .models import Post, Comment
from .forms import PostForm, CommentForm


# ================= POST LIST =================
def post_list(request):
    search = request.GET.get('search', '')
    posts = Post.objects.filter(title__icontains=search).order_by('-created_at')

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {
        'page_obj': page_obj,
        'search': search
    })


# ================= POST DETAIL + COMMENT =================
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', id=id)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


# ================= CREATE POST =================
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})


# ================= UPDATE POST =================
@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return redirect('post_list')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form})


# ================= DELETE POST =================
@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author == request.user:
        post.delete()

    return redirect('post_list')


# ================= REGISTER =================
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


# ================= LOGIN =================
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('post_list')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


# ================= LOGOUT =================
def logout_view(request):
    logout(request)
    return redirect('post_list')
