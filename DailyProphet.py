import os

from DataManager import Prophet
from flask import request, jsonify, flash, redirect, Flask
from werkzeug.utils import secure_filename

UPLOAD_DIR = 'dist/storage'
EXTENSIONS = {'png', 'jpeg', 'jpg', 'gif', 'mp4'}

app = Flask(__name__, static_folder='dist', static_url_path='/')
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR

prophet = Prophet()


@app.route('/')
def hello_world():
    return app.send_static_file("index.html")


@app.route('/media/', methods=['GET', 'POST'])
@app.route('/media/<identifier>', methods=['DELETE'])
def media(identifier=None):
    if request.method == 'DELETE':
        return prophet.delete_media(identifier)

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify(prophet.add_media(filename, file_type(filename)))

    return jsonify(prophet.read_media())


@app.route('/heartbeat')
def activate_media():
    return "<3"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in EXTENSIONS


def file_type(filename):
    mime = filename.rsplit('.', 1)[1].lower()
    if mime in ['mp4']:
        return 'video'

    return 'image'


if __name__ == '__main__':
    app.run()
