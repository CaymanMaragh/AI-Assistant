import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
from screenview import start_screen_share
from screenview import take_screenshot
from askAI import ask_gpt



r = sr.Recognizer()

def speak(text):
    print(f"Nexa: {text}")
    try:
        engine = pyttsx3.init()
        # voices = engine.getProperty("voices")
        # engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
    except:
        print("Voice recognition not supported on this platform.")

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        greeting = "Good Morning"
    elif hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    speak(greeting + ". How Can I assist you")

def take_command():
    while(1):
        try:
            with sr.Microphone() as source2:

                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                return MyText
        except sr.UnknownValueError:
            print("Could not understand audio, please try again.")
        except sr.RequestError:
            print("Could not request results; check your internet connection.")

def run_assistant():
    start_screen_share()
    wish_user()
    while True:
        query = take_command()

        if not query:
            continue

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(result)
            except:
                speak("Sorry I could not find anything")
        elif 'open youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open('https://www.youtube.com/')
        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open('https://www.google.com/')
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The current time is " + strTime)
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif 'take screenshot' in query:
            speak("Taking screenshot")
            take_screenshot()
        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a nice day")
            break
        elif 'ask' in query:
            speak(ask_gpt(query)) 
        else:
            speak("Sorry, I did not understand that. Try Again")

run_assistant()