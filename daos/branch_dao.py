#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configs.database import engine

def get_lima_branches():
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM branches WHERE branch_type_id=1
  """).format()
  return [dict(r) for r in conn.execute(stmt)]

def get_province_branches():
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM branches WHERE branch_type_id=2
  """).format()
  return [dict(r) for r in conn.execute(stmt)]

def get_branches():
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM branches
  """).format()
  return [dict(r) for r in conn.execute(stmt)]

def create(name, address, phone, whatsapp, branch_type_id):
  conn = engine.connect()
  stmt = ("""
    INSERT INTO branches (name, address, phone, whatsapp, branch_type_id) 
      VALUES ('{}','{}','{}','{}',{});
  """).format(name, address, phone, whatsapp, branch_type_id)
  rs = conn.execute(stmt)
  return rs.lastrowid

def update(id, name, address, phone, whatsapp, branch_type_id):
  print('1 +++++++++++++++++++++++++')
  print(address)
  print('2 +++++++++++++++++++++++++')
  conn = engine.connect()
  stmt = ("""
    UPDATE branches SET 
      name='{}',  address='{}',  phone='{}',  whatsapp='{}', branch_type_id={} 
      WHERE id={};
  """).format(name, address, phone, whatsapp, branch_type_id, id)

  rs = conn.execute(stmt)
  return rs

def get_branch_by_id(id):
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM branches WHERE id={};
  """).format(id)
  return [dict(r) for r in conn.execute(stmt)][0]
