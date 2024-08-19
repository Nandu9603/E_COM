"""
URL configuration for ecommerce1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('all/',views.all),
    path('category/<slug:val>',views.CategoryView.as_view(),name="category"),
    path('product_details/<int:pk>',views.product_details),
    path('add_cart/',views.add_cart, name="add_cart"),
    path('show_cart/',views.show_cart, name="show_cart"),
    path('remove/<int:pk>',views.remove_pro),
    path('pluscart/',views.plus_cart),
    path('add_quantity/<int:pk>',views.add_quantity),
    path('remove_quantity/<int:pk>',views.remove_quantity),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
