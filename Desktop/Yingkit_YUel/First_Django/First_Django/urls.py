"""First_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import re_path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('showtime/', views.showtime),

    #path(r'article/\d{4}', views.article_year)
    #有几个分组给view传几个参数
    #re_path(r'article/(\d{4})/(\d{2})', views.article_year),

    #有名分组  分组名为什么，view中的形参必须为分组名
    re_path(r'article/(?P<year>\d{4})/(?P<month>\d{2})', views.article_year_month),

    re_path(r'register', views.register, name='reg')
]
