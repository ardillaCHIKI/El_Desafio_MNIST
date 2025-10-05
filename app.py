import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps

# Cargar modelo
model = tf.keras.models.load_model("modelo_final.h5")

st.title("Clasificador de Dígitos MNIST")
st.write("Sube una imagen de un dígito (28x28 píxeles, escala de grises)")

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
