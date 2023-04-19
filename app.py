from flask import Flask, render_template, request, jsonify
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
if __name__ == '__main__':
   app.run()


@app.route('/encryption', methods=['get'])
def encryption():
    return "ooowweee"
