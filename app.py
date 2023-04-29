from flask import Flask, render_template, request, jsonify
from PIL import Image
from io import BytesIO
import base64
import io
import imageEncryption
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/encryption', methods=['POST'])
def encryption():
    image_file = request.files['image']
    image_data = io.BytesIO(image_file.read())
    image = Image.open(image_data)
    # encryption
    # encrypted = imageEncryption(image)
    print(image_data)
    return "image uploaded"


if __name__ == '__main__':
    app.run()
