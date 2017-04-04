
from collections import defaultdict
from math import ceil
from os.path import join

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import BlogPost
#from taggit.managers import TaggableManager


# Create your views here.

exclude_posts = ("about", "projects", "talks","test")

def home(request,page=''):
	args = dict()
	args['blogposts'] = BlogPost.objects.exclude(title__in = exclude_posts)
	max_page = ceil(len(args['blogposts']) / 3)
	if page and int(page) < 2:
		return redirect('/')
	else :
		page = int(page) if (page and int(page) > 0) else 1
		args['page'] = page
		args['prev_page'] = page + 1 if page < max_page else None
		args['newer_page'] = page -1 if page > 1 else None
		args['sl']= str(3 * (page - 1)) + ':' + str(3 * (page - 1) + 3)
		return render(request, 'index.html', args)


def blogpost(request,slug,id):
    args = {'blogpost': get_object_or_404(BlogPost,id=str(id))}
    return render(request, 'blogpost.html', args)


def archive(request):
    args = dict()
    blogposts = BlogPost.objects.exclude(title__in = exclude_posts)

    def get_sorted_posts(category):
        posts_by_year = defaultdict(list)
        posts_of_a_category = blogposts.filter(category=category)  # already sorted by pub_date
        for post in posts_of_a_category:
            year = post.pub_date.year
            posts_by_year[year].append(post)  # {'2013':post_list, '2014':post_list}
        posts_by_year = sorted(posts_by_year.items(), reverse=True)  # [('2014',post_list), ('2013',post_list)]
        return posts_by_year


    args['data'] = [
        ('programming', get_sorted_posts(category="programming")),
        ('acg', get_sorted_posts(category="acg")),
        ('nc', get_sorted_posts(category="nc")),  # no category
    ]

    return render(request, 'archive.html', args)
