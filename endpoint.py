import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from uuid import uuid4
from registry import FileRegistry
from fileutils import gen_unique_filename
import json

UPLOAD_FOLDER = './tmpfiles'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'

filereg = FileRegistry()

@app.route('/<entity_id>', methods=['GET', 'POST'])
def upload_file(entity_id):
    if 'file' not in request.files:
        flash('No file part')
        return "", 400
    file = request.files['file']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'] + "/" + entity_id)

    if not os.path.isdir(filepath):
        os.mkdir(filepath)

    if file:
        original_filename = file.filename
        filename = secure_filename(file.filename)
        filename, uuid = gen_unique_filename(filename)
        file.save(filepath + "/" + filename)
        filereg.register(entity_id, uuid, { "original_filename": original_filename })
        return uuid, 201

@app.route("/<entity_id>/<filename>", methods=["DELETE"])
def delete_file(entity_id, filename):
    filereg.deregister(entity_id, filename)
    return "", 204

@app.route("/<entity_id>/<uuid>", methods=["GET"])
def download_file(entity_id, uuid):
    metadata = filereg.get_file_metadata(entity_id, uuid)
    metadata = json.loads(metadata)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'] + "/" + entity_id)
    return send_from_directory(filepath, metadata["original_filename"] + "." + uuid, as_attachment=True)

