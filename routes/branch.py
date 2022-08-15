#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, template, HTTPResponse
from configs.helpers import menu
from daos.branch_dao import get_lima_branches, get_province_branches

subapp = Bottle()

@subapp.route('/', method='GET')
def home():
  print(get_lima_branches())
  locals = {
    'title': 'Gestión de Sedes',
    'menu': menu('/branch'),
    'lima_branches': get_lima_branches(),
    'province_branches': get_province_branches(),
  }
  boby_template = template('branch', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)