#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, template, request, HTTPResponse
from configs.helpers import menu
from daos.position_dao import get_all, get_position_by_id, create, update, delete

subapp = Bottle()

@subapp.route('/', method='GET')
def home():
  locals = {
    'title': 'Gestión de Posiciones',
    'menu': menu('/position'),
    'positions': get_all(),
  }
  boby_template = template('position/index', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)

@subapp.route('/create', method='GET')
def create_view():
  form_title = 'Crear Posición'
  locals = {
    'title': 'Gestión de Posiciones',
    'menu': menu('/position'),
    'position': {
      'id': 'E',
      'name': '',
    },
    'form_title': form_title,
  }
  boby_template = template('position/detail', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)

@subapp.route('/edit', method='GET')
def edit_view():
  position = get_position_by_id(request.params.id)
  if position != None:
    form_title = 'Editar Posición'
    locals = {
      'title': 'Gestión de Posiciones',
      'menu': menu('/position'),
      'position': {
        'id': position['id'],
        'name': position['name'],
      },
      'form_title': form_title,
    }
    boby_template = template('position/detail', locals = locals)
    return HTTPResponse(status = 200, body = boby_template)
  else:
    locals = {
      'title': 'Notifiación: Error 404',
      'message': 'Posición no encontrada',
      'url': '/position',
      'menu': menu('/xd'),
    }
    boby_template = template('_notification', locals = locals)
    return HTTPResponse(status = 404, body = boby_template)

@subapp.route('/delete', method='GET')
def delete_by_id():
  delete(request.params.id)
  locals = {
    'title': 'Notifiación: Registro Eliminado',
    'message': 'Posición eliminada',
    'url': '/position',
    'menu': menu('/xd'),
  }
  boby_template = template('_notification', locals = locals)
  return HTTPResponse(status = 404, body = boby_template)

@subapp.route('/save', method='POST')
def save():
  message = ''
  if request.forms.get('id') == 'E':
    message = 'Se ha creado una nueva posición'
    create(
      request.forms.get('name'),
    )
  else:
    message = 'Se ha editado la posición'
    update(
      request.forms.get('id'),
      request.forms.get('name'),
    )
  locals = {
    'title': 'Notifiación: ' + message,
    'message': message,
    'url': '/position',
    'menu': menu('/xd'),
  }
  boby_template = template('_notification', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)