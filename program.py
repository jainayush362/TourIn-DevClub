import pyttsx3  # text to speech library
import speech_recognition as sr  # Convert speech to text
import pyaudio
import datetime


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def userquery():
	rec = sr.Recognizer()
	with sr.Microphone() as source:
		rec.pause_threshold = 1
		print("Listening......")
		audio = rec.listen(source)

	try:
		print("Recognizing......")
		recquery = rec.recognize_google(audio, language='en-US,en-IN')
		print("You: ", recquery)
	except Exception as e:
		# print(e)
		print("Say that again please.....")
		return "None"
	return recquery

def timepredict():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The Current time is")
    speak(time)

def datepredict():
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    speak("Today is")
    speak(day)
    speak(month)
    speak(year)

def greet():
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    elif hour>=17 and hour<19:
        speak("Good Evening")
    else:
        speak("Good Night")

def wishme():
    print("*******WELCOME TO Indian Tourism Assistant*********")
    speak("Namaste, Welcome to TourIN, Indian Tourism Assistant")
    speak("May I know your name")
    name=userquery()
    speak("Hello")
    speak(name)
    timepredict()
    datepredict()
    greet()
    speak("TourIN at your service")
    speak("How may I help you today")






if __name__ == '__main__':
    wishme()
