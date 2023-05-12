"""backend_api URL Configuration

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
from django.urls import path, include
from durin import urls as durin_urls
from masters import urls as master_urls
from account import urls as acc_urls
from configuration import urls as conf_urls
from operation import urls as op_urls

urlpatterns = [
    path('api/', include(op_urls)),
    path('api/', include(conf_urls)),
    path('api/', include(master_urls)),
    path('api/', include(acc_urls)),
    path('api/' , include(durin_urls)),
    path('admin/', admin.site.urls),



]
