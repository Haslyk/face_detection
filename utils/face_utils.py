import face_recognition

def encode_face(image):
    encodings = face_recognition.face_encodings(image)
    if len(encodings) == 0:
        return None
    return encodings[0]

def compare_faces(known_encoding, unknown_encodings, tolerance=0.5):
    results = face_recognition.compare_faces(unknown_encodings, known_encoding, tolerance)
    distances = face_recognition.face_distance(unknown_encodings, known_encoding)
    return results, distances
