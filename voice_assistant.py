import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 145)
voices = engine.getProperty('voices')
engine.runAndWait()
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        talk('Yes?')
        try:
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-US')
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
            command = ""
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            command = ""
        command = command.lower()
    return command


def run_assistant():
    command = take_command()
    print(command)
    if command != "":
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + current_time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with a WiFi router')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'say hello' in command:
            talk("Hi Sandra! I hope you are fine.")
        else:
            talk('I did not understand.')

