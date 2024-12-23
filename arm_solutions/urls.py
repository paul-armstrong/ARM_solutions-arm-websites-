"""
URL configuration for arm_solutions project.

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
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.shortcuts import render
def custom_404_view(request):
    return render(request,'404.html')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('index.urls')),
  #  path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    path('sitemap.xml', TemplateView.as_view(template_name="sitemap.xml",content_type='application/xml')),
    path('www-sitemap.xml', TemplateView.as_view(template_name="www-sitemap-armsolutions.xml", content_type='application/xml')),
    re_path(r'^.*$', custom_404_view),
]
if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

