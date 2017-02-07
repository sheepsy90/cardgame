"""cardgame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'registration.views.landingpage'),

    url(r'^logout', 'registration.account.logout_user'),
    url(r'^authenticate', 'registration.account.authenticate_user'),

    url(r'^character_choosing', 'registration.views.character_choosing'),
    url(r'^choose/(?P<character_id>[\w-]+)', 'registration.views.choose'),
    url(r'^mainpage/', 'registration.views.main_page'),
]
