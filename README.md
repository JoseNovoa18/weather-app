# 🌤 Weather App (Aplicación del Clima)

Aplicación web sencilla desarrollada en Python que permite consultar el clima actual de cualquier ciudad ingresada por el usuario. La aplicación consume datos de una API externa y muestra la información en una interfaz web clara y amigable.

---

## 🚀 Características

- Búsqueda de clima por ciudad
- Consumo de API (Open-Meteo)
- Visualización de:
  - 🌡 Temperatura
  - 💨 Velocidad del viento
  - 🧭 Dirección del viento
- Interfaz web simple y responsive
- Estructura de proyecto organizada por módulos

---

## 🛠 Tecnologías utilizadas

- Python
- Flask
- HTML5
- CSS3
- API Open-Meteo

---

## 📁 Estructura del proyecto


weather_app/
└── src/
├── app.py
├── config.py
├── api/
├── services/
├── models/
├── utils/
├── templates/
└── static/


---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/weather-app.git
cd weather-app
2. Crear entorno virtual (opcional pero recomendado)
python -m venv venv

Activar:

Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate
3. Instalar dependencias
pip install -r requirements.txt
4. Ejecutar la aplicación
python -m src.app
5. Abrir en el navegador
http://127.0.0.1:5000/
🧠 Aprendizajes

Este proyecto permitió comprender:

Cómo estructurar un proyecto en Python usando módulos
Cómo consumir APIs externas
Cómo crear aplicaciones web con Flask
Cómo depurar errores relacionados con imports y ejecución
🤖 Uso de IA

Durante el desarrollo se utilizó inteligencia artificial como apoyo para:

Generación de código base
Resolución de errores (imports, ejecución, estructura)
Mejora de la organización del proyecto
Creación de documentación
🔮 Mejoras futuras
Mostrar descripción del clima (soleado, lluvia, etc.)
Añadir pronóstico extendido
Mejorar diseño con Bootstrap
Desplegar la app en internet
👨‍💻 Autor

Proyecto desarrollado como parte de aprendizaje en desarrollo de software.

📄 Licencia

Este proyecto es de uso educativo.