from flask import Flask, render_template, request, flash, url_for, redirect
from werkzeug.utils import secure_filename
import os
import cv2

# File Upload Location
UPLOAD_FOLDER = '/workspaces/codespaces-flask/Image Editing:OpenCv-Flask/static/images'

# Image extensions allowed
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'webp'}

# Creating Flask App
app = Flask(__name__)
# UploadFolder Configuration
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "Development"

# Function to validate File extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Fucntion to Process Images
def ProcessImage(filename, operation):
    # print(f'{operation}:{filename}')
    img = cv2.imread(f"static/images/{filename}")
    
    # Switch case to perform function based on requested operation
    match operation:
        # Convert to grayScale
        case "cgray":
            imgprocessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            newFilename = f"static/processed-images/{filename.split('.')[0]}-processed.{filename.split('.')[1]}"
            print(newFilename)
            cv2.imwrite(newFilename, imgprocessed)
            return newFilename
        # Convert to PNG
        case "cpng":
            newFilename = f"static/processed-images/{filename.split('.')[0]}-processed.png"
            cv2.imwrite(newFilename, img)
            return newFilename
        # Convert to WEBP
        case "cwebp":
            newFilename = f"static/processed-images/{filename.split('.')[0]}-processed.webp"
            cv2.imwrite(newFilename, img)
            return newFilename
        # Convert to JPG
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

# Function gets trigerred on FORM Submit in Homepage
@app.route("/edit", methods=['GET','POST'])
def edit():
    
    if request.method == 'POST':
        operation = request.form.get("operation")
        file = request.files['file']
        
        # If Opration not selected
        if not operation or not file.filename:
            flash('Please select both operation and image', 'error')
            return redirect(url_for('home'))
        
        if file and allowed_file(file.filename):
            # Renames file and secures it without spaces etc.
            filename = secure_filename(file.filename)
            
            # Save the file to the Upload_folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            # Send the imagefile and operation key to Process function
            filename = ProcessImage(filename, operation)
            
            flash(f"You image has been processed and is available at <a href='{filename}' target='_blank'>here</a>")
            return redirect(url_for('home'))

    return render_template("index.html")


app.run(debug=True)