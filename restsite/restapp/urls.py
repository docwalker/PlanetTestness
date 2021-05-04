from django.urls import include, path
from rest_framework import routers
from restapp import views

router = routers.DefaultRouter()
router.register('users', views.P_UserViewSet)
router.register('groups', views.P_GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
