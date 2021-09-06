from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from category.api.router import router_category
from post.api.router import router_post
from comment.api.router import router_comment

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Documentación de la API del Blog de Leandro",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="lea.arturi@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc',
                                        cache_timeout=0), name='schema-redoc'),
    path('api/', include('user.api.router')),
    path('api/', include(router_category.urls)),
    path('api/', include(router_post.urls)),
    path('api/', include(router_comment.urls)),
]
