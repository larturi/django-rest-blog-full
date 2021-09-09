from category.api.serializers import CategorySerializer
from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):

    category_data = CategorySerializer(source="category", read_only=True)

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
            'category',
            'category_data'
        ]
