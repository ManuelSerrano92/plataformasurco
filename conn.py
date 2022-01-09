import sqlite3
from sqlite3 import Error
from flask import current_app, g

def conn():
    try:
        if "db" not in g:
            g.db=sqlite3.connect("db/surcolombiana.db")
    except Error:
        print(Error)
    return g.db

def closeConn():
    db = g.pop("db", None)
    if db is not None:
        db.close()
