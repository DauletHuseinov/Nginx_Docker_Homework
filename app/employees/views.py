from django.shortcuts import render
from .models import Position, Employee
from .serializers import EmployeeSerializer, PositionSerializer
from rest_framework import mixins, viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.


class PositionAPIView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class PositionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class EmployeeAPIView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)
