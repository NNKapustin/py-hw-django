from rest_framework import serializers
from django.contrib.auth.models import User

from posts.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'text', 'image', 'author', 'created_at', 'is_favorite']

    author = UserSerializer(read_only=True)

    is_favorite = serializers.SerializerMethodField('is_favorite_check')

    def is_favorite_check(self, obj):
        # return self.context['request'].user.id in obj.favorite_by.values_list('id', flat=True) 
        # оптимизированный вариант
        return obj.favorite_by.filter(id=self.context['request'].user.id).exists()