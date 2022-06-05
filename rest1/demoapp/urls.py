
from django.urls import include, path

from rest_framework import routers

# from .views import get_users
from demoapp import views

router = routers.DefaultRouter()

router.register('users', views.UserViewSet, basename='users')
router.register('posts', views.PostViewSet, basename='posts')


urlpatterns = [
    path("",include(router.urls)),
    # path('user_names/',get_users, name = 'user'),
    # path('users/',views.UserData.as_view(), name = 'user'),
    # # path('users/<int:pk>/',views.UserData.as_view(), name = 'user'),

]
