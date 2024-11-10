from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from config import SELFIE_FOLDER, GROUP_PHOTO_FOLDER
from utils.face_utils import encode_face
import face_recognition

upload_routes = Blueprint('upload_routes', __name__)

@upload_routes.route('/upload_selfie', methods=['POST'])
def upload_selfie():
    if 'selfie' not in request.files or 'name' not in request.form:
        return jsonify({"error": "Selfie ve isim gerekli"}), 400

    selfie_file = request.files['selfie']
    name = request.form['name']
    filename = secure_filename(selfie_file.filename)
    filepath = os.path.join(SELFIE_FOLDER, filename)
    selfie_file.save(filepath)

    image = face_recognition.load_image_file(filepath)
    encoding = encode_face(image)
    if encoding is None:
        os.remove(filepath)
        return jsonify({"error": "Selfie'de yüz bulunamadı"}), 400


    return jsonify({"message": "Selfie başarıyla yüklendi"}), 200

@upload_routes.route('/upload_group_photos', methods=['POST'])
def upload_group_photos():
    if 'group_photos' not in request.files:
        return jsonify({"error": "Grup fotoğrafları gerekli"}), 400

    group_photos = request.files.getlist('group_photos')

    for photo in group_photos:
        filename = secure_filename(photo.filename)
        filepath = os.path.join(GROUP_PHOTO_FOLDER, filename)
        photo.save(filepath)

    return jsonify({"message": "Grup fotoğrafları başarıyla yüklendi"}), 200
