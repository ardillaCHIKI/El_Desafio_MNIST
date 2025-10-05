import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
from reconocimiento import predecir_imagen

st.set_page_config(page_title="El Desafío MNIST", layout="centered")
st.title("🖌️ Dibuja un número y la IA lo adivina")

canvas_result = st_canvas(
    fill_color="white",
    stroke_width=10,
    stroke_color="black",
    background_color="white",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas_result.image_data is not None:
    imagen = Image.fromarray((canvas_result.image_data[:, :, 0]).astype("uint8"))
    imagen = imagen.resize((28, 28)).convert("L")
    imagen = np.array(imagen) / 255.0
    imagen = imagen.reshape(1, 28, 28, 1)

    st.image(imagen, caption="Tu dibujo (convertido a 28x28)", width=150)
    prediccion = predecir_imagen(Image.fromarray((canvas_result.image_data[:, :, 0]).astype("uint8")))
    st.subheader(f"🔢 Predicción: {prediccion}")


