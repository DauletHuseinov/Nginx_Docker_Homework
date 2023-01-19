from django.shortcuts import render
from rest_framework.response import Response

from .serializers import ProfileSerializer
from .models import Profile
from rest_framework import mixins, viewsets, status


# Create your views here.

class ProfileRegisterAPIView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
