import sys
import os

from twisted.application import internet, service
from twisted.web import server, resource, wsgi, static
from twisted.python import threadpool
from twisted.internet import reactor

import twresource

sys.path.append("mydjangosite")
os.environ['DJANGO_SETTINGS_MODULE'] = 'mydjangosite.settings'

from django.core.handlers.wsgi import WSGIHandler

class Root(resource.Resource):

    def __init__(self, wsgi_resource):
        resource.Resource.__init__(self)
        self.wsgi_resource = wsgi_resource

    def getChild(self, path, request):
        path0 = request.prepath.pop(0)
        request.postpath.insert(0, path0)
        return self.wsgi_resource

def wsgi_resource():
    pool = threadpool.ThreadPool()
    pool.start()
    reactor.addSystemEventTrigger('after', 'shutdown', pool.stop)
    wsgi_resource = wsgi.WSGIResource(reactor, pool, WSGIHandler())
    return wsgi_resource


application = service.Application('twisted-django')

wsgi_root = wsgi_resource()
root = Root(wsgi_root)
print os.path.abspath(".")
d = os.path.join(os.path.abspath("."), "mydjangosite/media")
print d
staticrsrc = static.File(d)
root.putChild("media", staticrsrc)

root.putChild("google", twresource.GoogleResource())

main_site = server.Site(root)
internet.TCPServer(8000, main_site).setServiceParent(application)
