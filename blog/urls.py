"""blog URL Configuration

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
from django.contrib import admin

from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static

from my_auth import views as log_reg

from user import views as main

urlpatterns = [
    path('i_am_admin/', admin.site.urls),
    path('', main.home, name='index'),
    path('login/', log_reg.my_login, name='login'),
    path('register/', log_reg.my_register, name='register'),
    path('logout/', log_reg.logoutUser, name='logout'),
    path('createPost/', main.js_request, name='fetch'),
    path('createComment/', main.js_reqCom, name='fetchCom'),
    path('profil/', main.profil, name='profil'),
    path('info/<int:id>/' or 'info/<string:username>/', main.info, name='info'),
    path('category/<int:id>/', main.category, name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)