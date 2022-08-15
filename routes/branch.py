#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, template, request, HTTPResponse
from configs.helpers import menu
from daos.branch_dao import get_lima_branches, get_province_branches, get_branch_by_id, create, update, delete
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
  if branch != None:
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
  else:
    locals = {
      'title': 'Notifiación: Error 404',
      'message': 'Sede no encontrada',
      'url': '/branch',
      'menu': menu('/xd'),
    }
    boby_template = template('_notification', locals = locals)
    return HTTPResponse(status = 404, body = boby_template)

@subapp.route('/delete', method='GET')
def delete_by_id():
  delete(request.params.id)
  locals = {
    'title': 'Notifiación: Registro Eliminado',
    'message': 'Sede eliminada',
    'url': '/branch',
    'menu': menu('/xd'),
  }
  boby_template = template('_notification', locals = locals)
  return HTTPResponse(status = 404, body = boby_template)
  

@subapp.route('/save', method='POST')
def save():
  message = ''
  if request.forms.get('id') == 'E':
    message = 'Se ha creado una nueva sede'
    create(
      request.forms.get('name'),
      request.forms.get('address'),
      request.forms.get('phone'),
      request.forms.get('whatsapp'),
      request.forms.get('branch_type_id'),
    )
  else:
    message = 'Se ha editado la sede'
    update(
      request.forms.get('id'),
      request.forms.get('name'),
      request.forms.get('address'),
      request.forms.get('phone'),
      request.forms.get('whatsapp'),
      request.forms.get('branch_type_id'),
    )
  locals = {
    'title': 'Notifiación: ' + message,
    'message': message,
    'url': '/branch',
    'menu': menu('/xd'),
  }
  boby_template = template('_notification', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)