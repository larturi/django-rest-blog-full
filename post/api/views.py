from rest_framework.viewsets import ModelViewSet
from post.api.serializers import PostSerializer
from post.api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from post.models import Post


class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'category__slug']
