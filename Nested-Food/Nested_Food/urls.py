"""
URL configuration for Nested_Food project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('blog/',blog,name='blog'),
    path('booking/',booking,name='booking'),
    path('orderhistory/',orderhistory,name='orderhistory'),
    path('menu/',menu,name='menu'),
    path('single/',single,name='single'),
    path('contact/',contact_us,name='contact'),
    path('about/',about,name='about'),
    path('team/',team,name='team'),
    path('register/',register,name='register'),
    path('login/',signin,name='login'),
    path('cart/<int:id>',cart,name='cart'),
    path('cart/',cartall,name='cart'),
    path('dish/<int:id>',dish,name='dish'),
    path('qntyadd/<int:id>',qntyadd,name='qntyadd'),
    path('qntysub/<int:id>',qntysub,name='qntysub'),
    path('remove/<int:id>',removedish,name='remove'),
    path('order/',order,name='order'),
    path('payment/',payment,name='payment'),
    path('logout/',logout_user,name='logout'),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)