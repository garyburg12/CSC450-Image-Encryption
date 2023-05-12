from flask import Flask, render_template, request, jsonify, render_template, redirect, url_for
from PIL import Image
from io import BytesIO
import os
import base64
import io

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/encryption', methods=['POST'])
def encryption():
    if "image" not in request.files:
        return redirect(request.url)
    
    image = Image.open(request.files["image"])

    # Calling encryption function here
    encrypted_image = image.convert("L")
    encrypted_image_url = save_image(encrypted_image)
    
    return jsonify({"imageUrl": encrypted_image_url})

@app.route("/result")
def result():
    image_url = request.args.get("imageUrl")
    return render_template("result.html", imageUrl = image_url)

def save_image(image):
    filename = "encryptTest.jpg"
    path = os.path.join("static", filename)

    if os.path.exists(path):
        os.remove(path)

    image.save("static/" + filename)
    
    return url_for("static", filename=filename)

if __name__ == '__main__':
   app.run()