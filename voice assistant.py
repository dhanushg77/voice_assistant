import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import pyjokes
import sys

 

# init pyttsx

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")

 

engine.setProperty('voice', voices[0].id)  # 1 for female and 0 for male voice

 

def speak(audio):

    engine.say(audio)

    engine.runAndWait()

 

def take_command():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening…")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        print("Recognizing…")

        query = r.recognize_google(audio, language='en-in')

        print("User said:" + query + "\n")

    except Exception as e:

        print(e)

        speak("I didnt understand")

        return "None"

    return query

 

if __name__ == '__main__':

 

    speak("Danny assistance activated ")

    speak("How can i help you")

    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia …")

 

            query = query.replace("wikipedia", "")

            results = wikipedia.summary(query, sentences=2)

            speak("According to wikipedia")

            speak(results)

        elif 'are you' in query:
            speak("I am danny developed by Dhanush")
            
           
        elif 'open youtube' in query:

            speak("opening youtube")

            webbrowser.open("youtube.com")

        elif 'open google' in query:

            speak("opening google")

            webbrowser.open("google.com")

        elif "open github" in query:

            speak("opening github")

            webbrowser.open("github.com")

        elif 'open stackoverflow' in query:

            speak("opening stackoverflow")

            webbrowser.open("stackoverflow.com")

        elif 'open spotify' in query:

            speak("opening spotify")

            webbrowser.open("spotify.com")
            

        elif 'play music' in query:

            speak("opening music")

            webbrowser.open("spotify.com")

        elif 'play music' in query:

            speak("opening music")

            webbrowser.open("spotify.com")
            
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
            
        elif 'are you single' in query:
            speak('Nahh..I am in a relationship with wifi')
            
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            sys.exit()
