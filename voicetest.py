import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
is_done = True

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        print("Voice recognition not supported on this platform.")


for voice in voices:
    if is_done == True:
        is_done == False    
        print(f"Voice ID: {voice.id}")
        print(f"Name: {voice.name}")
        print(f"Gender: {voice.gender}")
        print(f"Languages: {voice.languages}")
        speak("This is what the voice sounds like")
        print("-" * 20)
        is_done == True
