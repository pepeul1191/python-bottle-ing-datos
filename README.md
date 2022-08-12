## Base de Datos

Instalar y activar el ambiente virtual:

    $ sudo apt install python3-virtualenv python3-venv
    $ python3 -m venv ./env
    $ source env/bin/activate

Arrancar aplicación con servidor Werkzeug:

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    $ mkdir tmp
    $ python app.py

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
+ https://pypi.org/project/lorem-text/
+ https://github.com/pepeul1191/python-accesos-v2

