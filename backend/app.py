#! /usr/bin/env python

from flask import Flask
from backend.views import *
from backend.sockets import SOCKET

SOCKET.start()
APP = Flask(__name__, static_url_path='', template_folder='../static/templates')

@APP.route('/', methods = ['GET'])
def index():
    return render_index()

@APP.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('../static/js', path)


jinja_options = APP.jinja_options.copy()
jinja_options.update(dict(
    variable_start_string='%%',
    variable_end_string='%%',
))
APP.jinja_options = jinja_options