from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from  inicio import views
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Autos.views.home', name='home'),
    # url(r'^Autos/', include('Autos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.inicio, name="inicio"),
    url(r'^nissan/$',views.nissan, name="nissan"),
    url(r'^aston/$',views.aston, name="aston"),
    url(r'^ferrari/$',views.ferrari, name="ferrari"),
    url(r'^acercade/$',views.acercade, name="acercade"),
    url(r'^contacto/$',views.contacto, name="contacto"),
)
