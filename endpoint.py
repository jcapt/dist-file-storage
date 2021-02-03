import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from uuid import uuid4
from registry import FileRegistry

UPLOAD_FOLDER = './tmpfiles'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'

filereg = FileRegistry()

@app.route('/<entity_id>', methods=['GET', 'POST'])
def upload_file(entity_id):
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return "", 400
        file = request.files['file']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'] + "/" + entity_id)

        if not os.path.isdir(filepath):
            os.mkdir(filepath)

        if file:
            filename = secure_filename(file.filename)
            filename = gen_unique_filename(filename)
            file.save(filepath + filename)
            filereg.register(entity_id, filename)
            return "", 201

@app.route("/<entity_id>/<filename>", methods=["DELETE"])
def delete_file(entity_id, filename):
    filereg.deregister(entity_id, filename)
    return "", 204

def gen_unique_filename(filename):
    return filename + "." + str(uuid4())

