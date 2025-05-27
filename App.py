import streamlit as st import pyttsx3

Configurar pyttsx3

engine = pyttsx3.init() voices = engine.getProperty('voices') engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id) engine.setProperty('rate', 165) engine.setProperty('volume', 1.0)

def narrar(texto): engine.say(texto) engine.runAndWait()

st.set_page_config(page_title="Aleksandr App", layout="wide", page_icon="🌟")

Estilo CSS personalizado

st.markdown(""" <style> body { background-color: #FFF5E1; } .stApp { background: linear-gradient(to right, #FFF5E1, #FFD1DC); } h1, h2, h3, h4 { color: #333; } .stButton>button { background-color: #FFD700; color: black; border-radius: 12px; height: 3em; width: 100%; font-weight: bold; } .stRadio > div { background-color: #fff; padding: 10px; border-radius: 10px; } </style> """, unsafe_allow_html=True)

def bienvenida(): st.image("logo_aleksandr.png", width=200) st.title("Bienvenido a Aleksandr") st.subheader("Donde los pequeños genios aprenden jugando") narrar("Hola. Soy Aleksandr. Vamos a aprender jugando.")

-------------- Ejercicios por categoría ---------------

def modulo_matematicas(): st.header("Matemáticas Divertidas")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Suma")
    narrar("Vamos a sumar")
    r1 = st.number_input("5 + 3 =", min_value=0, step=1, key="suma1")
    if st.button("Comprobar suma"):
        if r1 == 8:
            st.success("¡Correcto!")
            narrar("¡Correcto!")
        else:
            st.error("Ups, inténtalo de nuevo")
            narrar("Ups, inténtalo de nuevo")

with col2:
    st.subheader("Restas")
    r2 = st.number_input("10 - 4 =", min_value=0, step=1, key="resta1")
    if st.button("Comprobar resta"):
        if r2 == 6:
            st.success("¡Bien hecho!")
            narrar("¡Bien hecho!")
        else:
            st.error("No es correcto")
            narrar("No es correcto")

st.markdown("---")
st.subheader("Comparaciones")
r3 = st.radio("¿Qué número es mayor?", [3, 7, 5], key="comp1")
if st.button("Responder comparaciones"):
    if r3 == 7:
        st.success("¡Exacto!")
        narrar("¡Exacto!")
    else:
        st.error("Intenta otra vez")
        narrar("Intenta otra vez")

def modulo_logica(): st.header("Desafíos de Lógica")

st.subheader("Secuencia")
r = st.number_input("¿Qué número sigue? 2, 4, 6, 8, ...", min_value=0, step=1, key="sec")
if st.button("Comprobar secuencia"):
    if r == 10:
        st.success("¡Muy bien!")
        narrar("¡Muy bien!")
    else:
        st.error("Observa el patrón")
        narrar("Observa el patrón")

st.markdown("---")
st.subheader("¿Qué falta?")
r2 = st.radio("Sol, luna, estrella, ¿?", ["Nube", "Planeta", "Cometa"], key="faltante")
if st.button("Comprobar faltante"):
    if r2 == "Cometa":
        st.success("¡Lo lograste!")
        narrar("¡Lo lograste!")
    else:
        st.error("Ups, intenta otra opción")
        narrar("Ups, intenta otra opción")

def modulo_ahorro(): st.header("Ahorro e Inversiones") st.write("Tienes 10 monedas. Ahorras 2 por día. ¿Cuánto después de 5 días?") r = st.number_input("Respuesta ahorro:", min_value=0, step=1, key="ahorro") if st.button("Comprobar ahorro"): if r == 20: st.success("¡Perfecto!") narrar("¡Perfecto!") else: st.error("No es correcto") narrar("No es correcto")

st.markdown("---")
st.subheader("Diferenciar deseos y necesidades")
r2 = st.radio("¿Cuál es una necesidad?", ["Dulces", "Juguetes", "Comida"], key="necesidades")
if st.button("Ver respuesta necesidades"):
    if r2 == "Comida":
        st.success("¡Muy bien!")
        narrar("¡Muy bien!")
    else:
        st.error("Intenta de nuevo")
        narrar("Intenta de nuevo")

def modulo_razonar(): st.header("Piensa y Razona")

st.write("¿Qué harías si un amigo está triste?")
opciones = ["Lo ignoro", "Le doy un abrazo", "Le digo que se vaya"]
r = st.radio("Elige una opción:", opciones, key="emociones")
if st.button("Comprobar empatía"):
    if r == "Le doy un abrazo":
        st.success("¡Esa es la actitud!")
        narrar("¡Esa es la actitud!")
    else:
        st.error("¿Crees que eso ayudaría?")
        narrar("¿Crees que eso ayudaría?")

def modulo_extras(): st.header("Frase del día") frase = "No importa lo pequeño que seas, puedes hacer cosas grandes." st.info(frase) narrar(frase)

---------------------- Navegación ----------------------

def elegir_modulo(): modulo = st.sidebar.selectbox("Elige un módulo:", ["Matemáticas", "Lógica", "Ahorro e Inversiones", "Pensar y Razonar", "Extras"])

if modulo == "Matemáticas":
    modulo_matematicas()
elif modulo == "Lógica":
    modulo_logica()
elif modulo == "Ahorro e Inversiones":
    modulo_ahorro()
elif modulo == "Pensar y Razonar":
    modulo_razonar()
elif modulo == "Extras":
    modulo_extras()

def main(): bienvenida() elegir_modulo()

if name == "main": main()

