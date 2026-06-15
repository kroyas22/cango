from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import RegisterForm, PostForm


def home(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'home.html', {
        'posts': posts
    })


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'post_detail.html', {
        'post': post
    })


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')

    else:

        form = RegisterForm()

    return render(
        request,
        'register.html',
        {
            'form': form
        }
    )


@login_required
def profile(request):

    posts = Post.objects.filter(
        author=request.user
    ).order_by('-created_at')

    return render(
        request,
        'profile.html',
        {
            'posts': posts
        }
    )


@login_required
def create_post(request):

    if request.method == 'POST':

        form = PostForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('profile')

    else:

        form = PostForm()

    return render(
        request,
        'create_post.html',
        {
            'form': form
        }
    )


@login_required
def edit_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return redirect('/')

    if request.method == 'POST':

        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():

            form.save()

            return redirect('profile')

    else:

        form = PostForm(instance=post)

    return render(
        request,
        'edit_post.html',
        {
            'form': form
        }
    )


@login_required
def delete_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if post.author == request.user:
        post.delete()

    return redirect('profile')