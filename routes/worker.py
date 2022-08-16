#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, template, request, HTTPResponse
from configs.helpers import menu
from daos.worker_dao import get_all

subapp = Bottle()

@subapp.route('/', method='GET')
def home():
  step = int(request.params.step)
  page = int(request.params.page)
  workers_page = get_all(step, page)
  locals = {
    'title': 'Gestión de Empleados',
    'menu': menu('/worker'),
    'workers': workers_page['workers'],
    'pages': workers_page['pages'],
    'page': page,
  }
  boby_template = template('worker/index', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)
