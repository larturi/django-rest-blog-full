from rest_framework import serializers
from comment.models import Comment
from user.api.serializers import UserSerializer
from post.api.serializers import PostSerializer


class CommentSerializer(serializers.ModelSerializer):

    user_data = UserSerializer(source="user", read_only=True)
    post_data = PostSerializer(source="post", read_only=True)

    class Meta:
        model = Comment
        fields = [
            'content',
            'user',
            'user_data',
            'post',
            'post_data',
            'created_at'
        ]
