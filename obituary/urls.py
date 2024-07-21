"""
URL configuration for obituary project.

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
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from obituary_platform.views import home, create_obituary, obituary_info
from obituary_platform.sitemaps import ObituarySitemap

sitemaps = {
    'obituaries': ObituarySitemap,
}




urlpatterns = [
    path('', home, name='home'),  # This is the homepage URL
    path('create/', create_obituary, name='create_obituary'),  # This is the form for creating an obituary URL
    path('obituary_info/<slug>', obituary_info, name = 'obituary_info'), # This is the path to a single obituary article
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
