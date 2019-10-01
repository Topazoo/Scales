#! /usr/bin/env python

from flask import Flask, render_template, send_from_directory

App_Server = Flask(__name__, static_url_path='', template_folder='../static/templates')

@App_Server.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@App_Server.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('../static/js', path)

jinja_options = App_Server.jinja_options.copy()
jinja_options.update(dict(
    variable_start_string='%%',
    variable_end_string='%%',
))
App_Server.jinja_options = jinja_options