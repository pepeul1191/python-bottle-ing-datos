from configs.database import engine

def get_worker_branches(branch_type_id, worker_id):
  conn = engine.connect()
  stmt = ("""
    SELECT T.id AS id, T.name AS name, (CASE WHEN (P.exist = 1) THEN 1 ELSE 0 END) AS exist FROM
    (
      SELECT id, name, 0 AS exist FROM branches WHERE branch_type_id = {}
    ) T 
    LEFT JOIN 
    (
      SELECT PT.id, PT.name, 1 AS exist FROM 
      branches PT INNER JOIN branches_workers PTP ON
      PT.id = PTP.branch_id
      WHERE PTP.worker_id = {}
    ) P 
    ON P.id = T.id
  """).format(branch_type_id, worker_id)
  return [dict(r) for r in conn.execute(stmt)]

def get_record_by_ids(worker_id, branch_id):
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM branches_workers WHERE branch_id={} AND worker_id={};
  """).format(branch_id, worker_id)
  return conn.execute(stmt).fetchone()

def create(worker_id, branch_id):
  conn = engine.connect()
  stmt = ("""
    INSERT INTO branches_workers (branch_id, worker_id) 
      VALUES ({}, {});
  """).format(branch_id, worker_id)
  rs = conn.execute(stmt)
  return rs.lastrowid

def delete(worker_id, branch_id):
  conn = engine.connect()
  stmt = ("""
    DELETE FROM branches_workers WHERE worker_id={} AND branch_id={};
  """).format(worker_id, branch_id)
  rs = conn.execute(stmt)
  return rs