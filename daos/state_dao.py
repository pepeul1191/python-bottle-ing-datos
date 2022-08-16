#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configs.database import engine

def get_all():
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM states
  """).format()
  return [dict(r) for r in conn.execute(stmt)]

def create(name):
  conn = engine.connect()
  stmt = ("""
    INSERT INTO states (name) 
      VALUES ('{}');
  """).format(name)
  rs = conn.execute(stmt)
  return rs.lastrowid

def update(id, name):
  conn = engine.connect()
  stmt = ("""
    UPDATE states SET 
      name='{}' 
      WHERE id={};
  """).format(name, id)
  rs = conn.execute(stmt)
  return rs

def delete(id):
  conn = engine.connect()
  stmt = ("""
    DELETE FROM states WHERE id={};
  """).format(id)
  rs = conn.execute(stmt)
  return rs

def get_state_by_id(id):
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM states WHERE id={};
  """).format(id)
  return conn.execute(stmt).fetchone()
