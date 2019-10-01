#! /usr/bin/env python

from flask import Flask
from backend.views import *

APP = Flask(__name__, template_folder='../frontend')

@APP.route('/', methods = ['GET'])
def index():
    print('HERE')
    return render_index()
