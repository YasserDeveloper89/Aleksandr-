import streamlit as st import random from PIL import Image

st.set_page_config(page_title="Aleksandr App", layout="centered")

--- Logo ---

st.image("logo_aleksandr.png", use_container_width=True)

st.markdown(""" <h1 style='text-align: center; color: #1f4e79;'>¡Bienvenido a Aleksandr!</h1> <p style='text-align: center; font-size: 20px;'>Una app educativa interactiva para niños con talento y visión de futuro.</p> """, unsafe_allow_html=True)

--- Estilo con CSS ---

st.markdown(""" <style> .main { background-color: #f0f6ff; } h2 { color: #2c3e50; } .block-container { padding-top: 2rem; padding-bottom: 2rem; } </style> """, unsafe_allow_html=True)

--- Navegación de menú ---

menu = st.selectbox("Elige una categoría para comenzar a aprender:", [ "Matemáticas", "Lógica", "Ahorro e Inversiones", "Razonamiento Práctico" ])

--- Funciones para ejercicios ---

def mostrar_operacion(tipo): if "pregunta" not in st.session_state: if tipo == "+": a, b = random.randint(1, 50), random.randint(1, 50) st.session_state.pregunta = f"¿Cuánto es {a} + {b}?" st.session_state.respuesta = a + b elif tipo == "-": a, b = random.randint(20, 70), random.randint(1, 20) st.session_state.pregunta = f"¿Cuánto es {a} - {b}?" st.session_state.respuesta = a - b

st.subheader(st.session_state.pregunta)
user_answer = st.number_input("Tu respuesta:", step=1, format="%d")
if st.button("Responder"):
    if user_answer == st.session_state.respuesta:
        st.success("¡Correcto!")
    else:
        st.error("Incorrecto. ¡Sigue intentando!")
    del st.session_state.pregunta
    del st.session_state.respuesta

--- Contenido por categoría ---

if menu == "Matemáticas": st.header("Ejercicios de Matemáticas") operacion = st.radio("Elige el tipo de operación:", ["Suma", "Resta"]) if operacion == "Suma": mostrar_operacion("+") else: mostrar_operacion("-")

elif menu == "Lógica": st.header("Ejercicios de Lógica") ejercicios = [ ("¿Qué número sigue en la secuencia: 2, 4, 6, ?", 8), ("¿Qué figura tiene 4 lados iguales?", "cuadrado"), ("¿Cuál es el opuesto de 'noche'?", "día"), ("¿Cuántos días hay en una semana?", 7), ("¿Cuál es el primer mes del año?", "enero"), ("¿Qué animal dice 'miau'?", "gato"), ("¿Qué color resulta de mezclar rojo y azul?", "morado"), ("¿Cuánto es 10 dividido por 2?", 5), ("¿Qué sentido usamos para oír?", "oído"), ("¿Cuál es el opuesto de arriba?", "abajo") ] pregunta, respuesta = random.choice(ejercicios) st.subheader(pregunta) user_input = st.text_input("Tu respuesta:").lower() if st.button("Responder"): if str(respuesta) == user_input: st.success("¡Muy bien!") else: st.error("Respuesta incorrecta, intenta otra vez.")

elif menu == "Ahorro e Inversiones": st.header("Aprende sobre Ahorro e Inversiones") conceptos = [ ("¿Qué es ahorrar?", "guardar dinero para el futuro"), ("¿Dónde podemos guardar nuestro dinero de forma segura?", "banco"), ("¿Qué es una hucha?", "una caja para ahorrar dinero"), ("¿Qué significa invertir?", "usar dinero para ganar más dinero"), ("¿Por qué es importante el ahorro?", "para emergencias o metas futuras"), ("¿Qué es un presupuesto?", "plan para gastar el dinero"), ("¿Debemos gastar todo lo que ganamos?", "no"), ("¿Qué es un ingreso?", "dinero que recibimos"), ("¿Qué es un gasto?", "dinero que usamos"), ("¿Por qué es bueno tener metas de ahorro?", "para comprar cosas importantes") ] pregunta, respuesta = random.choice(conceptos) st.subheader(pregunta) user_input = st.text_input("Tu respuesta:").lower() if st.button("Enviar Respuesta"): if respuesta in user_input: st.success("¡Correcto!") else: st.error("No es la respuesta correcta, sigue aprendiendo.")

elif menu == "Razonamiento Práctico": st.header("Ejercicios de Razonamiento Práctico") retos = [ ("Si tienes 3 manzanas y te dan 2 más, ¿cuántas tienes en total?", 5), ("Tienes 10 caramelos y das 4, ¿cuántos te quedan?", 6), ("Vas a la tienda con 10 euros y compras algo que cuesta 7, ¿cuánto te queda?", 3), ("Si ves 5 pájaros en un árbol y 2 vuelan, ¿cuántos quedan?", 3), ("Si caminas 3 pasos hacia adelante y luego 2 hacia atrás, ¿cuántos pasos avanzaste?", 1), ("Tienes 8 lápices y pierdes 3, ¿cuántos tienes ahora?", 5), ("Si estudias 2 horas al día durante 5 días, ¿cuántas horas estudiaste?", 10), ("Si compras 2 juguetes por 5 euros cada uno, ¿cuánto gastaste?", 10), ("Si ahorras 1 euro cada día durante 7 días, ¿cuánto tienes?", 7), ("Si tienes 12 globos y se revientan 4, ¿cuántos te quedan?", 8) ] pregunta, respuesta = random.choice(retos) st.subheader(pregunta) user_input = st.number_input("Tu respuesta:", step=1) if st.button("Comprobar"): if int(user_input) == respuesta: st.success("¡Excelente trabajo!") else: st.error("Ups, no es correcto. ¡Intenta otra vez!")

