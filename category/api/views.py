from rest_framework.viewsets import ModelViewSet
from category.api.serializers import CategorySerializer
from category.models import Category
from category.api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']
