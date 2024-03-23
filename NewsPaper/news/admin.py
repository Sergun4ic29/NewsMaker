from django.contrib import admin
from django.contrib import admin
from .models import Post

from django.contrib.auth.admin import User

#admin.site.register(User, UserAdmin)

# Register your models here.
admin.site.register(Post)