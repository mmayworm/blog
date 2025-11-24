from django.contrib import admin
from .models import UserName    #importando nosso modelo criado
from .models import Post, Comment


# Register your models here.
admin.site.register(UserName)
admin.site.register(Post)
admin.site.register(Comment)

