from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField('URL Title', max_length=150, null=False, unique=True, allow_unicode=True)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_post_list', args=(self.slug,))


class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = models.SlugField('URL Title', max_length=250, null=False, unique=True, allow_unicode=True)
    short_description = models.TextField('Short Description')
    text = models.TextField()
    is_active = models.BooleanField('Active / Inactive', default=True)
    views = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_time = models.DateTimeField(auto_now_add=False, auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return reverse('post_detail', args=(self.slug,))
