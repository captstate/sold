from django.contrib import admin
from .models import Post
# we register our models here so they can be used/viewed in admin panel GUI 

admin.site.register(Post)