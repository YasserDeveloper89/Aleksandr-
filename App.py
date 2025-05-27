import streamlit as st
from gtts import gTTS
import base64
import os

# Configuración de la página
st.set_page_config(page_title="Aleksandr App", page_icon="🧠", layout="centered")

# Función para generar audio embebido
def narrar(texto, filename="narracion.mp3"):
    tts = gTTS(text=texto, lang='es')
    tts.save(filename)
    with open(filename, "rb") as f:
        audio_bytes = f.read()
        st.audio(audio_bytes, format='audio/mp3')

# Pantalla de bienvenida
def bienvenida():
    st.image("logo_aleksandr.png", width=300)
    st.title("Bienvenido a Aleksandr")
    st.subheader("Una app para mentes brillantes de 6 a 8 años")
    narrar("¡Hola! Soy Aleksandr, y te voy a ayudar a aprender cosas increíbles.")
    st.markdown("---")

# Menú de módulos
def elegir_modulo():
    st.header("¿Qué te gustaría explorar hoy?")
    modulo = st.selectbox(
        "Elige un módulo para empezar:",
        (
            "Mente Brillante",
            "Corazón Fuerte",
            "Cuerpo Activo",
            "Fortaleza Interior",
            "Proyecto Personal"
        )
    )

    if modulo == "Mente Brillante":
        st.subheader("Reto de lógica:")
        st.write("Si tienes 2 manzanas y te dan 3 más, ¿cuántas tienes?")
        narrar("Si tienes dos manzanas y te dan tres más, ¿cuántas tienes en total?")

    elif modulo == "Corazón Fuerte":
        st.subheader("Hoy practicamos la paciencia.")
        st.write("Respira profundamente tres veces. ¿Cómo te sientes?")
        narrar("Respira profundo tres veces. ¿Cómo te sientes ahora? Más tranquilo, ¿verdad?")

    elif modulo == "Cuerpo Activo":
        st.subheader("Mini ejercicio:")
        st.write("Levántate y estírate como un gato. ¡Cuenta hasta 10!")
        narrar("Levántate, estírate como un gato, y cuenta hasta diez conmigo. Uno, dos...")

    elif modulo == "Fortaleza Interior":
        st.subheader("Frase sabia de Aleksandr:")
        frase = "No puedes controlar lo que pasa, pero sí cómo reaccionas."
        st.info(frase)
        narrar(frase)

    elif modulo == "Proyecto Personal":
        st.subheader("Crea tu Mini Misión del Mes")
        idea = st.text_input("¿Qué proyecto te gustaría hacer este mes?")
        if idea:
            st.success(f"¡Gran idea! Aleksandr está emocionado por tu proyecto: {idea}")
            narrar(f"¡Gran idea! Aleksandr está emocionado por tu proyecto: {idea}")

# Ejecutar la app
def main():
    bienvenida()
    elegir_modulo()

if __name__ == "__main__":
    main()
