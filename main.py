import pyttsx3
from ollama import chat
import speech_recognition as sr

engine = pyttsx3.init()
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
try:
    text = r.recognize_whisper(audio, model="base")
    print(f"Transcription: {text}")
except sr.UnknownValueError:
    print("Could not understand audio")

response = chat(
    model='granite4:350m-h-q8_0',
    messages=[{'role': 'user', 'content': text}]
)

print(response.message.content)
engine.setProperty('rate', 210)
engine.say(response.message.content)
engine.runAndWait()