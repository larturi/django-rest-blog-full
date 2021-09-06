from rest_framework.viewsets import ModelViewSet
from category.api.serializers import CategorySerializer
from category.models import Category
from category.api.permissions import IsAdminOrReadOnly


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'
