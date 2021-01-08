
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from .models import BlogPost
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
    blogs = BlogPost.objects.all().order_by("-date")
    services3 = Service.objects.all()
    # Search feature
    query = request.GET.get('q')
    if query:
        blogs = blogs.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(author__user__first_name__icontains=query)
        ).distinct()
    return render(request, 'blog/blog.html', {'blogs': blogs})


def blog_detail(request):
    # blog = BlogPost.objects.get(id=blog_id)
    # top_stories_week = BlogPost.objects.order_by('-view_count')[:3]
    # recent_post = BlogPost.objects.order_by('-view_count')[:3]
    services3 = Service.objects.all()
    # if request.method == "POST":
    # return redirect(blog.get_absolute_url())
    # context = {
    # "blog": blog,
    # "top_stories_week": top_stories_week,
    # "recent_post": recent_post,
    # }
    return render(request, 'blog/single.html')


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
