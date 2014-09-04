from django.conf.urls import patterns, include, url
from django.conf import settings


from django.contrib import admin
import main.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BlandineWebSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', main.views.home),
    url(r'^symbiotonie/?$', main.views.symbio),
    url(r'^contact/?$', main.views.contact),
    url(r'^psycho/?$', main.views.psycho),
    url(r'^stages/?$', main.views.stages),
    url(r'^stages/voir/(?P<id>.*)/?$', main.views.view_stage),
    # CKEDITOR for HTML EDITOR
    (r'^ckeditor/', include('ckeditor.urls')),
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
