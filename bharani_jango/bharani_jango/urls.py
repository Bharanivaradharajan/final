"""
URL configuration for bharani_jango project.

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
from myapp import views

urlpatterns = [
    # pylint: disable=no-value-for-parameter
    path('admin/', admin.site.urls),
    path('',views.home),
    path('books.html/',views.books),
    path('social.html/',views.social),
    path('doctor.html/',views.doctor),
    path('reference.html/',views.reference),
    path('forms.html/',views.forms),
    path('ebooks.html',views.ebooks),
    ]
