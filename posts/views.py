from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Posts, Comment
from .choices import rating_choices, category_choices, postcriteria_choices
from . import forms

# Create your views here.


def index(request):
    # return HttpResponse('hello from posts')

    posts = Posts.objects.order_by('-created_at')
    postd = Posts.objects.order_by('-created_at')
    if request.method =="POST":
        query = request.POST['q']
        if query:
            posts = Posts.objects.filter(title__icontains=query)
            postd = Posts.objects.filter(body__icontains=query)


    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'title': 'Recent Posts',
        'rating_choices': rating_choices,
        'category_choices': category_choices,
        'postcriteria_choices': postcriteria_choices,
        'posts': paged_posts,
        'postd':postd
    }

    return render(request, 'posts/index.html', context)


def archives(request):

    posts = Posts.objects.order_by('-created_at')

    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'title': 'Recent Posts',
        'posts': paged_posts
    }

    return render(request, 'posts/archives.html', context)


def details(request, id):
    post = Posts.objects.get(id=id)
    print(post)
    comments = post.comments.all()

    # For Comment Form
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect("login")
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            # save to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.post = post
            instance.save()
            return redirect("details", id=post.id)

    form = forms.CommentForm()

    context = {
        'post': post,
        'form': form,
        'comments': comments
    }

    return render(request, 'posts/details.html', context)


@login_required(login_url="login")
def create(request):
    if request.method == 'POST':
        # request.files for image
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('index')

    else:
        form = forms.CreatePost()
        context = {
            'form': form
        }
        return render(request, 'posts/create.html', context)


def search(request):
    return render(request, 'posts/search.html')
