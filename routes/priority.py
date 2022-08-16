#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, template, request, HTTPResponse
from configs.helpers import menu
from daos.priority_dao import get_all, get_priority_by_id, create, update, delete

subapp = Bottle()

@subapp.route('/', method='GET')
def home():
  locals = {
    'title': 'Gestión de Prioridades',
    'menu': menu('/priority'),
    'priorities': get_all(),
  }
  boby_template = template('priority/index', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)

@subapp.route('/create', method='GET')
def create_view():
  form_title = 'Crear Prioridad'
  locals = {
    'title': 'Gestión de Prioridades',
    'menu': menu('/priority'),
    'priority': {
      'id': 'E',
      'name': '',
    },
    'form_title': form_title,
  }
  boby_template = template('priority/detail', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)

@subapp.route('/edit', method='GET')
def edit_view():
  priority = get_priority_by_id(request.params.id)
  if priority != None:
    form_title = 'Editar Prioridad'
    locals = {
      'title': 'Gestión de Prioridades',
      'menu': menu('/priority'),
      'priority': {
        'id': priority['id'],
        'name': priority['name'],
      },
      'form_title': form_title,
    }
    boby_template = template('priority/detail', locals = locals)
    return HTTPResponse(status = 200, body = boby_template)
  else:
    locals = {
      'title': 'Notifiación: Error 404',
      'message': 'Prioridad no encontrada',
      'url': '/priority',
      'menu': menu('/xd'),
    }
    boby_template = template('_notification', locals = locals)
    return HTTPResponse(status = 404, body = boby_template)

@subapp.route('/delete', method='GET')
def delete_by_id():
  delete(request.params.id)
  locals = {
    'title': 'Notifiación: Registro Eliminado',
    'message': 'Prioridad eliminada',
    'url': '/priority',
    'menu': menu('/xd'),
  }
  boby_template = template('_notification', locals = locals)
  return HTTPResponse(status = 404, body = boby_template)
  

@subapp.route('/save', method='POST')
def save():
  message = ''
  if request.forms.get('id') == 'E':
    message = 'Se ha creado una nueva prioridad'
    create(
      request.forms.get('name'),
    )
  else:
    message = 'Se ha editado la prioridad'
    update(
      request.forms.get('id'),
      request.forms.get('name'),
    )
  locals = {
    'title': 'Notifiación: ' + message,
    'message': message,
    'url': '/priority',
    'menu': menu('/xd'),
  }
  boby_template = template('_notification', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)