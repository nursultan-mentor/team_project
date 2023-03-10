from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import UserCreateView
from news import views


item_router = DefaultRouter()
item_router.register('items', views.ItemAPIView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', UserCreateView.as_view()),
    path('api/', include(item_router.urls)),
]
