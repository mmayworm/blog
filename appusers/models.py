from django.db import models


class UserName(models.Model):   #Você pode escolher o nome da classe, ela precisa herdar de model.Models.
    user_name = models.CharField(max_length=150, default='')
    
    def __str__(self):
        return f'user_name: {self.user_name}'
    
from django.db import models

class Post(models.Model):
    author_name = models.CharField(max_length=100, default="Anonymous")
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    # NOVO CAMPO: Para armazenar o URL da foto
    avatar_url = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author_name} - {self.post.title}'

