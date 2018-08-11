# main.py
import webview
import subprocess
import sys
import os
import logging
from logging import handlers

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

# Create a resizable window
webview.create_window("PyBrowse for Windows", "https://moosystems.com", width=800, height=600, resizable=True, fullscreen=False)

