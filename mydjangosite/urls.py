from django.conf.urls.defaults import *
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', TemplateView.as_view(template_name="index.html")),
    (r'^polls/$', 'mydjangosite.polls.views.index'),
    (r'^polls/(?P<poll_id>\d+)/$', 'mydjangosite.polls.views.detail'),
    #(r'^polls/(?P<poll_id>\d+)/results/$', 'mydjangosite.polls.views.results'),
    #(r'^polls/(?P<poll_id>\d+)/vote/$', 'mydjangosite.polls.views.vote'),
    # Uncomment the next line to enable the admin:
    (r'^admin/', admin.site.urls),
    (r'', include('django.contrib.auth.urls')),
)
