#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, template, HTTPResponse
from configs.helpers import menu

subapp = Bottle()

@subapp.route('/', method='GET')
def home():
  locals = {
    'title': 'Demo',
    'menu': menu('/demo'),
  }
  boby_template = template('demo/index', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)