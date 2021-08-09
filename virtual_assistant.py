
import speech_recognition as sr 
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia

# nombre del asistente
name = 'wachin'

# la clave de api
key = 'YOUR_API_KEY_HERE'

# Tecla para apagar el programa 
flag = 1

listener = sr.Recognizer()

engine = pyttsx3.init()

# Consigue voces y establece la primera de ellas
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# editar la configuracion predeterminada
engine. setProperty('rate', 178)
engine.setProperty('volume', 0.7)

def talk(text):
    '''
        aca puede hablar wachin
    '''
    engine.say(text)
    engine.runAndWait()

def listen():
    '''
        el programa recibi nuestra voz  y envia una funcion
    '''
    flag = 1
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            
            if name in rec:
                rec = rec.replace(name, '')
                flag = run(rec)
            else:
                talk("Habla bien bobo " + rec)
    except:
        pass
    return flag

def run(rec):
    '''
        All the actions that virtual assistant can do
    '''
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        wikipedia.set_lang("es")
        info = wikipedia.summary(order, 1)
        talk(info)
    elif 'sali' in rec:
        flag = 0
        talk("Nos vemos wacho...")
    else:
        talk("Habla bien te dije " + rec)
    return flag

while flag:
    flag = listen()