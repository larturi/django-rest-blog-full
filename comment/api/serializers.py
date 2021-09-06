from rest_framework import serializers
from comment.models import Comment
from user.api.serializers import UserSerializer
from category.api.serializers import CategorySerializer


class CommentSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # category = CategorySerializer()

    class Meta:
        model = Comment
        fields = ['content', 'user', 'post', 'created_at']
