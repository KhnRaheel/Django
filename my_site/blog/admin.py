from xml.etree.ElementTree import Comment
from django.contrib import admin

# Register your models here.
from .models import Comment, Post , Author, Tag


class PostAdmin(admin.ModelAdmin):
    list_filter= ("author","date","tag",)
    list_display=("title","date","author",)
    prepopulated_fields={"slug":("title",)}


admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)

