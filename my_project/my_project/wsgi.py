"""
WSGI config for my_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
#Also import
import os, sys, site

#Add the site packages, to override any system-wide
site.addsitedir('/home/reynoso1/webapps/mod_wsgi_3_5/lib/python3.5/site-packages')

#As is
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_demo.settings")

# Activate the virtualenv
activate_this = os.path.expanduser("~/webapps/mod_wsgi_3_5/bin/activate_this.py")
exec(open(activate_this).read())	


#execfile(activate_this, dict(__file__=activate_this))
 
# Calculate the path based on the location of the WSGI script
project = '/home/reynoso1/webapps/mod_wsgi_3_5/my_demo/'
workspace = os.path.dirname(project)
sys.path.append(workspace)
 
sys.path = ['/home/reynoso1/webapps/mod_wsgi_3_5/my_demo', '/home/reynoso1/webapps/mod_wsgi_3_5/my_demo/my_demo', '/home/reynoso1/webapps/mod_wsgi_3_5'] + sys.path
 

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_project.settings")

application = get_wsgi_application()
