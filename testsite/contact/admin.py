from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_time')
    search_fields = ['email', 'name']
    readonly_fields = ['created_time']


admin.site.register(Contact, ContactAdmin)