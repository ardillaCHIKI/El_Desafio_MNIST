import numpy as np
import tensorflow as tf
from PIL import Image

modelo = tf.keras.models.load_model("modelo_mnist.h5")

def predecir_imagen(imagen):
    imagen = imagen.convert("L").resize((28, 28))
    imagen = np.array(imagen) / 255.0
    imagen = imagen.reshape(1, 28, 28, 1)
    prediccion = modelo.predict(imagen)
    return np.argmax(prediccion)
