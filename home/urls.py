"""
URL configuration for home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from core.views import *
from django.conf.urls.static import static
from home import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tcp/',tcp,name="index"), 
    path('delete/<id>/',delete,name="delete"),
    path('update/<id>/',update,name="update"),
    path('register/',register,name="register"),
    path('login/',login,name="login"),
    path('about/',abot,name="about"),
    path('con/',con, name="contact"),
    # path('tbt/',tbt, name='header')
    path('session/',session),
    path('get/',get),
    path('logout/',logout),
    path('header1/',header1),
    path('main/',prohome,name="prohome"),
    path('proabout/',proabout,name="proabout"),
    path('prolatestnews/',prolatestnews,name="prolatestnews"),
    path('procategary/',procategary,name="procategary"),
    path('procontact/',procontact,name="procontact"),
    path('prohome/',prohome,name="prohome")

    
   
 ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
