from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from post.models import Post
from category.models import Category


class PostSerializer(serializers.ModelSerializer):
    category = PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Post
        depth = 2
        fields = ['title', 'content', 'slug', 'miniature',
                  'created_at', 'published', 'user', 'category']
