#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, template, request, HTTPResponse
from configs.helpers import menu
from daos.position_dao import get_all as get_all_positions
from daos.worker_dao import get_all, get_worker_by_id, create, update, delete

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

@subapp.route('/create', method='GET')
def create_view():
  form_title = 'Crear Empleado'
  locals = {
    'title': 'Gestión de Empleados',
    'menu': menu('/worker'),
    'worker': {
      'id': 'E',
      'names': '',
      'last_names': '',
      'email': '',
      'phone': '',
      'position_id': 1,
    },
    'form_title': form_title,
    'position_list': get_all_positions(),
  }
  boby_template = template('worker/detail', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)

@subapp.route('/edit', method='GET')
def edit_view():
  worker = get_worker_by_id(request.params.id)
  if worker != None:
    form_title = 'Editar Empleado'
    locals = {
      'title': 'Gestión de Sedes',
      'menu': menu('/worker'),
      'worker': {
        'id': worker['id'],
        'names': worker['names'],
        'last_names': worker['last_names'],
        'phone': worker['phone'],
        'email': worker['email'],
        'position_id': worker['position_id'],
      },
      'form_title': form_title,
      'position_list': get_all_positions(),
    }
    boby_template = template('worker/detail', locals = locals)
    return HTTPResponse(status = 200, body = boby_template)
  else:
    locals = {
      'title': 'Notifiación: Error 404',
      'message': 'Sede no encontrada',
      'url': '/worker',
      'menu': menu('/xd'),
    }
    boby_template = template('_notification', locals = locals)
    return HTTPResponse(status = 404, body = boby_template)

@subapp.route('/save', method='POST')
def save():
  message = ''
  if request.forms.get('id') == 'E':
    message = 'Se ha creado u nuevo empleado'
    create(
      request.forms.get('names'),
      request.forms.get('last_names'),
      request.forms.get('phone'),
      request.forms.get('email'),
      request.forms.get('position_id'),
    )
  else:
    message = 'Se ha editado un empleado'
    update(
      request.forms.get('id'),
      request.forms.get('names'),
      request.forms.get('last_names'),
      request.forms.get('phone'),
      request.forms.get('email'),
      request.forms.get('position_id'),
    )
  locals = {
    'title': 'Notifiación: ' + message,
    'message': message,
    'url': '/worker?step=10&page=1',
    'menu': menu('/xd'),
  }
  boby_template = template('_notification', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)

@subapp.route('/delete', method='GET')
def delete_by_id():
  delete(request.params.id)
  locals = {
    'title': 'Notifiación: Empleado Eliminado',
    'message': 'Empleado Eliminado',
    'url': '/worker?step=10&page=1',
    'menu': menu('/xd'),
  }
  boby_template = template('_notification', locals = locals)
  return HTTPResponse(status = 404, body = boby_template)