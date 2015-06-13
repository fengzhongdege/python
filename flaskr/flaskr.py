__author__ = 'kunchen'
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from contextlib import closing

DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'es123'
USERNAME = 'admin'
PASSWORD = '111'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

if __name__ == '__main__':
    app.run('0.0.0.0', 5001, debug=True)