# !/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, run, template, error, static_file, HTTPResponse
from routes.home import subapp as home_routes

app = Bottle()

@app.route('/', method='GET')
def home():
  return template('home')

# errors
@app.error(404)
def error404(error):
  return HTTPResponse(status = 404, body = 'error 404')

# static files
@app.route('/:filename#.*#')
def send_static(filename):
  return static_file(filename, root='./static')

if __name__ == '__main__':
  # mounting sub apps
  app.mount('/demo', home_routes)
  # run app
  run(
    app, host='localhost', port=8080, debug=True,reloader=True
  )