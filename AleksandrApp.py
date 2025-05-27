import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Aleksandr App", layout="centered")
st.markdown("""
    <style>
        .main {
            background-color: #e6f0ff;
            font-family: 'Comic Sans MS', cursive;
        }
        .title {
            text-align: center;
            font-size: 40px;
            color: #003366;
        }
    </style>
""", unsafe_allow_html=True)

# Logo
st.image("logo_aleksandr.png", use_container_width=True)

st.markdown("<h1 class='title'>Bienvenido a Aleksandr</h1>", unsafe_allow_html=True)

menu = st.selectbox("Elige una categoría para comenzar:", ["Matemáticas", "Lógica", "Ahorro e Inversión", "Pensar y Razonar"])

# Función generalizada para preguntas

def pregunta_interactiva(pregunta_texto, respuesta_correcta, clave_estado):
    if clave_estado not in st.session_state:
        st.session_state[clave_estado] = {"pregunta": pregunta_texto, "respuesta": respuesta_correcta, "chequeado": False, "correcto": None}

    estado = st.session_state[clave_estado]

    st.write(estado["pregunta"])
    respuesta = st.text_input("Tu respuesta:", key=f"input_{clave_estado}")

    if st.button("Comprobar", key=f"check_{clave_estado}") and not estado["chequeado"]:
        estado["chequeado"] = True
        estado["correcto"] = (respuesta.strip().lower() == str(estado["respuesta"]).lower())

    if estado["chequeado"]:
        if estado["correcto"]:
            st.success("¡Correcto!")
        else:
            st.error(f"Incorrecto. La respuesta correcta era {estado['respuesta']}.")
        if st.button("Siguiente", key=f"next_{clave_estado}"):
            del st.session_state[clave_estado]
            st.experimental_rerun()

# Categoría: Matemáticas
if menu == "Matemáticas":
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(['+', '-'])
    resultado = a + b if op == '+' else a - b
    pregunta = f"¿Cuánto es {a} {op} {b}?"
    pregunta_interactiva(pregunta, resultado, "matematica")

# Categoría: Lógica
elif menu == "Lógica":
    ejercicios = [
        ("¿Qué número sigue en la serie? 2, 4, 6, 8, ?", "10"),
        ("Si tienes 3 manzanas y das 1, ¿cuántas te quedan?", "2"),
        ("¿Qué es más pesado, un kilo de plomo o un kilo de plumas?", "ninguno"),
        ("¿Qué día viene después del lunes?", "martes")
    ]
    pregunta, respuesta = random.choice(ejercicios)
    pregunta_interactiva(pregunta, respuesta, "logica")

# Categoría: Ahorro e Inversión
elif menu == "Ahorro e Inversión":
    ejercicios = [
        ("Si ahorras 5 monedas al día por 7 días, ¿cuánto tendrás?", "35"),
        ("Si compras algo de 8 monedas y tienes 10, ¿cuánto te queda?", "2"),
        ("¿Es mejor gastar todo o guardar una parte para después? (gastar/guardar)", "guardar")
    ]
    pregunta, respuesta = random.choice(ejercicios)
    pregunta_interactiva(pregunta, respuesta, "ahorro")

# Categoría: Pensar y Razonar
elif menu == "Pensar y Razonar":
    ejercicios = [
        ("¿Qué harías si ves dinero en el suelo? (devolver/quedarse)", "devolver"),
        ("¿Qué se rompe al decir su nombre?", "el silencio"),
        ("Tengo patas pero no camino. ¿Qué soy?", "mesa")
    ]
    pregunta, respuesta = random.choice(ejercicios)
    pregunta_interactiva(pregunta, respuesta, "razonar")
    
