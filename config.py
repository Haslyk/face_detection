import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
SELFIE_FOLDER = os.path.join(UPLOAD_FOLDER, 'selfies')
GROUP_PHOTO_FOLDER = os.path.join(UPLOAD_FOLDER, 'group_photos')
PROCESSED_FOLDER = os.path.join(BASE_DIR, 'processed')

# Klasörlerin varlığını kontrol et ve oluştur
for folder in [UPLOAD_FOLDER, SELFIE_FOLDER, GROUP_PHOTO_FOLDER, PROCESSED_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)
