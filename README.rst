Django on Twisted using Twisted's (new) WSGI code
=================================================
This directory contains an example of how to combine Twisted and Django
using the latest WSGI functionality in twisted.web.

A more complete discussion of this code can be found here:
----------------------------------------------------------
http://clemesha.org/blog/2009/apr/23/Django-on-Twisted-using-latest-twisted-web-wsgi/


Install
-------
#. Recommended: Use a ``virtualenv`` and install with ``pip``, to get them type::

    easy_install virtualenv pip


#. Create a fresh ``virtualenv``::
    
    virtualenv --no-site-packages twisted_wsgi_django_env


#. Install dependencies into your ``virtualenv``::
    
    #You must have Django 1.0+ and Twisted 9.0.0+
    
    pip -E twisted_wsgi_django_env install twisted django


#. Get a copy of the example::

    curl http://github.com/clemesha/twisted-wsgi-django/tarball/master

    #Or clone a copy:
    
    $ git clone git://github.com/clemesha/twisted-wsgi-django.git


Run example
-----------

#. Move into your ``virtualenv`` and `activate` it::
    
    $ cd twisted_wsgi_django_env
    $ source bin/activate


#. Move into the example and do a `syncdb`::

    $ cd mydjangosite 
    $ python manage.py syncdb #be sure to create an admin user


#. Move up one directory and run the example::
    $ cd .. #assume you are in 'mydjangosite'
    $ twistd -ny server.py #open localhost:8000 in browser


License/Contact
---------------
All code licensed under the BSD.
Contact: Alex Clemesha <alex@clemesha.org> | http://twitter.com/clemesha
