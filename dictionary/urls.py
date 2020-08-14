"""swu_site_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    # path('<int:pk>/', views.post_detail),
    path('', views.index),
    path('2/', views.detail),
    path('3/', views.detail2),
    path('4/', views.detail3),
    path('5/', views.detail4),
    path('6/', views.detail5),
    path('7/', views.detail6),
    path('8/', views.detail7),
    path('9/', views.detail8),
    path('10/', views.detail9),
    path('11/', views.detail10),
    path('12/', views.detail11),
    path('13/', views.detail12),
    path('14/', views.detail13),
    path('15/', views.detail14),
    path('16/', views.detail15),
    path('17/', views.detail16),
    path('18/', views.detail17),
]
