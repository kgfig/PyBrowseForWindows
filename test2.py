import threading
from tornado.web import Application
import tornado.ioloop
import os

class WebThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name='WebThread')

    def run(self):
        curdir = os.path.dirname(os.path.realpath(__file__))

        ioloop = tornado.ioloop.IOLoop()

        application = Application() #Very simple tornado.web.Application
        http_server_api = tornado.httpserver.HTTPServer(application)
        http_server_api.listen(8888)

        print('starting app')

        ioloop.start()

t = WebThread()
t.start()

print('create window')
