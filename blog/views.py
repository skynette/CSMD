
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from .models import BlogPost, CommentPost
from services.models import Service


# def get_category_count():
# 	# get all posts and grab the categories, the count them
# 	queryset = BlogPost.objects.values(
# 		'categories__title').annotate(Count("categories__title"))
# 	return queryset


# def get_author(user):
# 	qs = Author.objects.filter(user=user)
# 	if qs.exists():
# 		return qs[0]
# 	else:
# 		return None

# Create your views here.

def search(request):
    blogs = BlogPost.objects.all().order_by("-date")
    # Search feature
    query = request.GET.get('q')
    if query:
        blogs = blogs.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(author__user__first_name__icontains=query)
        ).distinct()
    pass


def blog_list(request):
    about = "The Centre for Self Employment and Management Development (CSMD) Company is an indigenous business start up and management development trainer, consultant, vocational and entrepreneurship skills provider for all categories of employees and potential entrepreneurs including unemployed individuals in the society. She also caters for the needs of old workers (both the current and intending retirees)."
    posts = BlogPost.objects.all().order_by("-date")
    services3 = Service.objects.all()
    # Search feature
    query = request.GET.get('q')
    if query:
        blogs = blogs.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(author__user__first_name__icontains=query)
        ).distinct()
    context = {
        'posts':posts,
        'services3':services3,
        "about":about,
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request, url):
    blog = BlogPost.objects.get(url=url)
    top_stories_week = BlogPost.objects.order_by('-id')[:3]
    recent_posts = BlogPost.objects.order_by('-id')[0]
    recent_posts2 = BlogPost.objects.order_by('-id')[:3]
    services3 = Service.objects.all()
    comments = CommentPost.objects.all().filter(post=blog).order_by('-id')[:5]
    blog.views+=1
    blog.save()
    context = {
    "post": blog,
    "top_posts": top_stories_week,
    "recent_posts": recent_posts,
    "recent_post2": recent_posts2,
    'comments':comments,
    }
    return render(request, 'blog/single.html', context)

@login_required(login_url='/accounts/login/')
def commentView(request):
    if request.method == "POST":
        print(request.POST)
        user = request.user
        content = request.POST['Message']
        post_url = request.POST['post_url']
        post = BlogPost.objects.get(url=post_url)
        CommentPost.objects.create(user=user, content=content, post=post)
        return redirect('/blog/blog_detail/'+post_url)



@login_required(login_url='/accounts/login/')
def create_blog(request):
    return render(request, 'blogs/create_blog.html')


@login_required(login_url='/accounts/login/')
def update_blog(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    context = {
        'blog': blog,
    }
    return render(request, 'blogs/create_blog.html', context)


@login_required(login_url='/accounts/login/')
def delete_blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')
