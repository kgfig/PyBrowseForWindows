# main.py
import webview
import sys
import os
import logging
from logging import handlers
import cherrypy
import random
import string
import threading

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

handler = handlers.RotatingFileHandler(log_file, backupCount=10)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)

log = logging.getLogger('PyBrowse for Windows')
log.setLevel(logging.DEBUG)
log.addHandler(handler)

# py2exe will report an error even if there's none if we log something
# log_msg = 'Are we running as binary? %s' % run_as_binary
# log.debug(log_msg)

# Create a simple web server


class SimpleServer(object):

    requests_count = 0

    # Return the HTML content as our homepage
    @cherrypy.expose
    def index(self):
        return """<!DOCTYPE html>
    <html lang="en">
    <meta charset="UTF-8">
        <head>
            <title>PyBrowse</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="Description" content="MacDevOps:YVR 2016 test.">
            <link rel="stylesheet" type="text/css" media="screen" href="/static/css/style.css">
        </head>
        <body
            ondragstart="return false"
            draggable="false"
            ondragenter="event.dataTransfer.dropEffect='none'; event.stopPropagation(); event.preventDefault();"
            ondragover="event.dataTransfer.dropEffect='none';event.stopPropagation(); event.preventDefault();"
            ondrop="event.dataTransfer.dropEffect='none';event.stopPropagation(); event.preventDefault();">

            <div class="welcome_string">Welcome to CherryPy powered by Python.</div>

            <button id="fbutton" type="button">Get data from server</button>

            <div id="count_block"></div>
            <div id="dynamic_block"><div>

            <script>
                var count = 0;
                document.getElementById("fbutton").addEventListener("click", get_data_from_backend);

                function get_data_from_backend() {
                    var request = new XMLHttpRequest();

                    document.getElementById("count_block").innerHTML = "clicked this button " + ++count + " time" + (count > 1 ? "s": "");
                    
                    request.onload = function() {
                        if (request.readyState == 4 && request.status == 200) {
                            document.getElementById("dynamic_block").innerHTML = request.responseText + " client count " + count;
                        } else {
                            document.getElementById("dynamic_block").innerHTML = "an error occured: status " + request.status + " " + count;
                        }
                    };
                    request.addEventListener("error", onerror);
                    
                    request.open("GET", "generate", true);
                    request.send();
                }
            </script>
        </body>
    </html>"""

    # Respond to AJAX request
    @cherrypy.expose
    def generate(self):
        print('called generate')
        self.requests_count = self.requests_count + 1
        return 'server count %d' % self.requests_count 

# Configures and runs the web server
def start_server():
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public',
        }
    }
    cherrypy.config.update({
    'log.screen': False,
       'log.access_file': cherry_access_log,
       'log.error_file': cherry_error_log,
       'server.socket_port': 9090
    })
    cherrypy.quickstart(SimpleServer(), '/', conf)

# Start the server on a new thread
t = threading.Thread(target=start_server)
t.daemon = True
t.start()

# Create a resizable window
webview.create_window("PyBrowse for Windows", "http://localhost:9090/", width=800, height=600, resizable=True, fullscreen=False)

