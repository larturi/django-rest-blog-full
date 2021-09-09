from rest_framework import serializers
from post.models import Post
from category.api.serializers import CategorySerializer
from user.api.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):

    category_data = CategorySerializer(source="category", read_only=True)
    user_data = UserSerializer(source="user", read_only=True)

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'slug',
            'miniature',
            'created_at',
            'published',
            'user',
            'user_data',
            'category',
            'category_data'
        ]
