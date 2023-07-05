from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers

from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name',
                  'username', 'email', 'bio', 'profile_picture', 'gitHub', 'twitter', 'youtube', 'linkedin']


class CourseSerializer(ModelSerializer):
    Instructor = UserSerializer(source='instructor', read_only=True)

    class Meta:
        model = Course
        fields = [
            'Instructor',
            'id',
            'title',
            'what_you_learn',
            'requirements',
            'targeted_audience',
            'price',
            'duration_in_minutes',
            'created_at',
            'updated_at',
        ]
