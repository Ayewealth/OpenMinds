from django.urls import path

from . import views

urlpatterns = [
    path('', views.endpoints),
    path('users', views.UserCreateListApiView.as_view()),
    path('users/<str:username>/', views.UserRetrieveUpdateDestroyApiView.as_view()),

    path('course', views.CourseCreateListApiView.as_view()),
    path('course/<str:title>/', views.CourseRetrieveUpdateDestroyApiView.as_view()),
]
