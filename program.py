import pyttsx3  #text to speech library
import speech_recognition as sr  # Convert speech to text
import pyaudio


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-50)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def listen():
	rec=sr.Recognizer()
	with sr.Microphone() as source:
		rec.pause_threshold=1
		print("Listening......")
		audio = rec.listen(source)

	try:
		print("Recognizing......")
		recquery = rec.recognize_google(audio,language='en-US,en-IN')
		print("You: ",recquery)
	except Exception as e:
		# print(e)
		print("Say that again please.....")
		return "None"
	return recquery

if __name__ == '__main__':
	s="Hloo"
	speak(s)
	listen() 
