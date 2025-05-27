import streamlit as st
import random
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Aleksandr - Aprende Jugando", layout="centered")

# Cargar y mostrar el logo
logo = Image.open("logo_aleksandr.png")
st.image(logo, use_container_width=False, width=180)

# Estilo visual masculino e infantil
st.markdown("""
    <style>
        body, .main {
            background-color: #AED6F1;
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
        respuesta = st.number_input(f"¿Cuánto es {a} + {b}?", step=1, format="%d", key="suma")
    else:
        if a < b:
            a, b = b, a
        correcto = a - b
        respuesta = st.number_input(f"¿Cuánto es {a} - {b}?", step=1, format="%d", key="resta")

    if st.button("Comprobar resultado"):
        if int(respuesta) == correcto:
            st.success("¡Muy bien!")
        else:
            st.error(f"Intenta otra vez. La respuesta correcta era {correcto}")

def logica():
    st.subheader("Lógica")
    st.write("¿Qué número viene después en la secuencia?")
    st.write("2, 4, 6, 8, ?")
    respuesta = st.number_input("Tu respuesta:", step=1, format="%d", key="logica")
    if st.button("Verificar lógica"):
        if int(respuesta) == 10:
            st.success("¡Correcto!")
        else:
            st.error("Casi, piensa en los números pares.")

def ahorro():
    st.subheader("Ahorro e Inversiones")
    st.write("Tienes 10 monedas y compras un juguete que cuesta 7.")
    respuesta = st.number_input("¿Cuánto te queda?", step=1, format="%d", key="ahorro")
    if st.button("Comprobar ahorro"):
        if int(respuesta) == 3:
            st.success("¡Eso es! Sabes ahorrar.")
        else:
            st.error("Revisa la resta: 10 - 7.")

def pensamiento():
    st.subheader("Pensamiento y Razonamiento")
    pregunta = "Si el sol sale por el este, ¿por dónde se pone?"
    respuesta = st.text_input(pregunta)
    if st.button("Verificar respuesta"):
        if respuesta.strip().lower() == "oeste":
            st.success("¡Muy bien pensado!")
        else:
            st.error("Pista: es el lado contrario al este.")

# Mostrar la sección según selección
if seleccion == "Matemáticas":
    matematicas()
elif seleccion == "Lógica":
    logica()
elif seleccion == "Ahorro e Inversiones":
    ahorro()
elif seleccion == "Pensamiento y Razonamiento":
    pensamiento()
