#! /usr/bin/env python

from flask import render_template

def render_index():
    print('HERE')
    return render_template('index.html')
