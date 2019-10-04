#! /usr/bin/env python

from Drivers.Socket_Scanner import Socket_Scanner
from flask import Flask, render_template, send_from_directory, jsonify

class Application():
    static_root = 'static/'
    server = Flask(__name__, static_url_path='', template_folder='static/templates/')
    scanner = Socket_Scanner()

    def __init__(self, static_root='static/', template_folder='templates/', static_url_path=''):
        Application.static_root = static_root
        
        self.server.template_folder = static_root + '/' + template_folder
        self.server.static_url_path = static_url_path

    def run(self=None, debug=False):
        Application.server.jinja_options.update(dict(variable_start_string='%%', variable_end_string='%%',))
        Application.server.run(debug=debug, host='0.0.0.0')

    @server.route('/', methods = ['GET'])
    def index():
        return render_template('index.html')

    @server.route('/js/<path:path>')
    def serve_js(path):
        return send_from_directory(Application.static_root + 'js', path)

    @server.route('/css/<path:path>')
    def serve_css(path):
        return send_from_directory(Application.static_root + 'css', path)

    @server.route('/sockets', methods = ['GET'])
    def get_potential_sockets():
        return jsonify(paths=Application.scanner.find_potential_sockets())


if __name__ == '__main__':
    Application.run()
