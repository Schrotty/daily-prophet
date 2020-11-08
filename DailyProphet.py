import os

from flask import request, jsonify, flash, redirect, Flask
from werkzeug.utils import secure_filename

from DataManager import Prophet
from DisplayManager import DisplayManager

UPLOAD_DIR = 'dist/storage'
EXTENSIONS = {'png', 'jpeg', 'jpg', 'gif', 'mp4', 'mov'}
VIDEO_EXTS = {'mp4', 'mov'}

app = Flask(__name__, static_folder="dist/", static_url_path="/")
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR

prophet = Prophet()
display = DisplayManager()


@app.route('/')
@app.route('/gallery', methods=['GET', 'POST'])
def hello_world():
    if request.path.endswith('/gallery'):
        display.activate()

    return app.send_static_file("public/index.html")


@app.route('/media/', methods=['GET', 'POST'])
@app.route('/media/random/')
@app.route('/media/<identifier>', methods=['DELETE', 'PUT'])
def media(identifier=None):
    if request.method == 'DELETE':
        return jsonify(prophet.delete_media(identifier))

    if request.method == 'PUT':
        return jsonify(prophet.update_media(identifier))

    if request.method == 'POST':
        if 'file[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        for file in request.files.getlist("file[]"):
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                prophet.add_media(filename, file_type(filename))

    if request.path.endswith('random/'):
        return jsonify(prophet.random())

    return jsonify(prophet.read_media())


@app.route('/heartbeat')
def activate_media():
    return "<3"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in EXTENSIONS


def file_type(filename):
    mime = filename.rsplit('.', 1)[1].lower()
    if mime in VIDEO_EXTS:
        return 'video'

    return 'image'


if __name__ == '__main__':
    app.run()
