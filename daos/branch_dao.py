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

def get_branch_by_id(id):
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM branches WHERE id={};
  """).format(id)
  return [dict(r) for r in conn.execute(stmt)][0]

