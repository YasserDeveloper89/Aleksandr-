import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Aleksandr App", layout="centered")

# Estilo personalizado
st.markdown("""
    <style>
        .main {
            background-color: #d0e7f9;
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

menu = st.selectbox("Elige una categoría para comenzar:", [
    "Matemáticas", "Lógica", "Ahorro e Inversión", "Pensar y Razonar"
])

# Función para lógica de ejercicios
def pregunta_interactiva(pregunta_texto, respuesta_correcta, clave_estado):
    if clave_estado not in st.session_state:
        st.session_state[clave_estado] = {
            "pregunta": pregunta_texto,
            "respuesta": respuesta_correcta,
            "chequeado": False,
            "correcto": None
        }

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

# Preguntas por categoría
if menu == "Matemáticas":
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(['+', '-'])
    resultado = a + b if op == '+' else a - b
    pregunta = f"¿Cuánto es {a} {op} {b}?"
    pregunta_interactiva(pregunta, resultado, "matematica")

elif menu == "Lógica":
    preguntas = [
        ("¿Qué número sigue en la serie? 2, 4, 6, 8, ?", "10"),
        ("Si tienes 3 manzanas y das 1, ¿cuántas te quedan?", "2"),
        ("¿Qué es más pesado, un kilo de plomo o un kilo de plumas?", "ninguno"),
        ("¿Qué día viene después del lunes?", "martes"),
        ("¿Qué número falta? 1, 3, 5, ?, 9", "7"),
        ("Si un pato pone un huevo en la frontera, ¿de quién es?", "de nadie"),
        ("¿Cuántos meses tienen 28 días?", "todos"),
        ("¿Qué cosa crece mientras más le quitas?", "hueco"),
        ("¿Qué hay una vez en un minuto, dos veces en un momento, pero nunca en mil años?", "m"),
        ("¿Qué se moja mientras seca?", "toalla")
    ]
    pregunta, respuesta = random.choice(preguntas)
    pregunta_interactiva(pregunta, respuesta, "logica")

elif menu == "Ahorro e Inversión":
    preguntas = [
        ("Si ahorras 5 monedas al día por 7 días, ¿cuánto tendrás?", "35"),
        ("Si compras algo de 8 monedas y tienes 10, ¿cuánto te queda?", "2"),
        ("¿Es mejor gastar todo o guardar una parte para después? (gastar/guardar)", "guardar"),
        ("Si guardas 10 monedas por 5 semanas, ¿cuánto tienes?", "50"),
        ("Si una cosa cuesta 25 monedas y tienes 30, ¿cuánto te sobra?", "5"),
        ("Si inviertes 10 y ganas 5, ¿cuánto tienes?", "15"),
        ("¿Qué es mejor? ¿Tener el dinero en una caja o en un banco?", "banco"),
        ("¿Qué significa invertir?", "hacer crecer el dinero"),
        ("¿Para qué sirve ahorrar?", "futuro"),
        ("¿Qué puedes hacer si quieres comprar algo muy caro?", "ahorrar")
    ]
    pregunta, respuesta = random.choice(preguntas)
    pregunta_interactiva(pregunta, respuesta, "ahorro")

elif menu == "Pensar y Razonar":
    preguntas = [
        ("¿Qué harías si ves dinero en el suelo? (devolver/quedarse)", "devolver"),
        ("¿Qué se rompe al decir su nombre?", "el silencio"),
        ("Tengo patas pero no camino. ¿Qué soy?", "mesa"),
        ("¿Qué puedes atrapar pero no lanzar?", "resfriado"),
        ("¿Qué tiene un ojo pero no puede ver?", "aguja"),
        ("¿Qué tiene dientes pero no muerde?", "peine"),
        ("¿Qué camina sin moverse?", "reloj"),
        ("¿Qué sube pero nunca baja?", "edad"),
        ("¿Qué tiene cuello pero no cabeza?", "camisa"),
        ("¿Qué siempre está delante de ti pero no puedes ver?", "futuro")
    ]
    pregunta, respuesta = random.choice(preguntas)
    pregunta_interactiva(pregunta, respuesta, "razonar")
