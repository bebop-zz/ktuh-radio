from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^tinymce/', include('tinymce.urls')),

    # Front Page
    (r'^$', 'front_page.views.index'),

    # Show Grid
    (r'^show_grid/$', 'show_grid.views.index'),
    (r'^show_grid/(?P<show_grid_id>\d+)/$', 'show_grid.views.detail'),

    # Music
    (r'^music/$', 'music.views.index'),
    (r'^music/(?P<music_id>\d+)/$', 'music.views.detail'),

    # Events
    (r'^events/$', 'events.views.index'),
    (r'^events/(?P<event_id>\d+)/$', 'events.views.detail'),

    # Faqs
    (r'^faq/$', 'faq.views.index'),
    (r'^faq/(?P<faq_id>\d+)/$', 'faq.views.detail'),

    # Admin:
    (r'^admin/show_grid/showgrid/$', 'show_grid.admin_views.showgrid'),
    (r'^admin/', include(admin.site.urls)),
)
