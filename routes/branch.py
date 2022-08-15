#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, template, request, HTTPResponse
from configs.helpers import menu
from daos.branch_dao import get_lima_branches, get_province_branches, get_branch_by_id
from daos.branch_type_dao import get_all as branch_type_all

subapp = Bottle()

@subapp.route('/', method='GET')
def home():
  locals = {
    'title': 'Gestión de Sedes',
    'menu': menu('/branch'),
    'lima_branches': get_lima_branches(),
    'province_branches': get_province_branches(),
  }
  boby_template = template('branch', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)

@subapp.route('/create', method='GET')
def create_view():
  form_title = 'Crear Sede - Lima'
  if int(request.params.branch_type_id) == 2:
    form_title = 'Crear Sede - Provincia'
  locals = {
    'title': 'Gestión de Sedes',
    'menu': menu('/branch'),
    'branch': {
      'id': 'E',
      'name': '',
      'address': '',
      'phone': '',
      'whatsapp': '',
      'branch_type_id': 1,
    },
    'form_title': form_title,
    'branch_type_list': branch_type_all(),
    'branch_type_id': request.params.branch_type_id,
  }
  boby_template = template('branch_detail', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)

@subapp.route('/edit', method='GET')
def edit_view():
  branch = get_branch_by_id(request.params.id)
  form_title = 'Editar Sede - Lima'
  if int(branch['branch_type_id']) == 2:
    form_title = 'Editar Sede - Provincia'
  locals = {
    'title': 'Gestión de Sedes',
    'menu': menu('/branch'),
    'branch': {
      'id': branch['id'],
      'name': branch['name'],
      'address': branch['address'],
      'phone': branch['phone'],
      'whatsapp': branch['whatsapp'],
      'branch_type_id': branch['branch_type_id'],
    },
    'form_title': form_title,
    'branch_type_list': branch_type_all(),
    'branch_type_id': branch['branch_type_id'],
  }
  boby_template = template('branch_detail', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)