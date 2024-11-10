# routes/processing_routes.py
from flask import Blueprint, jsonify
import os
from config import SELFIE_FOLDER, GROUP_PHOTO_FOLDER, PROCESSED_FOLDER
from utils.face_utils import encode_face, compare_faces
from utils.image_utils import draw_faces
import face_recognition

processing_routes = Blueprint('processing_routes', __name__)

@processing_routes.route('/process_images', methods=['GET'])
def process_images():
    selfies = []
    for filename in os.listdir(SELFIE_FOLDER):
        filepath = os.path.join(SELFIE_FOLDER, filename)
        image = face_recognition.load_image_file(filepath)
        encoding = encode_face(image)
        if encoding is not None:
            name = os.path.splitext(filename)[0]
            selfies.append({'name': name, 'encoding': encoding})

    results = []
    for group_photo_filename in os.listdir(GROUP_PHOTO_FOLDER):
        group_photo_path = os.path.join(GROUP_PHOTO_FOLDER, group_photo_filename)
        group_image = face_recognition.load_image_file(group_photo_path)
        group_encodings = face_recognition.face_encodings(group_image)
        face_locations = face_recognition.face_locations(group_image)

        matches = []
        distances = []
        names = []

        for encoding in group_encodings:
            match_found = False
            for selfie in selfies:
                result, distance = compare_faces(selfie['encoding'], [encoding])
                if result[0] and distance[0] <= 0.5:  # %50 doğruluk oranı filtresi
                    matches.append(True)
                    distances.append(distance[0])
                    names.append(selfie['name'])
                    match_found = True
                    break
            if not match_found:
                matches.append(False)
                distances.append(1.0)
                names.append("Unknown")

        processed_image = draw_faces(group_image, face_locations, matches, distances, names)
        processed_filename = f"processed_{group_photo_filename}"
        processed_image.save(os.path.join(PROCESSED_FOLDER, processed_filename))

        results.append({
            "group_photo": group_photo_filename,
            "processed_photo": processed_filename
        })

    return jsonify(results), 200
