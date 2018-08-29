#!/usr/bin/env python
#
# Runs a Tornado web server with a django project
# Make sure to edit the DJANGO_SETTINGS_MODULE to point to your settings.py
#
# http://localhost:8080/hello-tornado
# http://localhost:8080

import sys
import os

from tornado.options import options, define, parse_command_line
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi

from django.core.wsgi import get_wsgi_application

import threading
import asyncio

define('port', type=int, default=8080)


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello from tornado')


def main():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'locallibrary.settings' # TODO: edit this
    sys.path.append('./locallibrary') # path to your project if needed

    parse_command_line()

    wsgi_app = get_wsgi_application()
    container = tornado.wsgi.WSGIContainer(wsgi_app)

    tornado_app = tornado.web.Application(
        [
            ('/hello-tornado', HelloHandler),
            ('.*', tornado.web.FallbackHandler, dict(fallback=container)),
        ])

    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    asyncio.set_event_loop(asyncio.new_event_loop())
    tornado.ioloop.IOLoop.instance().start()

t = threading.Thread(target=main)
t.daemon = True
t.start()
t.join()
print('create window')
