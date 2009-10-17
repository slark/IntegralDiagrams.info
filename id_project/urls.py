from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('id_app.views',
    (r'^layout.html$', direct_to_template, {'template':   'layout.html'}),
    (r'^$',                                               'home'),
    (r'^subjects$',                                       'subjects'),
    (r'^authors$',                                        'authors'),
    (r'^sources$',                                        'sources'),
    (r'^more$',                                           'more'),
    (r'^all-diagrams/page-(?P<allPageNum>\d+)$',          'all'),
    (r'^(?P<navLink>\S+)/\S+/(?P<setID>\S+)/thumbnails$', 'thumbnails'),
    (r'^(?P<navLink>\S+)/\S+/(?P<setID>\S+)/details$',    'details'),
    (r'^\S+/(?P<photoID>\S+)$',                           'diagram'),
)
