import streamlit as st
from gtts import gTTS
import os
import random

# Función para generar la voz
def narrar(texto):
    tts = gTTS(text=texto, lang='es')
    tts.save("narracion.mp3")
    os.system("start narracion.mp3")  # Para Windows. Usa 'afplay' en Mac o 'mpg321' en Linux

# Función de bienvenida
def bienvenida():
    st.image("logo_aleksandr.png", width=300)  # El logo de Aleksandr
    narrar("¡Hola! Soy Aleksandr, y te voy a ayudar a aprender cosas increíbles.")
    st.title("Bienvenidos a la Aventura de Aleksandr")
    st.write("¿Estás listo para comenzar? Vamos a aprender juntos.")

# Función de módulos interactivos
def elegir_modulo():
    st.write("¿Qué te gustaría aprender hoy?")
    modulo = st.selectbox(
        "Elige un módulo:",
        ("Mente Brillante", "Corazón Fuerte", "Cuerpo Activo", "Fortaleza Interior", "Proyecto Personal")
    )
    if modulo == "Mente Brillante":
        st.write("Vamos a resolver un reto de lógica...")
        narrar("Vamos a resolver un reto de lógica. ¿Estás listo?")
    elif modulo == "Corazón Fuerte":
        st.write("Hoy vamos a aprender sobre la paciencia...")
        narrar("Hoy vamos a aprender sobre la paciencia.")
    elif modulo == "Cuerpo Activo":
        st.write("Hagamos una pequeña actividad física...")
        narrar("Hagamos una pequeña actividad física para activar el cuerpo.")
    elif modulo == "Fortaleza Interior":
        st.write("Hoy vamos a reflexionar sobre la templanza...")
        narrar("Hoy vamos a reflexionar sobre la templanza.")
    elif modulo == "Proyecto Personal":
        st.write("Es hora de planificar tu proyecto personal...")
        narrar("Es hora de planificar tu proyecto personal.")

# Configuración de Streamlit
def main():
    bienvenida()
    elegir_modulo()

if __name__ == "__main__":
    main()
