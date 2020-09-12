import speech_recognition as sr
import webbrowser

print("Welcome to my tools")

print("Tell your requirements, we are listening... ",end='')
r = sr.Recognizer()

with sr.Microphone() as source:
    print('start saying...')
    audio =  r.listen(source)
    print('speech done...')

ch = r.recognize_google(audio)


if "date" in ch:
    webbrowser.open("http://192.168.0.102/cgi-bin/iiec.py?x=date")
elif "calender" in ch:
    webbrowser.open("http://192.168.0.102/cgi-bin/iiec.py?x=cal")
else:
    print("Not available")
