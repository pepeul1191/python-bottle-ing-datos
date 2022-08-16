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