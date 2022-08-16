#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email import message
import os
from datetime import datetime
from bottle import Bottle, template, request, HTTPResponse
from configs.helpers import menu
from daos.position_dao import get_all as get_all_positions
from daos.worker_dao import get_all, get_worker_by_id, create, update, delete, update_image_url
from daos.branch_worker_dao import get_worker_branches, get_record_by_ids, create as create_branch_worker, delete as delete_branch_worker

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
        'image_url': worker['image_url'],
      },
      'form_title': form_title,
      'lima_branchs': get_worker_branches(1, request.params.id),
      'province_branchs': get_worker_branches(2, request.params.id),
      'position_list': get_all_positions(),
    }
    print(get_worker_branches(1, request.params.id))
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

@subapp.route('/branch', method='POST')
def save():
  worker_id = int(request.forms.get('worker_id'))
  branches_id_exist = request.forms.get('branches_id_exist').split(',')
  branches_id_not_exist = request.forms.get('branches_id_not_exist').split(',')
  for branch_id in branches_id_exist:
    branch_id = int(branch_id)
    e = get_record_by_ids(worker_id, branch_id)
    if e == None:
      create_branch_worker(worker_id, branch_id)
  for branch_id in branches_id_not_exist:
    branch_id = int(branch_id)
    e = get_record_by_ids(worker_id, branch_id)
    if e != None:
      delete_branch_worker(worker_id, branch_id)
  locals = {
    'title': 'Notifiación: Sedes del Empleado Actualizado',
    'message': 'Sedes del Empleado Actualizado',
    'url': request.forms.get('url'),
    'menu': menu('/xd'),
  }
  boby_template = template('_notification', locals = locals)
  return HTTPResponse(status = 200, body = boby_template)

@subapp.route('/upload_image', method='POST')
def upload_image():
  status = 200
  message = 'Imagen asociada al trabajador'
  upload = request.files.get('file')
  id = int(request.forms.get('id'),)
  ext = os.path.splitext(upload.filename)
  timestamp = datetime.timestamp(datetime.now())*10000
  if ext[1] not in ('.png', '.jpg'):
    status = 500
    message = 'Debe de seleccionar una imagen'
  file_path = "{path}/{file}".format(path='static/uploads', file=str(timestamp) + ext[1])
  upload.save(file_path)
  update_image_url(id, "{path}/{file}".format(path='uploads', file=str(timestamp) + ext[1]))
  locals = {
    'title': 'Notifiación: ' + message,
    'message': message,
    'url': request.forms.get('url'),
    'menu': menu('/xd'),
  }
  boby_template = template('_notification', locals = locals)
  return HTTPResponse(status = status, body = boby_template)