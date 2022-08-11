from lorem_text import lorem
import traceback
import random
import sqlite3

def fill_tickets():
  con = sqlite3.connect('app.db')
  try:
    cur = con.cursor()
    for i in range(10000):
      created = "datetime(strftime('%s', '2020-01-31 00:00:00') + abs(random() % (strftime('%s', '2020-01-31 23:59:59') - strftime('%s', '2022-07-30 00:00:00'))), 'unixepoch')"
      edited = "datetime(strftime('%s', '2020-01-31 00:00:00') + abs(random() % (strftime('%s', '2020-01-31 23:59:59') - strftime('%s', '2022-07-30 00:00:00'))), 'unixepoch')"
      resume = lorem.words(random.randint(7, 13))
      description = lorem.paragraphs(random.randint(1, 2))
      worker_id = random.randint(1,100)
      priority_id = random.randint(1,3)
      branch_id = random.randint(1,36)
      state_id = random.randint(1,4)
      ticket_type_id = random.randint(1,3)
      query = """
        INSERT INTO tickets 
          (created, edited, resume, description, worker_id, priority_id, branch_id, state_id, ticket_type_id) 
          VALUES 
          ({created},{edited},'{resume}','{description}',{worker_id},{priority_id},{branch_id},{state_id},{ticket_type_id});
        """.format(
          created=created, 
          edited=edited, 
          resume=resume, 
          description=description, 
          worker_id=worker_id, 
          priority_id=priority_id, 
          branch_id=branch_id, 
          state_id=state_id, 
          ticket_type_id=ticket_type_id
        )
      cur.execute(query)
    con.commit()
  except:
    traceback.print_exc()
  finally:
    con.close()
  
def inserts_tickets():
  try:
    query = """
      INSERT INTO tickets 
        (created, edited, resume, description, worker_id, priority_id, branch_id, state_id, ticket_type_id) 
        VALUES 
      """
    for i in range(10000):
      created = "datetime(strftime('%s', '2020-01-31 00:00:00') + abs(random() % (strftime('%s', '2020-01-31 23:59:59') - strftime('%s', '2022-07-30 00:00:00'))), 'unixepoch')"
      edited = "datetime(strftime('%s', '2020-01-31 00:00:00') + abs(random() % (strftime('%s', '2020-01-31 23:59:59') - strftime('%s', '2022-07-30 00:00:00'))), 'unixepoch')"
      resume = lorem.words(random.randint(7, 13))
      description = lorem.paragraphs(random.randint(1, 2))
      worker_id = random.randint(1,100)
      priority_id = random.randint(1,3)
      branch_id = random.randint(1,36)
      state_id = random.randint(1,4)
      ticket_type_id = random.randint(1,3)
      query = query + """
          ({created},{edited},'{resume}','{description}',{worker_id},{priority_id},{branch_id},{state_id},{ticket_type_id}),
        """.format(
          created=created, 
          edited=edited, 
          resume=resume, 
          description=description, 
          worker_id=worker_id, 
          priority_id=priority_id, 
          branch_id=branch_id, 
          state_id=state_id, 
          ticket_type_id=ticket_type_id
        )
    f = open("demofile3.txt", "w")
    f.write(query)
    f.close()
  except:
    traceback.print_exc()
  finally:
    pass

inserts_tickets()