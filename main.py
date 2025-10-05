import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
from reconocimiento import predecir_imagen

st.set_page_config(page_title="El Desafío MNIST", layout="centered")
st.title("🖌️ Dibuja un número y la IA lo adivina")

canvas_result = st_canvas(
    fill_color="white",
    stroke_width=2,
    stroke_color="black",
    background_color="white",
    height=200,
    width=200,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas_result.image_data is not None:
    # Convertir a imagen PIL
    imagen_pil = Image.fromarray(canvas_result.image_data[:, :, 0].astype("uint8"))
    imagen_pil = imagen_pil.resize((28, 28)).convert("L")

    # Mostrar imagen procesada
    st.image(imagen_pil, caption="Tu dibujo (convertido a 28x28)", width=150)

    # Convertir a array para predicción
    imagen_array = np.array(imagen_pil).reshape(1, 28, 28, 1).astype("float32") / 255.0

    # Predecir
    from reconocimiento import predecir_imagen
    prediccion = predecir_imagen(imagen_pil)

    st.subheader(f"🧠 Predicción: {prediccion}")
