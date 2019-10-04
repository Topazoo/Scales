#! /usr/bin/env python

from flask import Flask, render_template, send_from_directory

Static_Root = '../../static/'
App_Server = Flask(__name__, static_url_path='', template_folder=Static_Root + 'templates/')

@App_Server.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@App_Server.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory(Static_Root + 'js', path)

@App_Server.route('/css/<path:path>')
def serve_css(path):
    return send_from_directory(Static_Root + 'css', path)

App_Server.jinja_options.update(dict(variable_start_string='%%', variable_end_string='%%',))