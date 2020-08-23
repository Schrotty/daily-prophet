import os
import sqlite3

from flask import Flask
from werkzeug.exceptions import abort
from werkzeug.wrappers import Response


def row_fac(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d


class Prophet:
    def __init__(self):
        if not os.path.exists('dist/storage'):
            os.mkdir('dist/storage')

        with sqlite3.connect('media.db') as connection:
            connection.execute('CREATE TABLE IF NOT EXISTS media '
                               '(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
                               'filename TEXT NOT NULL, type TEXT NOT NULL)')

        self.media = {}
        self.read_media()

    def read_media(self):
        with sqlite3.connect('media.db') as connection:
            connection.row_factory = row_fac
            self.media = connection.execute("SELECT id, filename, type FROM media").fetchall()

        return self.media

    def add_media(self, f, t):
        with sqlite3.connect('media.db') as connection:
            connection.execute("INSERT INTO media (filename, type) VALUES (?, ?)", (f, t))

        return self.media

    def delete_media(self, identifier):
        with sqlite3.connect('media.db') as connection:
            file = connection.execute("SELECT filename FROM media WHERE id={0}".format(identifier)).fetchone()
            if file is None:
                return abort(404)

            os.remove("dist/storage/{0}".format(file[0]))
            connection.execute("DELETE FROM media WHERE id=?", (identifier,))

        return Response("", 200)
