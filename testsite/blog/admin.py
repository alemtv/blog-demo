from django.contrib import admin
from django import forms
from .models import Category, Post


class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ('name', 'modified_time')
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ['modified_time', 'created_time']


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active', 'views', 'modified_time')
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)