from django.urls import include, path
from rest_framework import routers
from restapp import views

#router = routers.DefaultRouter()
#router.register('users', views.P_UserViewSet)
#router.register('groups', views.P_GroupViewSet)

urlpatterns = [
    path('users/', views.P_UserView.as_view()),
    path('users/<str:userid>/', views.P_UserView.as_view()),
    path('groups/', views.P_GroupView.as_view()),
    path('groups/<str:name>/', views.P_GroupView.as_view()),
]
