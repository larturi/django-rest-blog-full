from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.api.serializers import PostSerializer
from post.api.permissions import IsAdminOrReadOnly


class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['slug']
