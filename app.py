import os

from flask import Flask, render_template, request

from ocr_core import ocr_core
import cv2
from pdf2image import convert_from_path, convert_from_bytes


UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home_page():
    # images = convert_from_path('./static/uploads/sample.pdf')
    # print(images)
    return render_template('index.html')

@app.route('/detect')
def detect():
    path ='./static/uploads/preview.png'
    original_image = cv2.imread(path)
    # imread() function, along with the path to the image we want to process. 
    # The imread() function simply loads the image from the specified file in an ndarray. 
    # If the image could not be read, for example in case of a missing file or an unsupported format, the function will return None.
    return render_template('detect.html',msg =path,something=original_image)


@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):
            file.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, file.filename))

            # call the OCR function on it
            extracted_text = ocr_core(file)

            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully Processed',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run()