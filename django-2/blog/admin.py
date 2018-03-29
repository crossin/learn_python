from django.contrib import admin
from blog import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'text', 'created_date']
    search_fields = ['title', 'text']
    list_filter = ['author']



admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)
