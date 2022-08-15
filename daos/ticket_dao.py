#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil
from configs.database import engine

def get_all(step, page):
  conn = engine.connect()
  # count
  stmt = ("""
    SELECT COUNT(*) AS n FROM vw_tickets 
  """).format()
  count = conn.execute(stmt).fetchone()['n']
  # page
  pages = ceil(count / step)
  offset = (page - 1) * step
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM vw_tickets 
    ORDER BY id 
    LIMIT {} OFFSET {};
  """).format(step, offset)
  resp = {
    'pages': pages,
    'tickets': [dict(r) for r in conn.execute(stmt)]
  }
  return resp