import streamlit as st
from gtts import gTTS
import tempfile

def narrar(texto):
    tts = gTTS(text=texto, lang='es')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format="audio/mp3")

st.set_page_config(page_title="Aleksandr App", layout="wide", page_icon="🌟")

# Estilo visual infantil
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #FFF5E1, #FFD1DC);
            font-family: 'Comic Sans MS', cursive;
        }
        h1, h2, h3 {
            color: #333;
        }
        .stButton>button {
            background-color: #FFD700;
            color: black;
            border-radius: 12px;
            height: 3em;
            width: 100%;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

def bienvenida():
    st.title("Bienvenido a Aleksandr")
    st.subheader("Donde los pequeños genios aprenden jugando")
    narrar("Hola. Soy Aleksandr. Vamos a aprender jugando.")

def modulo_matematicas():
    st.header("Matemáticas Divertidas")
    preguntas = [
        ("5 + 3 =", 8),
        ("10 - 4 =", 6),
        ("7 + 6 =", 13),
        ("9 - 2 =", 7),
        ("4 + 9 =", 13)
    ]
    for i, (pregunta, respuesta) in enumerate(preguntas):
        r = st.number_input(pregunta, key=f"mat{i}")
        if st.button(f"Comprobar {pregunta}", key=f"btnmat{i}"):
            if r == respuesta:
                st.success("¡Correcto!")
                narrar("¡Correcto!")
            else:
                st.error("Intenta otra vez.")
                narrar("Intenta otra vez.")

def modulo_logica():
    st.header("Desafíos de Lógica")
    secuencias = [
        ("2, 4, 6, 8, ...", 10),
        ("5, 10, 15, 20, ...", 25)
    ]
    for i, (pregunta, respuesta) in enumerate(secuencias):
        r = st.number_input(f"¿Qué número sigue? {pregunta}", key=f"seq{i}")
        if st.button(f"Verificar {pregunta}", key=f"btnseq{i}"):
            if r == respuesta:
                st.success("¡Muy bien!")
                narrar("¡Muy bien!")
            else:
                st.error("Observa el patrón.")
                narrar("Observa el patrón.")

def modulo_ahorro():
    st.header("Ahorro e Inversiones")
    st.write("Tienes 10 monedas. Ahorras 2 por día. ¿Cuánto después de 5 días?")
    r = st.number_input("Respuesta:", key="ahorro")
    if st.button("Comprobar ahorro"):
        if r == 20:
            st.success("¡Perfecto!")
            narrar("¡Perfecto!")
        else:
            st.error("No es correcto.")
            narrar("No es correcto.")

def modulo_razonar():
    st.header("Piensa y Razona")
    r = st.radio("¿Qué harías si un amigo está triste?", 
                 ["Lo ignoro", "Le doy un abrazo", "Le digo que se vaya"], key="empatia")
    if st.button("Responder empatía"):
        if r == "Le doy un abrazo":
            st.success("¡Esa es la actitud!")
            narrar("¡Esa es la actitud!")
        else:
            st.error("¿Crees que eso ayudaría?")
            narrar("¿Crees que eso ayudaría?")

def modulo_extras():
    st.header("Frase del día")
    frase = "No importa lo pequeño que seas, puedes hacer cosas grandes."
    st.info(frase)
    narrar(frase)

def main():
    bienvenida()
    opcion = st.sidebar.radio("¿Qué quieres aprender hoy?",
        ["Matemáticas", "Lógica", "Ahorro e Inversiones", "Pensar y Razonar", "Extras"])
    
    if opcion == "Matemáticas":
        modulo_matematicas()
    elif opcion == "Lógica":
        modulo_logica()
    elif opcion == "Ahorro e Inversiones":
        modulo_ahorro()
    elif opcion == "Pensar y Razonar":
        modulo_razonar()
    elif opcion == "Extras":
        modulo_extras()

if __name__ == "__main__":
    main()
