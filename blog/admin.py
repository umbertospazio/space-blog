from django.contrib import admin
from . import models

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'slug')
    prepopulated_fields = {"slug": ("title",),}

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'publish_date', 'status')
    list_filter = ('status', 'publish_date',)
    search_fields = ('name', 'email', 'content',)

#admin.site.register(models.Post, AuthorAdmin)
