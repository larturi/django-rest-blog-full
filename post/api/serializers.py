from rest_framework import serializers
from post.models import Post
from user.api.serializers import UserSerializer
from category.api.serializers import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'slug',
            'miniature',
            'created_at',
            'published',
            'user',
            'category'
        ]
