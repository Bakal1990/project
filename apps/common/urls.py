from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    'common.views',
    url(r'^admin/', include(admin.site.urls)),
    url('', include('posts.urls', 'posts')),
    url(r'^profile/', include('profiles.urls', 'profiles')),
    url('', include('social.apps.django_app.urls', namespace='social')),
)

urlpatterns += patterns(
    'django.views.static',
    url(r'^static/(.*)$', 'serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}))
