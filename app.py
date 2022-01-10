# app.py
from flask import Flask, render_template, flash, request, redirect
from werkzeug.utils import secure_filename
import os
#import magic
import urllib.request

app = Flask(__name__)

UPLOAD_FOLDER = 'static/'

app.secret_key = "zWIm007r3dkv9Nfv9jV2uaNRrGkqGzMu"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the files part
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('files[]')
        # Check if files has more than 3 items
        if(len(files) > 3):
            flash('You cannot select more than 3 images')
            return redirect(request.url)
        # Delete the images in static/ before adding new ones
        for root, dirs, fichiers in os.walk(UPLOAD_FOLDER):
            for fichier in fichiers:
                os.remove(os.path.join(root, fichier))
        # Add new images
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File(s) successfully uploaded')
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
