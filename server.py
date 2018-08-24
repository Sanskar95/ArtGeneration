import datetime
import json
import time

import os
from flask import Flask, request, flash, url_for, send_from_directory, render_template
from nst_utils import *

import numpy as np
import tensorflow as tf

# this is how we initialize a flask application
from werkzeug.utils import redirect, secure_filename

app = Flask(__name__,template_folder='template')
app.secret_key = "super secret key"
UPLOAD_FOLDER="/Users/z002r1y/PycharmProjects/ArtGeneration/output"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER






UPLOAD_FOLDER='/Users/z002r1y/PycharmProjects/ArtGeneration/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

# @app.route("/timestamp", methods=["GET"])
# def get_timesptamp_millis():
#     return "kewjdgbjhb"
#
# @app.route("/img")
# def hello():
#     message = "Hello, World"
#     return render_template('index.html', message=message)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

j=0
@app.route("/json", methods=["POST"])
def json_example():
    req_data = request.get_json()

    id = req_data['id'];

    file = open("/Users/z002r1y/PycharmProjects/ArtGeneration/id/id.txt", "w")
    file.write(str(id))


    print(id)
    return "d"


@app.route("/process", methods=["GET"])
def yeye():

    os.system("source env/bin/activate")
    os.system("python art.py")
    return "d"






#
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     file = request.files['file']
#     f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#     file.save(f)
#
#     return "file uploaded successfully"


if __name__ == "__main__":
    """
    this is run when the script is started.
    """

    # this is how we run the flask server, once the script is run
    app.run(host='0.0.0.0', threaded=True)