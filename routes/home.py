#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, request, HTTPResponse

subapp = Bottle()

@subapp.route('/', method='GET')
def home():
  status = 200
  resp = 'hola desdel nuevo home'
  return HTTPResponse(status = status, body = resp)