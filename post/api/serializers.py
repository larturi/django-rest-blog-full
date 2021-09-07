from rest_framework import serializers
from post.models import Post
from user.models import User
from category.models import Category

from user.api.serializers import UserSerializer
from category.api.serializers import CategorySerializer


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', ]


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', ]


class PostSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # category = CategorySerializer()

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
            'user'
        ]
