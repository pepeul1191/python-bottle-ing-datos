# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
from bottle import Bottle, run, template, error, static_file, HTTPResponse
from routes.demo import subapp as demo_routes
from routes.branch import subapp as branch_routes
from routes.position import subapp as position_routes
from routes.ticket import subapp as ticket_routes
from routes.employee import subapp as employee_routes
from routes.priority import subapp as priority_routes
from routes.state import subapp as state_routes
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
  app.mount('/demo', demo_routes)
  app.mount('/branch', branch_routes)
  app.mount('/position', position_routes)
  app.mount('/employee', employee_routes)
  app.mount('/priority', priority_routes)
  app.mount('/state', state_routes)
  app.mount('/ticket', ticket_routes)
  # run app
  load_dotenv()
  print(os.getenv('ENV'))
  run(
    app, host='localhost', port=8080, debug=True,reloader=True
  )