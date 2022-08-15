#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, template, request, HTTPResponse
from configs.helpers import menu
from daos.ticket_dao import get_all

subapp = Bottle()

@subapp.route('/', method='GET')
def home():
  step = int(request.params.step)
  page = int(request.params.page)
  tickest_page = get_all(step, page)
  locals = {
    'title': 'Gestión de Tickets',
    'menu': menu('/ticket'),
    'tickets': tickest_page['tickets'],
    'pages': tickest_page['pages'],
    'page': page,
  }
  boby_template = template('ticket/index', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)
