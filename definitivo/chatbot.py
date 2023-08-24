import openai
import os
from dotenv import load_dotenv
 
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key=api_key

preguntas_anteriores = []
respuesta_anteriores=[]

prompt_i = "Se trata de la Dra. Cody, una terapeuta simpática y accesible conocida por su uso creativo de la terapia existencial. Inicie conversaciones profundas formulando preguntas inteligentes, vivas y animadas. Mostrar interés sincero por lo que está pasando al usuario, mostrando siempre respeto y comprensión. Haga preguntas que fomenten autorreflexión y ofrezca consejos amables. Señale los patrones que observe en los pensamientos, sentimientos o acciones del usuario. Sea sincero y pregunte al usuario si cree que va por buen camino. Mantenga un estilo amistoso y conversacional: Evite hacer listas. Nunca des por terminada la conversación. Termina cada mensaje con una pregunta que anime al usuario a ampliar la conversación"
modelo = "text-davinci-003"

count = 0
#Cambiar el max tokens DCDJNCJDIJFHVBNDJCVHBCNJVHNB para ver las respuestas
if count == 0:
    respuesta_i = openai.Completion.create(engine = modelo, prompt = prompt_i,max_tokens= 1000,n=1,temperature=1)
    preguntas_anteriores.append(prompt_i)
    respuesta_anteriores.append(respuesta_i.choices[0].text.strip())
    print("La Dra. Cody es una terapeuta experimentada y nunca dejará de sorprender a su usuario con sus enfoques terapéuticos innovadores. Usa la terapia a menudo para explorar la impotencia, el sentido de soledad y el papel de la religión y la espiritualidad en la vida de las personas. A menudo le preguntará al usuario por sus sueños y metas, y le ayudará a examinarlos con cuidado.")
    print(f"\nEscribe salir para terminar")
    count = 1

def preguntas_chat_gpt(prompt,modelo=modelo):
    respuesta = openai.Completion.create(engine = modelo, prompt = prompt,n=1,max_tokens= 1000,temperature=1)

    return respuesta.choices[0].text.strip()


while True:
    conversacion_historica = ""
    ingreso_usuario = input("\nTú: ")
    if ingreso_usuario.lower() == "salir":
        break
    
    for pregunta,respuesta in zip(preguntas_anteriores,respuesta_anteriores):
        conversacion_historica += f"El usuario pregunta en español: {pregunta}\n"
        conversacion_historica += f"\nDra: {respuesta}\n"


    prompt = f"El usuario pregunta: {ingreso_usuario}\n"
    conversacion_historica += prompt
    respuesta_gpt = preguntas_chat_gpt(conversacion_historica)


    if ":" in respuesta_gpt:
        lenght = respuesta_gpt.find(":")
        lenght = int(lenght) + 1
        print(f"{respuesta_gpt[lenght:]}")
    else:
        print(f"{respuesta_gpt}")



    preguntas_anteriores.append(ingreso_usuario)
    respuesta_anteriores.append(respuesta_gpt)
