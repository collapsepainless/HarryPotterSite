from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'ASH\'N\'DANNY\'S\'SITE/fan_art_uploads'  # Folder where uploaded images will be stored
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # Allowed file extensions

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'art-file' in request.files:
        file = request.files['art-file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('fanart'))
    
    return 'Image upload failed'

@app.route('/fanart')
def fanart():
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    image_paths = [os.path.join(app.config['UPLOAD_FOLDER'], image) for image in images]
    return render_template('fanart.html', images=image_paths)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
