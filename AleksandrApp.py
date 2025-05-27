import streamlit as st
import random
from PIL import Image

# Configuración general
st.set_page_config(page_title="Aleksandr - Aprende Jugando", layout="centered")
st.markdown("<style>body {background-color: #D6EAF8;}</style>", unsafe_allow_html=True)

# Mostrar logo
logo = Image.open("logo_aleksandr.png")
st.image(logo, width=150)

st.title("Bienvenido a Aleksandr")
st.write("Elige una categoría para comenzar a aprender de forma divertida:")

categorias = ["Selecciona una categoría", "Matemáticas", "Lógica", "Ahorro e Inversiones", "Pensamiento y Razonamiento"]
seleccion = st.selectbox("Categoría:", categorias)

# Inicializar estado para matemáticas
if 'math_score' not in st.session_state:
    st.session_state.math_score = 0
if 'math_question' not in st.session_state:
    st.session_state.math_question = {}

def generar_nueva_pregunta():
    operador = random.choice(["+", "-"])
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    if operador == "-" and a < b:
        a, b = b, a
    return {"a": a, "b": b, "op": operador}

def matematicas():
    st.subheader("Ejercicios de Matemáticas")
    if not st.session_state.math_question:
        st.session_state.math_question = generar_nueva_pregunta()

    q = st.session_state.math_question
    if q["op"] == "+":
        correcto = q["a"] + q["b"]
        pregunta = f"{q['a']} + {q['b']} = ?"
    else:
        correcto = q["a"] - q["b"]
        pregunta = f"{q['a']} - {q['b']} = ?"

    respuesta = st.number_input(pregunta, step=1, format="%d", key="respuesta")

    if st.button("Comprobar respuesta"):
        if int(respuesta) == correcto:
            st.success("¡Correcto!")
            st.session_state.math_score += 1
            st.session_state.math_question = generar_nueva_pregunta()
        else:
            st.error("¡Ups! Inténtalo otra vez.")

    st.info(f"Ejercicios correctos: {st.session_state.math_score}")

# Mostrar la categoría seleccionada
if seleccion == "Matemáticas":
    matematicas()
elif seleccion == "Lógica":
    st.write("Aquí irán ejercicios de lógica.")
elif seleccion == "Ahorro e Inversiones":
    st.write("Aquí irán ejercicios de ahorro.")
elif seleccion == "Pensamiento y Razonamiento":
    st.write("Aquí irán ejercicios de pensamiento.")
