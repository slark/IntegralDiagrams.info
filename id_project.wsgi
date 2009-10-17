import os
import sys

sys.path = ['/home/slark/webapps/integraldiagrams', '/home/slark/webapps/integraldiagrams/lib/python2.5',
'/home/slark/webapps/integraldiagrams/id_project'] + sys.path
from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'id_project.settings'
application = WSGIHandler()
