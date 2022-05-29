from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.template import loader
from django.views.generic import ListView
from .models import Category, Post


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by('-modified_time').filter(is_active=1)


def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug, is_active=1)
    template_name = loader.get_template('blog/detail.html')
    context = {
        'post': post
    }
    post.increase_views()
    return HttpResponse(template_name.render(context, request))


def category_list(request):
    cat_list = Category.objects.all().values()
    for cat in cat_list:
        cat['url'] = reverse('category_post_list', args=(cat['slug'],))
        cat['post_count'] = Post.objects.filter(category=cat['id'], is_active=1).count()
    template_name = loader.get_template('blog/category_list.html')
    context = {
        'categories': cat_list,
    }
    return HttpResponse(template_name.render(context, request))


def category_post_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    post_list = Post.objects.filter(category=category)
    template_name = loader.get_template('blog/index.html')
    context = {
        'post_list': post_list
    }
    return HttpResponse(template_name.render(context, request))

