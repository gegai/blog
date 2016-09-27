"""blog1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^log/', views.log,name='log'),
    # url('^login/',views.login,name='login'),
    url('^login/',views.acc_login,name='login'),
    url('^logout/',views.acc_logout,name='logout'),
    url('^register/',views.register,name='register'),
    url(r'^article/(?P<article_id>\d+)/$', views.article_detail, name='article_detail'),
    url(r'^category/(?P<category_id>\d+)/$', views.category, name='category'),
    url(r'^article/new/$', views.new_article, name='new_article'),
    url(r'^$', views.index, name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 为了修正前端图片显示

