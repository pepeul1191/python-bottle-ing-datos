CREATE TABLE IF NOT EXISTS "schema_migrations" (version varchar(255) primary key);
CREATE TABLE branch_types (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name	VARCHAR(11) NOT NULL
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE branches (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name	VARCHAR(30) NOT NULL,
  address	VARCHAR(70) NOT NULL,
  phone	VARCHAR(25),
  whatsapp	VARCHAR(25),
  branch_type_id	INT,
  FOREIGN KEY(branch_type_id) REFERENCES branch_types ( id ) ON DELETE CASCADE
);
CREATE TABLE ticket_types (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name	VARCHAR(25) NOT NULL
);
CREATE TABLE priorities (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name	VARCHAR(25) NOT NULL
);
CREATE TABLE states (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name	VARCHAR(25) NOT NULL
);
CREATE TABLE positions (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name	VARCHAR(25) NOT NULL
);
CREATE TABLE workers (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  names	VARCHAR(45) NOT NULL,
  last_names	VARCHAR(45) NOT NULL,
	email	VARCHAR(45) NOT NULL,
  phone	VARCHAR(25),
  position_id	INT,
  FOREIGN KEY(position_id) REFERENCES positions ( id ) ON DELETE CASCADE
);
CREATE TABLE branches_workers (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  worker_id	INT,
  branch_id	INT,
  FOREIGN KEY(worker_id) REFERENCES workers ( id ) ON DELETE CASCADE,
  FOREIGN KEY(branch_id) REFERENCES branches ( id ) ON DELETE CASCADE
);
CREATE TABLE users (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "user"	VARCHAR(145) NOT NULL,
  password	VARCHAR(145) NOT NULL,
	last_login	TIMESTAMP,
  worker_id	INT,
  activation_key VARCHAR(25),
  reset_key VARCHAR(25),
  FOREIGN KEY(worker_id) REFERENCES workers ( id ) ON DELETE CASCADE
);
CREATE TABLE service_types (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name	VARCHAR(40) NOT NULL
);
CREATE TABLE tickets (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  created	TIMESTAMP NOT NULL,
  edited TIMESTAMP,
	resume	VARCHAR(30) NOT NULL,
  description	TEXT NOT NULL,
  worker_id	INT,
  priority_id	INT,
  branch_id	INT,
  state_id	INT,
  ticket_type_id	INT,
  FOREIGN KEY(worker_id) REFERENCES workers ( id ) ON DELETE CASCADE,
  FOREIGN KEY(priority_id) REFERENCES priorities ( id ) ON DELETE CASCADE,
  FOREIGN KEY(branch_id) REFERENCES branches ( id ) ON DELETE CASCADE,
  FOREIGN KEY(state_id) REFERENCES states ( id ) ON DELETE CASCADE,
  FOREIGN KEY(ticket_type_id) REFERENCES ticket_types ( id ) ON DELETE CASCADE
);
CREATE TABLE service_tickets (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  ticket_id	INT,
	FOREIGN KEY(ticket_id) REFERENCES tickets ( id ) ON DELETE CASCADE
);
CREATE TABLE service_tickets_types (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  service_ticket_id	INT,
  service_type_id	INT,
  FOREIGN KEY(service_ticket_id) REFERENCES service_tickets ( id ) ON DELETE CASCADE,
  FOREIGN KEY(service_type_id) REFERENCES service_types ( id ) ON DELETE CASCADE
);
CREATE TABLE ticket_files (
	id	SERIAL PRIMARY KEY,
  description	VARCHAR(150) NOT NULL,
  url	VARCHAR(60) NOT NULL,
  ticket_id INTEGER NOT NULL,
  FOREIGN KEY (ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);
CREATE VIEW vw_tickets AS
  SELECT
    T.id, T.resume,
      TO_CHAR(T.created,'%Y/%m/%d') AS created, TO_CHAR(T.edited,'%Y/%m/%d') AS edited,
      T.worker_id, CONCAT(W.last_names, ', ',W.names) AS worker_name,
      T.priority_id, P.name AS priority_name,
      T.state_id, S.name AS state_name,
      T.ticket_type_id, TT.name AS ticket_type_name,
      T.branch_id, CONCAT(BT.name, ', ',B.name) AS branch_name
  FROM tickets T
  JOIN workers W ON W.id = T.worker_id
  JOIN priorities P ON P.id = T.priority_id
  JOIN states S ON S.id = T.state_id
  JOIN branches B ON B.id = T.branch_id
  JOIN ticket_types TT ON TT.id = T.ticket_type_id
  JOIN branch_types BT ON B.branch_type_id = BT.id
  ORDER BY T.created;
-- Dbmate schema migrations
INSERT INTO "schema_migrations" (version) VALUES
  ('20220726004204'),
  ('20220726004355'),
  ('20220726004657'),
  ('20220726010927'),
  ('20220726012021'),
  ('20220726012027'),
  ('20220726012215'),
  ('20220726012220'),
  ('20220726012231'),
  ('20220726012236'),
  ('20220726013756'),
  ('20220726013801'),
  ('20220726013802'),
  ('20220726014143'),
  ('20220726014334'),
  ('20220726014954'),
  ('20220726015002'),
  ('20220726015834'),
  ('20220726020758'),
  ('20220726020959'),
  ('20220726230401'),
  ('20220804151900'),
  ('20220804160935'),
  ('20220811183224');
