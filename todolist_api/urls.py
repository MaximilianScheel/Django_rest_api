
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from todo.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'todos', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    
]
