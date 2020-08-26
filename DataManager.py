import os
import sqlite3

from dotenv import load_dotenv
from moviepy.editor import VideoFileClip
from werkzeug.exceptions import abort


def row_fac(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d


class Prophet:
    def __init__(self):
        load_dotenv(dotenv_path='.prophetenv')
        self.database = 'dist/storage/_index.db'
        self.last_rand = -1

        if not os.path.exists('dist/storage'):
            os.mkdir('dist/storage')

        with sqlite3.connect(self.database) as connection:
            connection.execute('CREATE TABLE IF NOT EXISTS media '
                               '(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
                               'filename TEXT NOT NULL,'
                               'type TEXT NOT NULL, duration INTEGER)')

        self.media = {}
        self.read_media()

    def read_media(self):
        with sqlite3.connect(self.database) as connection:
            connection.row_factory = row_fac
            self.media = connection.execute("SELECT id, filename, type FROM media").fetchall()

        return self.media

    def random(self):
        with sqlite3.connect(self.database) as connection:
            connection.row_factory = row_fac
            random = connection.execute(
                "SELECT id, filename, type, duration FROM media ORDER BY RANDOM() LIMIT 1").fetchone()

        if random is not None:
            if random['duration'] == 0:
                random['duration'] = int(os.getenv("PROPHET_IMG_TIMEOUT", 60))

        return random

    def add_media(self, f, t):
        length = 0
        if t == 'video':
            length = VideoFileClip("{0}/dist/storage/{1}".format(os.getcwd(), f)).duration

        with sqlite3.connect(self.database) as connection:
            connection.execute("INSERT INTO media (filename, type, duration) VALUES (?, ?, ?)", (f, t, length))

        return self.media

    def delete_media(self, identifier):
        with sqlite3.connect(self.database) as connection:
            file = connection.execute("SELECT filename FROM media WHERE id={0}".format(identifier)).fetchone()
            if file is None:
                return abort(404)

            try:
                os.remove("{0}/dist/storage/{1}".format(os.getcwd(), file[0]))
            except OSError:
                pass

            connection.execute("DELETE FROM media WHERE id=?", (identifier,))

        return self.read_media()
