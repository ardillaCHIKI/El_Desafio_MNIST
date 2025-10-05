# El_Desafio_MNIST
https://github.com/ardillaCHIKI/El_Desafio_MNIST.git
🧠 El Desafío MNIST
Este repositorio contiene un proyecto de clasificación de dígitos manuscritos utilizando el conjunto de datos MNIST. El objetivo es entrenar y evaluar modelos de aprendizaje automático para reconocer números del 0 al 9 a partir de imágenes en escala de grises de 28x28 píxeles.

📁 Estructura del Proyecto
El_Desafio_MNIST/
├── src/                      # Código fuente principal
├── static/                  # Recursos estáticos (si aplica)
├── venv/                    # Entorno virtual de Python
├── Ejercicio1_classify_numbers.ipynb  # Notebook con análisis y entrenamiento
├── main.py                  # Script principal de ejecución
├── mnist_trainer.py         # Módulo de entrenamiento del modelo
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Este archivo

🚀 Cómo empezar
Clona el repositorio:
git clone https://github.com/ardillaCHIKI/El_Desafio_MNIST.git
cd El_Desafio_MNIST

Crea y activa el entorno virtual:
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\\Scripts\\activate   # En Windows

Instala las dependencias:

bash
pip install -r requirements.txt
Ejecuta el proyecto: Puedes correr el notebook Ejercicio1_classify_numbers.ipynb para explorar el flujo de trabajo o ejecutar main.py para lanzar el modelo desde consola.

🚀 Cómo ejecutar el proyecto desde main.py
Una vez que hayas instalado las dependencias y activado el entorno virtual, puedes lanzar el modelo directamente desde el script principal:
bash
python main.py

🧪 Funcionalidades
Carga y preprocesamiento del dataset MNIST.

Entrenamiento de modelos de clasificación.

Evaluación de precisión y visualización de resultados.

Modularización del código para facilitar su mantenimiento.

📊 Tecnologías utilizadas
Python 3

TensorFlow / Keras

NumPy, Matplotlib

Jupyter Notebook
