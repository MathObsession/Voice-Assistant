import pyttsx3
import pyt2s
from ollama import chat
import speech_recognition as sr

answer = []
engine = pyttsx3.init()

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_whisper(audio, model="small")
        print(f"Transcription: {text}")
    except sr.UnknownValueError:
        print("Could not understand audio")

    response = chat(
        model='ministral-3:8b-cloud',
        messages=[
            {'role': 'user', 'content': text},
            {'role': 'system', 'content':f'You are a helpful assistant whose name is churo. You provide concise and to the point answers. Use this context to answer the questions of the user based on the users past chats: {answer} use this information when the user asks a question linked with the past chats. This is the context of the past user questions {text}'}
            ]
    )
    print(response.message.content)
    answer.append(response.message.content)
    engine.setProperty('rate', 155)
    engine.say(response.message.content)
    engine.runAndWait()

    continue_chat=input("Do you want to continue talking to me? ").lower().strip()
    if continue_chat != "yes":
        print("Bye!")
        break

    else:
        continue

