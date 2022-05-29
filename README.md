# python-voice-assistant
This repo contains a very simple and basic voice assistant written in Python

# How to install
To install on Windows be sure to install pipwin:  
```pip install pipwin```  
and use it to install some specific modules:  
```pipwin install pyaudio```

To start the voice assistant:  
```python wake_word_detection.py```

Some simple test commands are implemented:
```
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
        elif 'hello' in command:
            talk("Hi!")
        else:
            talk('I did not understand. Please try commands like play, time, who is, or joke.')
```
