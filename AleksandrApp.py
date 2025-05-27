import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Aleksandr App", layout="centered")

# Cargar logo
logo = Image.open("logo_aleksandr.png")
st.image(logo, use_container_width=True)

st.markdown("<h1 style='text-align: center; color: #2b5fa0;'>Bienvenido a Aleksandr</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #444;'>Una app educativa interactiva para niños superdotados</h4>", unsafe_allow_html=True)

# Menú principal
menu = st.sidebar.selectbox("Selecciona una materia", ["Inicio", "Matemáticas", "Lógica", "Ahorro e Inversiones", "Pensamiento y Razonamiento"])

if menu == "Inicio":
    st.write("Elige una materia en el menú para comenzar a estudiar.")
    st.success("¡Vamos a aprender cosas increíbles!")

# -------------------- MATEMÁTICAS --------------------
elif menu == "Matemáticas":
    st.header("Ejercicios de Matemáticas")
    operations = ['+', '-']
    
    if "math_question" not in st.session_state:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        op = random.choice(operations)
        st.session_state.math_question = (a, b, op)
    
    a, b, op = st.session_state.math_question
    if op == '+':
        result = a + b
    else:
        result = a - b
    
    st.write(f"¿Cuánto es {a} {op} {b}?")
    user_answer = st.number_input("Tu respuesta:", step=1)
    
    if st.button("Comprobar"):
        if user_answer == result:
            st.success("¡Correcto! Muy bien.")
        else:
            st.error(f"Incorrecto. La respuesta era {result}")
        del st.session_state.math_question

# -------------------- LÓGICA --------------------
elif menu == "Lógica":
    st.header("Ejercicios de Lógica")
    preguntas = [
        ("¿Qué número sigue en la secuencia? 2, 4, 6, 8, ...", "10"),
        ("Si ayer fue lunes, ¿qué día es mañana?", "miércoles"),
        ("¿Cuántos lados tiene un triángulo?", "3"),
        ("¿Qué pesa más, 1kg de plomo o 1kg de algodón?", "iguales"),
        ("¿Cuál es la mitad de 10?", "5"),
        ("Si tienes 3 manzanas y comes 2, ¿cuántas quedan?", "1"),
        ("¿Qué letra sigue: A, C, E, G, ...?", "I"),
        ("¿Cuántos meses tienen 28 días?", "12"),
        ("Si un tren va a 100 km/h, ¿cuántos km recorrerá en 2 horas?", "200"),
        ("¿Cuál es el opuesto de noche?", "día")
    ]
    
    if "logic_q" not in st.session_state:
        st.session_state.logic_q = random.choice(preguntas)
    
    q, correct = st.session_state.logic_q
    st.write(q)
    answer = st.text_input("Tu respuesta:")
    
    if st.button("Comprobar"):
        if answer.strip().lower() == correct.lower():
            st.success("¡Correcto!")
        else:
            st.error(f"Incorrecto. La respuesta era: {correct}")
        del st.session_state.logic_q

# -------------------- AHORRO E INVERSIONES --------------------
elif menu == "Ahorro e Inversiones":
    st.header("Conceptos Básicos de Ahorro")
    conceptos = [
        ("¿Qué es ahorrar?", "Guardar parte del dinero para el futuro."),
        ("¿Por qué es importante ahorrar?", "Para estar preparados ante emergencias."),
        ("¿Qué es una alcancía?", "Un lugar donde se guarda dinero."),
        ("¿Qué es una inversión?", "Poner dinero para que crezca con el tiempo."),
        ("¿Cuál es mejor, gastar todo o ahorrar una parte?", "Ahorrar una parte."),
        ("¿Qué es un banco?", "Lugar donde puedes guardar dinero seguro."),
        ("¿Qué significa presupuesto?", "Plan para gastar el dinero."),
        ("¿Qué es una meta de ahorro?", "Un objetivo que quieres alcanzar con tus ahorros."),
        ("¿Debes gastar todo tu dinero en dulces?", "No, debes ahorrar una parte."),
        ("¿Cómo puedes ganar dinero?", "Ayudando en casa, vendiendo algo o trabajando.")
    ]
    
    if "ahorro_q" not in st.session_state:
        st.session_state.ahorro_q = random.choice(conceptos)
    
    pregunta, respuesta = st.session_state.ahorro_q
    st.write(pregunta)
    respuesta_usuario = st.text_area("Tu respuesta:")
    
    if st.button("Verificar"):
        st.info(f"Una buena respuesta sería: {respuesta}")
        del st.session_state.ahorro_q

# -------------------- PENSAMIENTO Y RAZONAMIENTO --------------------
elif menu == "Pensamiento y Razonamiento":
    st.header("Ejercicios para Pensar Mejor")
    ejercicios = [
        "Imagina que tienes que construir una casa con bloques. ¿Qué harías primero?",
        "Si un amigo está triste, ¿cómo puedes ayudarlo?",
        "Si tienes 5 juguetes y regalas 2, ¿cuántos te quedan?",
        "Si llueve, ¿qué necesitas para no mojarte?",
        "¿Cómo resolverías un problema si no tienes todas las piezas?",
        "¿Qué harías si ves un billete en la calle?",
        "Si tienes dos caminos para llegar a casa, ¿cómo eliges el mejor?",
        "¿Por qué es bueno preguntar cuando no sabes algo?",
        "Si tienes sueño pero aún no es hora de dormir, ¿qué haces?",
        "¿Por qué es importante escuchar a los demás?"
    ]
    
    st.write(random.choice(ejercicios))
    st.text_area("Tu reflexión:")
