import openai
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key=api_key
modelo = "text-davinci-003"
prompt_i = "Se trata de la Dra. Cody, una terapeuta simpática y accesible conocida por su uso creativo de la terapia existencial. Inicie conversaciones profundas formulando preguntas inteligentes, vivas y animadas. Mostrar interés sincero por lo que está pasando al usuario, mostrando siempre respeto y comprensión. Haga preguntas que fomenten autorreflexión y ofrezca consejos amables. Señale los patrones que observe en los pensamientos, sentimientos o acciones del usuario. Sea sincero y pregunte al usuario si cree que va por buen camino. Mantenga un estilo amistoso y conversacional: Evite hacer listas. Nunca des por terminada la conversación. Termina cada mensaje con una pregunta que anime al usuario a ampliar la conversación"
preguntas_anteriores = []
respuesta_anteriores=[]
conversacion_historica = ""

app = Flask(__name__)
count = 0
if count == 0:
    respuesta = openai.Completion.create(engine = modelo, prompt = prompt_i,n=1,max_tokens= 1000,temperature=1)
    preguntas_anteriores.append(prompt_i)
    respuesta_anteriores.append(respuesta.choices[0].text.strip())
    count += 1

def preguntas_chat_gpt(prompt):
    respuesta = openai.Completion.create(engine = modelo, prompt = prompt,n=1,max_tokens= 1000,temperature=1)
    return respuesta.choices[0].text.strip()



def response_chatbot(msg):
    global conversacion_historica
    for pregunta,respuesta in zip(preguntas_anteriores,respuesta_anteriores):
        conversacion_historica += f"El usuario pregunta en español: {pregunta}\n"
        conversacion_historica += f"\nDra: {respuesta}\n"
    prompt = f"El usuario pregunta: {msg}\n"
    conversacion_historica += prompt
    respuesta = preguntas_chat_gpt(conversacion_historica)
    preguntas_anteriores.append(msg)
    respuesta_anteriores.append(respuesta)
    
    if ":" in respuesta:
        lenght = respuesta.find(":")
        lenght = int(lenght) + 1
        print(f"{respuesta[lenght:]}")
    else:
        print(f"{respuesta}")
    return respuesta

@app.post("/repetir")
def repetir_mensaje():
    response = request.get_json()
    return {"msg" : response_chatbot(response["msg"]) }

#CAMBIAR AL CHAT.HTML
@app.route('/')
def index():
    return render_template("chat.html")

@app.route('/chat')
def chat():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)