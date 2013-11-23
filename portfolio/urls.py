"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project
"""
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from settings import base

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^portfolio/', include('portfolio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # Static files, served from server
    #url(r'^static/(\?P.*)$', 'django.views.static.serve', {'document_root': base.STATIC_ROOT}),

    # These apply to the public app
    url(r'^portfolio-blog[/]$', TemplateView.as_view(template_name='portfolio-blog.html')),
    url(r'^portfolio-about[/]$', TemplateView.as_view(template_name='portfolio-about.html')),
    url(r'^portfolio-contact[/]$', TemplateView.as_view(template_name='portfolio-contact.html')),
    url(r'^portfolio-project-one[/]$', TemplateView.as_view(template_name='portfolio-project-one.html')),
    url(r'^portfolio-home[/]$', TemplateView.as_view(template_name='portfolio-home.html')),
    url(r'^$', TemplateView.as_view(template_name='portfolio-home.html')),
)
