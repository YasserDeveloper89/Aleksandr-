import streamlit as st
import random
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

# Configuración
st.set_page_config(page_title="Aleksandr - Aprende Jugando", layout="centered")

# Colores y estilo
dark_blue = "#1A5276"
light_blue = "#D6EAF8"

st.markdown(f"""
    <style>
    body {{background-color: {light_blue};}}
    .logo-container {{display: flex; justify-content: center; margin-bottom: 20px;}}
    .main-title {{text-align: center; font-size: 36px; color: {dark_blue};}}
    .menu-grid {{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
        margin-top: 2rem;
    }}
    .menu-item {{
        background: white;
        border-radius: 15px;
        padding: 1rem;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        font-size: 20px;
        color: {dark_blue};
    }}
    </style>
""", unsafe_allow_html=True)

# Logo
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
logo = Image.open("logo_aleksandr.png")
st.image(logo, width=250, use_column_width=False)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<h1 class="main-title">Bienvenido a Aleksandr</h1>', unsafe_allow_html=True)
st.markdown("""
Elige una categoría para comenzar a estudiar de forma divertida e interactiva.
""")

# Selección de sección
seccion = st.selectbox("Selecciona una categoría:", [
    "---", "Matemáticas", "Lógica", "Ahorro e Inversiones", "Razonamiento"
])

# Preguntas por categoría
preguntas_matematicas = [
    ("5 + 3 = ?", "8"), ("10 - 4 = ?", "6"), ("6 + 7 = ?", "13"),
    ("9 - 2 = ?", "7"), ("3 + 8 = ?", "11"), ("7 + 6 = ?", "13"),
    ("10 - 5 = ?", "5"), ("4 + 4 = ?", "8"), ("12 - 3 = ?", "9"),
    ("15 + 6 = ?", "21"), ("18 - 7 = ?", "11"), ("9 + 9 = ?", "18"),
    ("20 - 10 = ?", "10"), ("3 + 5 = ?", "8"), ("14 - 9 = ?", "5")
]

preguntas_logica = [
    ("¿Qué objeto no encaja? Perro, Gato, Mesa, Conejo", "Mesa"),
    ("¿Cuál es el patrón? 2, 4, 6, ...", "8"),
    ("Completa: Sol, Luna, Estrella, ...", "Cielo"),
    ("¿Cuál es el siguiente? Lunes, Martes, Miércoles, ...", "Jueves"),
    ("¿Cuál no pertenece? Carro, Bicicleta, Avión, Camisa", "Camisa")
]

# Categorías
if seccion == "Matemáticas":
    st.subheader("Ejercicios de Matemáticas")
    q = random.choice(preguntas_matematicas)
    respuesta = st.text_input(q[0], key="mat")
    if st.button("Comprobar", key="btn_mat"):
        if respuesta.strip() == q[1]:
            st.success("¡Correcto!")
        else:
            st.error("Incorrecto. Inténtalo otra vez.")

elif seccion == "Lógica":
    st.subheader("Ejercicios de Lógica")
    q = random.choice(preguntas_logica)
    respuesta = st.text_input(q[0], key="log")
    if st.button("Verificar", key="btn_log"):
        if respuesta.strip().lower() == q[1].lower():
            st.success("Muy bien")
        else:
            st.error("Incorrecto")

elif seccion == "Ahorro e Inversiones":
    st.subheader("Ahorro e Inversiones")
    st.write("Tienes 10 monedas. Compras un cuaderno que cuesta 4 monedas.")
    respuesta = st.text_input("¿Cuánto dinero te queda?", key="ahorro")
    if st.button("Comprobar ahorro"):
        if respuesta.strip() == "6":
            st.success("¡Muy bien! Ahorraste bien.")
        else:
            st.error("Incorrecto. Inténtalo de nuevo.")

elif seccion == "Razonamiento":
    st.subheader("Razonamiento")
    st.write("¿Qué harías si encuentras una cartera en el suelo?")
    opciones = ["Guardarla", "Buscar al dueño", "Ignorarla", "Tirarla"]
    seleccion = st.radio("Elige la mejor opción:", opciones, key="raz")
    if st.button("Verificar razonamiento"):
        if seleccion == "Buscar al dueño":
            st.success("¡Muy bien pensado!")
        else:
            st.error("Podemos pensar una mejor opción.")
