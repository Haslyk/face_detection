from flask import Flask, render_template, send_from_directory
from routes.upload_routes import upload_routes
from routes.processing_routes import processing_routes
from config import PROCESSED_FOLDER

app = Flask(__name__)

app.register_blueprint(upload_routes)
app.register_blueprint(processing_routes)

# Ana sayfa rotası
@app.route('/')
def index():
    return render_template('index.html')

# İşlenmiş fotoğrafları sunma rotası
@app.route('/processed/<filename>')
def processed(filename):
    return send_from_directory(PROCESSED_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=False)