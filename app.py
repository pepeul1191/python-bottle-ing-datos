# !/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, run, template, request, static_file

app = Bottle()

@app.route('/', method='GET')
def home():
  return template('home')

run(
  app, host='localhost', port=8080, debug=True,reloader=True
)