## Migraciones

Archivo <b>.env</b>

    DB_USER="root"
    DB_PASS="123"
    DB_HOST="127.0.0.1"
    DB_PORT=5433
    DB_NAME="tickets"
    DB="sqlite:///db/app.db"

Migraciones con DBMATE - app:

    $ dbmate -d "db/migrations" -e "DB" new <<nombre_de_migracion>>
    $ dbmate -d "db/migrations" -e "DB" up
    $ dbmate -d "db/migrations" -e "DB" rollback

Backup SQLite

    $ sqlite3 app.db .dump > dbname.bak

---

Fuentes:

+ https://github.com/pepeul1191/tutorial-flask