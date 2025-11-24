from rest_framework import serializers  # importando serializers do rest framework
from .models import UserName    # importando nosso modelo criado
from .models import Post, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):  # Definir um nome de classe e herdar de serializer.ModelSerializer
    class Meta:
        model = UserName    # definir qual o model que será serilizado
        fields = '__all__'  # definir quais campos serão serializados
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'text', 'author_name', 'avatar_url','created_at']
        read_only_fields = ['author', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author_name', 'title', 'content', 'image', 'created_at', 'comments']
        
class UserSerializerAuth(serializers.ModelSerializer):
    class Meta:
        model = User
        # Escolha os campos que o frontend precisa
        fields = ['username']        