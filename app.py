# !/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
from bottle import Bottle, run, template, error, static_file, HTTPResponse
from routes.home import subapp as home_routes
from routes.branch import subapp as branch_routes
from configs.helpers import menu

app = Bottle()

@app.route('/', method='GET')
def home():
  locals = {
    'title': 'Bienvenido',
    'menu': menu('/'),
  }
  boby_template = template('home', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)

# errors
@app.error(404)
def error404(error):
  locals = {
    'title': 'Error 404',
    'menu': menu('/xd'),
  }
  boby_template = template('error', locals = locals)
  return HTTPResponse(status = 404, body = boby_template)

# static files
@app.route('/:filename#.*#')
def send_static(filename):
  return static_file(filename, root='./static')

if __name__ == '__main__':
  # mounting sub apps
  app.mount('/demo', home_routes)
  app.mount('/branch', branch_routes)
  # run app
  run(
    app, host='localhost', port=8080, debug=True,reloader=True
  )