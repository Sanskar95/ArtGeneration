import datetime
import json
import time

import os

from PIL import Image
from flask import Flask, request, flash, url_for, send_from_directory, render_template
from nst_utils import *

import numpy as np
import tensorflow as tf

# this is how we initialize a flask application
from werkzeug.utils import redirect, secure_filename

app = Flask(__name__,template_folder='template')
app.secret_key = "super secret key"



UPLOAD_FOLDER='/Users/z002r1y/PycharmProjects/ArtGeneration/output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_DIRECTORY='/Users/z002r1y/PycharmProjects/ArtGeneration/contentImage'


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

    file = open("/Users/z002r1y/PycharmProjects/ArtGeneration/styleId/id.txt", "w")
    file.write(str(id))


    print(id)
    return "d"


@app.route("/up", methods=['POST'])
def upload_filex():
    
    file = request.files['image']

    basewidth = 400
    img = Image.open(file)
   
    hsize = 300
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save('/Users/z002r1y/PycharmProjects/ArtGeneration/contentImage/photo.jpg')
    # f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    # file.save(f)

    return render_template('index.html')






@app.route("/process", methods=["GET"])
def yeye():

    os.system("source env/bin/activate")
    os.system("python art.py")
    return "d"


@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)


@app.route('/files/<filename>', methods=['POST'])
def post_file(filename):
    """Upload a file."""

    if '/' in filename:
        # Return 400 BAD REQUEST
        os.abort(400, 'no subdirectories directories allowed')

    # with open(os.path.join(UPLOAD_DIRECTORY, filename), 'wb') as fp:
    #     fp.write(request.data)
    req_data = request.get_json()

    id = req_data['id'];

    file = open("/Users/z002r1y/PycharmProjects/ArtGeneration/contentId/id.txt", "w")
    file.write(str(id))


    # Return 201 CREATED
    return '', 201


if __name__ == "__main__":
    """
    this is run when the script is started.
    """

    # this is how we run the flask server, once the script is run
    app.run(host='0.0.0.0', threaded=True)