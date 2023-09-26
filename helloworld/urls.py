"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from helloworldapp.views import helloworld1, helloworld2, helloworld3, \
    helloworld4, helloworld5, helloworld6, helloworld7, helloworld8

urlpatterns = [
    path('', helloworld1),
    path('admin/', admin.site.urls),
    path('helloworld1/', helloworld1),
    path('helloworld2/', helloworld2),
    path('helloworld3/<name>/', helloworld3),  # with templates and variables
    # django seance 2
    path('helloworld5/', helloworld5),  # read database
    path('helloworld6/', helloworld6),  # read css, h1 red
    path('helloworld7/', helloworld7, name='helloworld7'),  # internal link to helloworld8
    path('helloworld8/', helloworld8, name='helloworld8'),  # internal link to helloworld7
]

