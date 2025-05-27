import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Aleksandr - Aprende Jugando", layout="centered")

# Colores y estilo visual
dark_blue = "#1A5276"
light_blue = "#E8F6F3"

st.markdown(f"""
    <style>
    .main-container {{
        background-color: {light_blue};
        padding: 2rem;
        border-radius: 15px;
    }}
    .menu-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-top: 2rem;
    }}
    .menu-item button {{
        width: 100%;
        padding: 1rem;
        border: none;
        background-color: {dark_blue};
        color: white;
        border-radius: 12px;
        font-size: 18px;
        font-weight: bold;
    }}
    </style>
""", unsafe_allow_html=True)

# Logo
logo = Image.open("logo_aleksandr.png")
st.image(logo, use_container_width=True)

st.title("Bienvenido a Aleksandr")
st.subheader("Elige una categoría para aprender y divertirte")

# Menú moderno
categoria = None
col1, col2 = st.columns(2)

with col1:
    if st.button("Matemáticas"):
        categoria = "matematicas"
    if st.button("Ahorro e Inversiones"):
        categoria = "ahorro"

with col2:
    if st.button("Lógica"):
        categoria = "logica"
    if st.button("Razonamiento"):
        categoria = "razonamiento"

# Preguntas por categoría
preguntas_matematicas = [
    ("5 + 3", 8), ("10 - 4", 6), ("6 + 7", 13),
    ("9 - 2", 7), ("3 + 8", 11), ("7 + 6", 13),
    ("10 - 5", 5), ("4 + 4", 8), ("12 - 3", 9),
    ("15 + 6", 21), ("18 - 7", 11), ("9 + 9", 18),
    ("20 - 10", 10), ("3 + 5", 8), ("14 - 9", 5)
]

preguntas_logica = [
    ("¿Qué objeto no encaja? Perro, Gato, Mesa, Conejo", "mesa"),
    ("¿Cuál es el patrón? 2, 4, 6, ...", "8"),
    ("Completa: Sol, Luna, Estrella, ...", "cielo"),
    ("¿Qué sigue? Lunes, Martes, Miércoles, ...", "jueves"),
    ("¿Cuál no pertenece? Carro, Bicicleta, Avión, Camisa", "camisa")
]

# Mostrar preguntas según categoría
if categoria == "matematicas":
    st.subheader("Ejercicios de Matemáticas")
    pregunta, resultado = random.choice(preguntas_matematicas)
    respuesta = st.text_input(f"{pregunta} = ?", key="math")

    if st.button("Comprobar respuesta"):
        try:
            if int(respuesta.strip()) == resultado:
                st.success("¡Correcto!")
            else:
                st.error("Respuesta incorrecta. Intenta otra vez.")
        except:
            st.error("Escribe un número válido.")

elif categoria == "logica":
    st.subheader("Ejercicios de Lógica")
    pregunta, correcta = random.choice(preguntas_logica)
    respuesta = st.text_input(pregunta, key="logica")
    if st.button("Comprobar lógica"):
        if respuesta.strip().lower() == correcta.lower():
            st.success("¡Bien pensado!")
        else:
            st.error("Intenta con otra lógica.")

elif categoria == "ahorro":
    st.subheader("Ahorro e Inversiones")
    st.write("Tienes 10 monedas. Compras un cuaderno que cuesta 4 monedas.")
    respuesta = st.text_input("¿Cuánto dinero te queda?", key="ahorro")
    if st.button("Verificar ahorro"):
        if respuesta.strip() == "6":
            st.success("¡Correcto!")
        else:
            st.error("Incorrecto. Revisa tus cuentas.")

elif categoria == "razonamiento":
    st.subheader("Razonamiento")
    opciones = ["Guardarla", "Buscar al dueño", "Ignorarla", "Tirarla"]
    seleccion = st.radio("¿Qué harías si encuentras una cartera en el suelo?", opciones)
    if st.button("Verificar razonamiento"):
        if seleccion == "Buscar al dueño":
            st.success("¡Muy buen razonamiento!")
        else:
            st.error("Piensa en lo correcto.")
