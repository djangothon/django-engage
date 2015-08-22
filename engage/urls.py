from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'engage.views',
    url("", include('django_socketio.urls')),
)
