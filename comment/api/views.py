from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from comment.models import Comment
from comment.api.serializers import CommentSerializer


class CommentApiViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-created_at']
    filterset_fields = ['post']
