from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
import base64

app = Flask(__name__)
model = load_model('mnist_model.keras')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['image']
    image = Image.open(io.BytesIO(base64.b64decode(data.split(',')[1]))).convert('L')
    image = image.resize((28, 28))
    image = np.array(image) / 255.0
    image = image.reshape(1, 28, 28, 1)
    prediction = model.predict(image)
    return jsonify({'resultado': int(np.argmax(prediction))})

if __name__ == '__main__':
    app.run(debug=True)