from django.urls import path
from django.urls.resolvers import URLPattern
from user.api.views import RegisterView

urlpatterns = [
    path('auth/register', RegisterView.as_view())
]
