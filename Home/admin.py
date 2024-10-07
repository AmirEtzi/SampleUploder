from django.contrib import admin
from .models import Post, PostImage, Category

admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Category)
