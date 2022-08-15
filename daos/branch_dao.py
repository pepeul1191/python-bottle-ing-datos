from configs.database import engine


def get_lima_branches():
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM branches WHERE branch_type_id=1
  """).format(1)
  return [dict(r) for r in conn.execute(stmt)]

def get_province_branches():
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM branches WHERE branch_type_id=2
  """).format(1)
  return [dict(r) for r in conn.execute(stmt)]