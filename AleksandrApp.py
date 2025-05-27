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
try:
    logo = Image.open("logo_aleksandr.png")
    st.image(logo, use_container_width=True)
except:
    st.markdown("**[Logo no encontrado]**")

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
    ("5 + 3", 8), ("10 - 4", 6), ("6 + 7", 13), ("9 - 2", 7),
    ("3 + 8", 11), ("7 + 6", 13), ("10 - 5", 5), ("4 + 4", 8),
    ("12 - 3", 9), ("15 + 6", 21)
]

preguntas_logica = [
    ("¿Qué objeto no encaja? Perro, Gato, Mesa, Conejo", "mesa"),
    ("¿Cuál es el patrón? 2, 4, 6, ...", "8"),
    ("Completa: Sol, Luna, Estrella, ...", "cielo"),
    ("¿Qué sigue? Lunes, Martes, Miércoles, ...", "jueves"),
    ("¿Cuál no pertenece? Carro, Bicicleta, Avión, Camisa", "camisa"),
    ("¿Qué falta? A, B, C, ...", "D"),
    ("Uno, Dos, Tres, ...", "cuatro"),
    ("Manzana, Plátano, Fresa, Televisor", "televisor"),
    ("Suma: 1+2+3", "6"),
    ("Mitad de 10", "5")
]

preguntas_ahorro = [
    ("Tienes 10 monedas. Compras un cuaderno por 4. ¿Cuánto te queda?", "6"),
    ("Ahorras 3 cada día por 5 días. ¿Cuánto tienes?", "15"),
    ("Tenías 20, gastas 5. ¿Saldo?", "15"),
    ("Ahorro de 2 por 7 días. ¿Total?", "14"),
    ("Gastas 3 de 9. ¿Restante?", "6"),
    ("Compras 2 cosas de 4. Tienes 10. ¿Te queda?", "2"),
    ("Tienes 8, ganas 4. ¿Total?", "12"),
    ("Tenías 6, te dan 5. ¿Ahora?", "11"),
    ("Ahorras 10, gastas 2. ¿Saldo?", "8"),
    ("Tienes 12 y regalas 3. ¿Cuánto conservas?", "9")
]

preguntas_razonamiento = [
    ("¿Qué harías si encuentras una cartera en el suelo?", "Buscar al dueño"),
    ("Alguien necesita ayuda. ¿Qué haces?", "Ayudar"),
    ("¿Qué es más correcto? Compartir o pelear", "Compartir"),
    ("¿Cómo cuidarías el planeta?", "No tirar basura"),
    ("¿Qué es más importante? Jugar o estudiar", "Estudiar"),
    ("¿Qué harías si ves bullying?", "Pedir ayuda"),
    ("Si un amigo está triste, tú...", "Lo animas"),
    ("Si rompes algo, tú...", "Lo arreglas"),
    ("¿Es correcto mentir?", "No"),
    ("¿Debes respetar a los demás?", "Sí")
]

# Mostrar preguntas según categoría
if categoria == "matematicas":
    st.subheader("Ejercicios de Matemáticas")
    if "pregunta" not in st.session_state:
        st.session_state.pregunta, st.session_state.resultado = random.choice(preguntas_matematicas)
        st.session_state.comprobado = False

    st.markdown(f"### {st.session_state.pregunta} = ?")
    respuesta = st.text_input("Tu respuesta:", key="respuesta_mate")

    if st.button("Comprobar respuesta"):
        try:
            if int(respuesta.strip()) == st.session_state.resultado:
                st.success("¡Correcto!")
            else:
                st.error("Respuesta incorrecta. Intenta otra vez.")
            st.session_state.comprobado = True
        except:
            st.error("Escribe un número válido.")

    if st.session_state.comprobado:
        if st.button("Siguiente pregunta"):
            st.session_state.pregunta, st.session_state.resultado = random.choice(preguntas_matematicas)
            st.session_state.comprobado = False
            st.experimental_rerun()

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
    pregunta, correcta = random.choice(preguntas_ahorro)
    respuesta = st.text_input(pregunta, key="ahorro")
    if st.button("Verificar ahorro"):
        if respuesta.strip() == correcta:
            st.success("¡Correcto!")
        else:
            st.error("Incorrecto. Revisa tus cuentas.")

elif categoria == "razonamiento":
    st.subheader("Razonamiento")
    pregunta, correcta = random.choice(preguntas_razonamiento)
    respuesta = st.text_input(pregunta, key="razonamiento")
    if st.button("Verificar razonamiento"):
        if respuesta.strip().lower() == correcta.lower():
            st.success("¡Muy buen razonamiento!")
        else:
            st.error("Piensa un poco más.")
