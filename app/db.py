import click
from flask import current_app, g
from flask.cli import with_appcontext

import sqlite3


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    
    database_path = os.path.join(os.path.dirname(__file__), 'instance/tourdeflask.sqlite')
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    schema_path = os.path.join(os.path.dirname(__file__), 'app/schema.sql')
    with open(schema_path, 'r') as f:
        cursor.executescript(f.read())

    connection.commit()
    connection.close()

    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    Definujeme příkaz příkazové řádky
    """
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
