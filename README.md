# El_Desafio_MNIST
https://github.com/ardillaCHIKI/El_Desafio_MNIST.git
🧠 El Desafío MNIST
Proyecto de clasificación de dígitos manuscritos usando el famoso dataset MNIST. El objetivo es entrenar un modelo que pueda reconocer números del 0 al 9 a partir de imágenes en escala de grises de 28x28 píxeles.

📦 Estructura del repositorio
Código
El_Desafio_MNIST/
├── Ejercicio1_classify_numbers.ipynb  # Notebook con entrenamiento y evaluación
├── main.py                            # Script principal para ejecutar el modelo
├── mnist_trainer.py                   # Módulo con funciones de entrenamiento
├── requirements.txt                   # Lista de dependencias
└── venv/                              # Entorno virtual (opcional)
⚙️ Instalación y ejecución
1. Clonar el repositorio
bash
git clone https://github.com/ardillaCHIKI/El_Desafio_MNIST.git
cd El_Desafio_MNIST
2. Crear y activar el entorno virtual (Windows)
bash
python -m venv venv
venv\Scripts\activate
💡 En Mac/Linux: source venv/bin/activate

3. Instalar dependencias
bash
pip install -r requirements.txt
4. Ejecutar el proyecto desde main.py
bash
python main.py
Este script se encarga de:

Cargar el dataset MNIST.

Preprocesar las imágenes.

Entrenar el modelo.

Evaluar su rendimiento.

Mostrar ejemplos de predicciones.

🧪 ¿Qué tecnologías se usan?
Python 🐍

TensorFlow / Keras

NumPy

Matplotlib

Jupyter Notebook
