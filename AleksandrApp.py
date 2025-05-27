import streamlit as st
import random
from PIL import Image

# Configurar la página
st.set_page_config(page_title="Aleksandr - Aprende Jugando", layout="centered")

# Cargar y mostrar el logo
logo = Image.open("logo_aleksandr.png")
st.image(logo, use_column_width=False, width=180)

# Fondo y estilo
st.markdown("""
    <style>
        body {
            background-color: #D6EAF8;
        }
        .main {
            background-color: #D6EAF8;
        }
        .stButton>button {
            background-color: #3498DB;
            color: white;
            font-size: 20px;
            border-radius: 10px;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<h1 style='text-align: center; color: #2C3E50;'>Bienvenido a Aleksandr</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Donde los pequeños genios aprenden jugando</h4>", unsafe_allow_html=True)

# Menú de categorías
opciones = ["Selecciona una categoría", "Matemáticas", "Lógica", "Ahorro e Inversiones", "Pensamiento y Razonamiento"]
seleccion = st.selectbox("¿Qué quieres estudiar hoy?", opciones)

# Funciones por categoría
def matematicas():
    st.subheader("Matemáticas")
    a, b = random.randint(1, 10), random.randint(1, 10)
    operador = st.radio("Elige una operación", ["Suma", "Resta"])
    if operador == "Suma":
        correcto = a + b
        respuesta = st.number_input(f"¿Cuánto es {a} + {b}?", step=1)
    else:
        correcto = a - b
        respuesta = st.number_input(f"¿Cuánto es {a} - {b}?", step=1)
    if st.button("Comprobar"):
        if respuesta == correcto:
            st.success("¡Muy bien!")
        else:
            st.error(f"Intenta otra vez. La respuesta correcta era {correcto}")

def logica():
    st.subheader("Lógica")
    st.write("¿Qué viene después?")
    secuencia = [2, 4, 6, 8]
    respuesta = st.number_input(f"2, 4, 6, 8, ?", step=1)
    if st.button("Verificar lógica"):
        if respuesta == 10:
            st.success("¡Correcto!")
        else:
            st.error("Casi, piensa en los pares.")

def ahorro():
    st.subheader("Ahorro e Inversiones")
    st.write("Tienes 10 monedas y quieres comprar un juguete que vale 7.")
    respuesta = st.number_input("¿Cuánto te sobra después de comprarlo?", step=1)
    if st.button("Comprobar ahorro"):
        if respuesta == 3:
            st.success("¡Eso es! Sabes administrar el dinero.")
        else:
            st.error("Revisa bien la resta.")

def pensamiento():
    st.subheader("Pensamiento y Razonamiento")
    pregunta = "Si el sol sale por el este, ¿por dónde se pone?"
    respuesta = st.text_input(pregunta)
    if st.button("Verificar respuesta"):
        if respuesta.strip().lower() == "oeste":
            st.success("¡Muy bien pensado!")
        else:
            st.error("Pista: piensa en el lado contrario.")

# Mostrar la categoría seleccionada
if seleccion == "Matemáticas":
    matematicas()
elif seleccion == "Lógica":
    logica()
elif seleccion == "Ahorro e Inversiones":
    ahorro()
elif seleccion == "Pensamiento y Razonamiento":
    pensamiento()
