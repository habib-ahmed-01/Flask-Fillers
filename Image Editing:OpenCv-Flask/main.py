from flask import Flask, render_template, request, flash, url_for, redirect
from werkzeug.utils import secure_filename
import os
import cv2

UPLOAD_FOLDER = '/workspaces/codespaces-flask/Image Editing:OpenCv-Flask/static/images'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'webp'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "Development"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def ProcessImage(filename, operation):
    # print(f'{operation}:{filename}')
    img = cv2.imread(f"static/images/{filename}")
    match operation:
        case "cgray":
            imgprocessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            newFilename = f"static/processed-images/{filename.split('.')[0]}-processed.{filename.split('.')[1]}"
            print(newFilename)
            cv2.imwrite(newFilename, imgprocessed)
            return newFilename
        case "cpng":
            newFilename = f"static/processed-images/{filename.split('.')[0]}-processed.png"
            cv2.imwrite(newFilename, img)
            return newFilename
        case "cwebp":
            newFilename = f"static/processed-images/{filename.split('.')[0]}-processed.webp"
            cv2.imwrite(newFilename, img)
            return newFilename
        case "cjpg":
            newFilename = f"static/processed-images/{filename.split('.')[0]}-processed.jpg"
            cv2.imwrite(newFilename, img)
            return newFilename

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/edit", methods=['GET','POST'])
def edit():
    if request.method == 'POST':
        operation = request.form.get("operation")
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "redirect(request.url)"
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return "redirect(request.url)"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filename = ProcessImage(filename, operation)
            flash(f"You image has been processed and is available at <a href='{filename}' target='_blank'>here</a>")
            return redirect(url_for('home'))

    return render_template("index.html")

app.run(debug=True)