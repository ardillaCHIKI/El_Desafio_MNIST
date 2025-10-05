import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps

st.title("Clasificador MNIST con Streamlit")

# Cargar modelo entrenado
try:
    model = load_model("modelo_final.h5")
    st.success("Modelo cargado correctamente.")
except:
    st.error("No se encontró el modelo. Entrénalo primero con train_model.py")

# Mostrar ejemplo de predicción
st.header("Sube una imagen de un dígito (28x28 píxeles, escala de grises)")
uploaded_file = st.file_uploader("Selecciona una imagen", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L")
    image = ImageOps.invert(image)
    image = image.resize((28, 28))
    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    st.image(image, caption="Imagen cargada", width=150)
    prediction = model.predict(img_array)
    st.write(f"Predicción: **{np.argmax(prediction)}**")

# Mostrar métricas del modelo
st.header("Evaluación del modelo")
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0
y_test_cat = tf.keras.utils.to_categorical(y_test)

loss, accuracy = model.evaluate(x_test, y_test_cat, verbose=0)
st.write(f"Pérdida en test: {loss:.4f}")
st.write(f"Precisión en test: {accuracy:.4f}")
