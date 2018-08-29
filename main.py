# main.py
import webview
import subprocess
import sys
import os
import logging
from logging import handlers

import asyncio
import threading
import tornado.httpserver
import tornado.ioloop
from tornado import options
import tornado.web
import tornado.wsgi

from django.core.wsgi import get_wsgi_application

# Check if we are running as exe or as a script
try:
    base_dir = os.path.realpath(os.path.dirname(__file__))
    run_as_binary = False
except NameError:
    base_dir = os.path.realpath(os.path.dirname(os.path.dirname(os.path.dirname(sys.argv[0]))))
    run_as_binary = True


# Setup logging
if run_as_binary:
    log_file = os.path.join(base_dir, '..', 'PyBrowse for Windows.log')
    cherry_access_log = os.path.join(base_dir, '..', 'access.log')
    cherry_error_log = os.path.join(base_dir, '..', 'error.log')
    app_name = 'PyBrowse for Windows'
else:
    log_file = os.path.join(base_dir, '..', 'PyBrowse for Windows.log')
    cherry_access_log = os.path.join(base_dir, 'access.log')
    cherry_error_log = os.path.join(base_dir, 'error.log')
    app_name = 'PyBrowse for Windows'

handler = logging.handlers.RotatingFileHandler(log_file, backupCount=10)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)

log = logging.getLogger('PyBrowse for Windows')
log.setLevel(logging.DEBUG)
log.addHandler(handler)

# py2exe will report an error even if there's none if we log something
# log_msg = 'Are we running as binary? %s' % run_as_binary
# log.debug(log_msg)

# Setup server
try:
    options.define('port', type=int, default=8085)
except:
    pass

"""
class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello from Tornado')
"""
class WebThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name='WebThread')

    def run(self):
        curdir = os.path.dirname(os.path.realpath(__file__))

        ioloop = tornado.ioloop.IOLoop()

        application = tornado.web.Application()
        http_server_api = tornado.httpserver.HTTPServer(application)
        http_server_api.listen(8085)

        print('starting app')

        ioloop.start()

t = WebThread()
t.start()

"""
class WebServer(tornado.web.Application):

    def __init__(self):
        os.environ['DJANGO_SETTINGS_MODULE'] = 'locallibrary.settings'
        sys.path.append('./locallibrary')

        options.parse_command_line()

        wsgi_app = get_wsgi_application()
        container = tornado.wsgi.WSGIContainer(wsgi_app)

        handlers = [
            ('.*', tornado.web.FallbackHandler, dict(fallback=container)),
        ]
        settings = {
            'debug': True,
        }
        super().__init__(handlers, **settings)

    def start(self, port=8085):
        print('start the server')
        ioloop = tornado.ioloop.IOLoop.current()
        self.listen(port)
        #ioloop.add_callback(create_window)
        ioloop.start()


server = WebServer()

#web = WebThread()
#web.start()

def start_server():
    asyncio.set_event_loop(asyncio.new_event_loop())
    server.start(options.options.port)

t = threading.Thread(target=start_server)
t.daemon = True
t.start()
"""
import time
time.sleep(10)

print('create window')
# Create a resizable window
webview.create_window("PyBrowse for Windows", "https://localhost:8085/", width=800, height=600, resizable=True, fullscreen=False)

