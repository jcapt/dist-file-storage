import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from uuid import uuid4

UPLOAD_FOLDER = './tmpfiles'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'

@app.route('/<entity_id>', methods=['GET', 'POST'])
def upload_file(entity_id):
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return "", 400
        file = request.files['file']

        if not os.path.isdir("./" + entity_id):
            os.mkdir(app.config['UPLOAD_FOLDER'] + "/" + entity_id)

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/" + entity_id, gen_unique_filename(filename)))
            return "", 201


def gen_unique_filename(filename):
    return filename + "." + str(uuid4())

