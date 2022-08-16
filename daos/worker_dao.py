#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil
from configs.database import engine

def get_all(step, page):
  conn = engine.connect()
  # count
  stmt = ("""
    SELECT COUNT(*) AS n FROM workers 
  """).format()
  count = conn.execute(stmt).fetchone()['n']
  # page
  pages = ceil(count / step)
  offset = (page - 1) * step
  conn = engine.connect()
  stmt = ("""
    SELECT W.id, W.names, W.last_names, W.email, W.phone, W.position_id, P.name AS position_name 
    FROM workers W 
    JOIN positions P ON P.id = W.position_id 
    ORDER BY W.id 
    LIMIT {} OFFSET {};
  """).format(step, offset)
  resp = {
    'pages': pages,
    'workers': [dict(r) for r in conn.execute(stmt)]
  }
  return resp

def get_worker_by_id(id):
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM workers WHERE id={};
  """).format(id)
  return conn.execute(stmt).fetchone()

def create(names, last_names, phone, email, position_id):
  conn = engine.connect()
  stmt = ("""
    INSERT INTO workers (names, last_names, phone, email, position_id) 
      VALUES ('{}','{}','{}','{}',{});
  """).format(names, last_names, phone, email, position_id)
  rs = conn.execute(stmt)
  return rs.lastrowid

def update(id, names, last_names, phone, email, position_id):
  conn = engine.connect()
  stmt = ("""
    UPDATE workers SET 
      names='{}',  last_names='{}',  phone='{}',  email='{}', position_id={} 
      WHERE id={};
  """).format(names, last_names, phone, email, position_id, id)
  rs = conn.execute(stmt)
  return rs

def update_image_url(id, image_url):
  conn = engine.connect()
  stmt = ("""
    UPDATE workers SET 
      image_url='{}' WHERE id={};
  """).format(image_url, id)
  rs = conn.execute(stmt)
  return rs

def delete(id):
  conn = engine.connect()
  stmt = ("""
    DELETE FROM workers WHERE id={};
  """).format(id)
  rs = conn.execute(stmt)
  return rs