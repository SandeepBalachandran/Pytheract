import os

from flask import Flask, render_template, request

from ocr_core import ocr_core
# import cv2
# from pdf2image import convert_from_path, convert_from_bytes
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
import os

import json
from flask_cors import CORS, cross_origin

import base64
import requests
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
CORS(app)
app.secret_key = "secretkey"

app.config["MONGO_URI"] = "mongodb://localhost:27017/users"

mongo = PyMongo(app)

app.config["IMAGE_UPLOADS"] = r'D:\Experiments\sample_project\Git Projects\Pytheract\uploads'
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG", "JPG", "JPEG", "GIF"]

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


@app.route("/add", methods=["POST"])
def add_user():
    _json = request.get_json()

    _type = _json["type"]
    _img_url_old = _json["image_url_old"]
    _img_url_new = _json["image_url_new"]
    _denoise_text = _json["de_noised_text"]
    _noise_text = _json["noise_text"]

    # _name = request.args.get("name" , False)
    # _email = request.args.get("email" , False)
    # _pwd = request.args.get("password" , False)

    # _name = request.data.name
    # _email = request.data.email
    # _pwd = request.data.password

    if _type and request.method == "POST":
        # hashed_pwd = generate_password_hash(_pwd)

        id = mongo.db.user.insert(
            {
                "type": _type,
                "image_url_old": _img_url_old,
                "img_url_new": _img_url_new,
                "denoise_text": _denoise_text,
                "noise_text": _noise_text,
            }
        )
        res = jsonify("data added succesfully")
        res.status_code = 201
        return res
    else:
        return not_found()


@app.route("/denoise/documents/pix", methods=["GET"])
def get_all_users():
    users = mongo.db.user.find()
    resp = dumps(users)
    return resp


@app.route("/user/<id>", methods=["GET"])
def get_single_user(id):
    user = mongo.db.user.find_one({"_id": ObjectId(id)})
    resp = dumps(user)
    return resp


@app.route("/user/<id>", methods=["PUT"])
def update_user(id):
    _id = id
    _json = request.json
    _name = _json["name"]
    _email = _json["email"]
    _pwd = _json["password"]

    if _name and _email and _pwd and request.method == "PUT":
        hashed_pwd = generate_password_hash(_pwd)

        # id = mongo.db.user.insert({"name": _name, "email": _email, "pwd": hashed_pwd})
        id = mongo.db.user.update_one(
            {
                "_id": ObjectId(_id["$oid"] if "$oid" in _id else ObjectId(_id)),
            },
            {"$set": {"name": _name, "email": _email, "pwd": hashed_pwd}},
        )
        res = jsonify("user updated succesfully")
        res.status_code = 200
        return res
    else:
        return not_found()


@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    user = mongo.db.user.delete_one({"_id": ObjectId(id)})
    resp = jsonify({ "result":user ,"message":"User deleted succesfully"})
    resp.status_code = 200
    return resp


@app.route("/denoise/documents/pix", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if request.files:
            typename = request.form.get('type')
            image = request.files["image"]
            if image.filename == "":
                return "Image Must have a file name"
            path = app.config["IMAGE_UPLOADS"] +'/'+typename 
            if not os.path.exists(path):          
                os.makedirs(path)
            app.config["UPLOAD_FOLDER"] = path
            root = 'http://localhost:5500/Pytheract/uploads';
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            imgfullpath = root + '/' +typename+'/'+image.filename
            if typename and request.method == "POST":
                # hashed_pwd = generate_password_hash(_pwd)
                extracted_text = ocr_core(image)
                id = mongo.db.user.insert(
                    {
                        "type": typename,
                        "image_url_old": imgfullpath,
                        "img_url_new": imgfullpath,
                        "denoise_text":extracted_text,
                        "noise_text":extracted_text,
                    }
                )
                res = jsonify({"result":imgfullpath, "message":"uploaded succesfully"})
                res.status_code = 201
                return res
            else:
                return not_found()
        else:
            res = jsonify("Bad request")
            res.status_code = 400
            return res
    else:
        res = jsonify("Method Not Allowed")
        res.status_code = 405
        return res

@app.errorhandler(404)
def not_found(error=None):
    message = {"status": 400, "message": "Not found " + request.url}

    res = jsonify(message)
    res.status_code = 404
    return res

if __name__ == '__main__':
    app.run()