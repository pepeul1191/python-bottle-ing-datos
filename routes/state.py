#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, template, request, HTTPResponse
from configs.helpers import menu
from daos.state_dao import get_all, get_state_by_id, create, update, delete

subapp = Bottle()

@subapp.route('/', method='GET')
def home():
  locals = {
    'title': 'Gestión de Estados',
    'menu': menu('/state'),
    'states': get_all(),
  }
  boby_template = template('state/index', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)

@subapp.route('/create', method='GET')
def create_view():
  form_title = 'Crear Estado'
  locals = {
    'title': 'Gestión de Estados',
    'menu': menu('/state'),
    'state': {
      'id': 'E',
      'name': '',
    },
    'form_title': form_title,
  }
  boby_template = template('state/detail', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)

@subapp.route('/edit', method='GET')
def edit_view():
  state = get_state_by_id(request.params.id)
  if state != None:
    form_title = 'Editar Estado'
    locals = {
      'title': 'Gestión de Estado',
      'menu': menu('/state'),
      'state': {
        'id': state['id'],
        'name': state['name'],
      },
      'form_title': form_title,
    }
    boby_template = template('state/detail', locals = locals)
    return HTTPResponse(status = 200, body = boby_template)
  else:
    locals = {
      'title': 'Notifiación: Error 404',
      'message': 'Estado no encontrada',
      'url': '/state',
      'menu': menu('/xd'),
    }
    boby_template = template('_notification', locals = locals)
    return HTTPResponse(status = 404, body = boby_template)

@subapp.route('/delete', method='GET')
def delete_by_id():
  delete(request.params.id)
  locals = {
    'title': 'Notifiación: Registro Eliminado',
    'message': 'Estado eliminado',
    'url': '/state',
    'menu': menu('/xd'),
  }
  boby_template = template('_notification', locals = locals)
  return HTTPResponse(status = 404, body = boby_template)
  

@subapp.route('/save', method='POST')
def save():
  message = ''
  if request.forms.get('id') == 'E':
    message = 'Se ha creado un nuevo estado'
    create(
      request.forms.get('name'),
    )
  else:
    message = 'Se ha editado el estado'
    update(
      request.forms.get('id'),
      request.forms.get('name'),
    )
  locals = {
    'title': 'Notifiación: ' + message,
    'message': message,
    'url': '/state',
    'menu': menu('/xd'),
  }
  boby_template = template('_notification', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)