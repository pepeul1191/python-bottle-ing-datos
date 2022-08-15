from configs.database import engine

def get_all():
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM branch_types
  """).format(1)
  return [dict(r) for r in conn.execute(stmt)]
