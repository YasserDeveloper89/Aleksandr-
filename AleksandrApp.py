import streamlit as st
from gtts import gTTS
import tempfile

# Función de narración
def narrar(texto):
    tts = gTTS(text=texto, lang='es')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format="audio/mp3")

# Configuración de la app
st.set_page_config(page_title="Aleksandr App", layout="wide", page_icon="🧠")

# Fondo azul claro y estilo infantil
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #D0E6F6, #A2D4F1);
            font-family: 'Comic Sans MS', cursive;
        }
        h1, h2, h3 {
            color: #0A1F44;
        }
        .stButton>button {
            background-color: #1E90FF;
            color: white;
            border-radius: 12px;
            height: 3em;
            width: 100%;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Logo y bienvenida
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/2048px-User_icon_2.svg.png", width=100)
st.title("Bienvenido a Aleksandr")
st.subheader("Donde los pequeños genios aprenden jugando")
narrar("Hola. Soy Aleksandr. Vamos a aprender jugando.")

# Menú lateral
opcion = st.sidebar.radio("Elige una categoría para comenzar:",
    ["", "Matemáticas", "Lógica", "Ahorro e Inversiones", "Pensar y Razonar", "Frase del día"])

# Módulos de ejercicios
def modulo_matematicas():
    st.header("Matemáticas Divertidas")
    preguntas = [
        ("5 + 3 =", 8),
        ("10 - 4 =", 6),
        ("7 + 6 =", 13),
        ("9 - 2 =", 7),
        ("4 + 9 =", 13),
        ("6 + 2 =", 8),
        ("3 + 3 =", 6)
    ]
    for i, (pregunta, respuesta) in enumerate(preguntas):
        r = st.number_input(pregunta, step=1, format="%d", key=f"mat_{i}")
        if st.button(f"Comprobar {pregunta}", key=f"btnmat_{i}"):
            if r == respuesta:
                st.success("¡Correcto!")
                narrar("¡Correcto!")
            else:
                st.error("Intenta otra vez.")
                narrar("Intenta otra vez.")

def modulo_logica():
    st.header("Desafíos de Lógica")
    ejercicios = [
        ("¿Qué número sigue? 2, 4, 6, 8, ...", 10),
        ("¿Qué número sigue? 5, 10, 15, 20, ...", 25),
        ("¿Qué número sigue? 1, 3, 6, 10, ...", 15)
    ]
    for i, (pregunta, respuesta) in enumerate(ejercicios):
        r = st.number_input(pregunta, step=1, format="%d", key=f"log_{i}")
        if st.button(f"Verificar {pregunta}", key=f"btnlog_{i}"):
            if r == respuesta:
                st.success("¡Muy bien!")
                narrar("¡Muy bien!")
            else:
                st.error("Observa el patrón.")
                narrar("Observa el patrón.")

def modulo_ahorro():
    st.header("Ahorro e Inversiones")
    ejercicios = [
        ("Si tienes 10 monedas y ahorras 2 por día, ¿cuánto tendrás en 5 días?", 20),
        ("Si guardas 3 monedas al día durante 4 días, ¿cuántas tienes?", 12)
    ]
    for i, (pregunta, respuesta) in enumerate(ejercicios):
        r = st.number_input(pregunta, step=1, format="%d", key=f"ah_{i}")
        if st.button(f"Comprobar {pregunta}", key=f"btnah_{i}"):
            if r == respuesta:
                st.success("¡Perfecto!")
                narrar("¡Perfecto!")
            else:
                st.error("No es correcto.")
                narrar("No es correcto.")

def modulo_razonar():
    st.header("Piensa y Razona")
    preguntas = [
        ("¿Qué harías si un amigo está triste?", 
         ["Lo ignoro", "Le doy un abrazo", "Le digo que se vaya"], 
         "Le doy un abrazo"),
        ("Si ves basura en el suelo, ¿qué haces?",
         ["La recojo", "La pateo", "No es mi problema"],
         "La recojo")
    ]
    for i, (texto, opciones, correcta) in enumerate(preguntas):
        r = st.radio(texto, opciones, key=f"raz_{i}")
        if st.button(f"Responder {texto}", key=f"btnraz_{i}"):
            if r == correcta:
                st.success("¡Muy bien pensado!")
                narrar("¡Muy bien pensado!")
            else:
                st.error("Piénsalo otra vez.")
                narrar("Piénsalo otra vez.")

def modulo_extras():
    st.header("Frase del día")
    frase = "No importa lo pequeño que seas, puedes hacer cosas grandes."
    st.info(frase)
    narrar(frase)

# Ejecutar el módulo elegido
if opcion == "Matemáticas":
    modulo_matematicas()
elif opcion == "Lógica":
    modulo_logica()
elif opcion == "Ahorro e Inversiones":
    modulo_ahorro()
elif opcion == "Pensar y Razonar":
    modulo_razonar()
elif opcion == "Frase del día":
    modulo_extras()
