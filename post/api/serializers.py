from rest_framework import serializers
from post.models import Post
from user.models import User
from category.models import Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        depth = 2
        fields = [
            'id',
            'title',
            'content',
            'slug',
            'miniature',
            'created_at',
            'published',
            'category',
            'user',
        ]
