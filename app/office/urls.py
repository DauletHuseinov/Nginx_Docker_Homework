"""office URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account import views as acc_view

from employees import views as emp_view

acc_router = DefaultRouter()
acc_router.register('register', acc_view.ProfileRegisterAPIView)

empl_router = DefaultRouter()
empl_router.register('employee', emp_view.EmployeeAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),

    path('api/account/', include(acc_router.urls)),

    path('api/office/position/', emp_view.PositionAPIView.as_view()),
    path('api/office/position/<int:pk>/', emp_view.PositionDetailAPIView.as_view()),

    path('api/office/', include(empl_router.urls))
]
