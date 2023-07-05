from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, mixins

from .models import *
from .serializers import *

# Create your views here.


@api_view(['Get'])
def endpoints(request):
    data = [
        '/user', '/user:<username>',
        '/courses', '/courses:<title>',
        '/blog', '/blog:<title>',
        '/carts', '/cartitems',
    ]
    return Response(data)


class UserCreateListApiView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def perform_update(self, serializer):
        instance = serializer.save()

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class CourseCreateListApiView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'title'

    def perform_update(self, serializer):
        instance = serializer.save()

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
