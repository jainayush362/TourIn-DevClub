import pyttsx3  # text to speech library
import speech_recognition as sr  # Convert speech to text
import pyaudio
import datetime
import requests
import sys
import json #to handle json compatability
import os
import webbrowser as wb #to open web browser of searches


engine = pyttsx3.init()
rate = engine.getProperty('rate')

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


def climate():
    #OPENWEATHERMAP API
    api_key = "dcf8adda9d8376fbeddac1ecfeb70c00"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "india"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
    response = requests.get(complete_url)
    x = response.json() 

    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        z = x["weather"]  
        weather_description = z[0]["description"]
        speak("Temperature in Celcius unit is")
        speak(current_temperature)
        speak("Overall description of weather is")
        speak(weather_description)
        print(" Temperature (in Celcius unit) = " +
                        str(current_temperature) + 
            "\n Atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n Humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n Description = " +
                        str(weather_description))   
    else:
        speak("Not have any updated data!")

    speak("Do you want to know weather forecast of any particular place or city then say yes else no")
    predictother = userquery().lower()
    if 'yes' in predictother:
        speak("Just speak the name of city of which you want to predict weather forecast")
        city_name = userquery().lower()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
        response = requests.get(complete_url)
        x = response.json() 

        if x["cod"] != "404": 
            y = x["main"] 
            current_temperature = y["temp"] 
            current_pressure = y["pressure"] 
            current_humidiy = y["humidity"] 
            z = x["weather"]  
            weather_description = z[0]["description"]
            speak("Temperature in Celcius unit is")
            speak(current_temperature)
            speak("Overall description of weather is")
            speak(weather_description)
            print("Results : Temperature (in Celcius unit) = " +
                            str(current_temperature) + 
                "\n Atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                "\n Humidity (in percentage) = " +
                            str(current_humidiy) +
                "\n Description = " +
                            str(weather_description))   
        else:
            speak("Not have any updated data!")
            print("Result : City Not Found")
    else:
        speak("You can check again to get updated condition.")
	
	
def about_india():
    speak("India, officially the Republic of India, is a country in South Asia. It is the second-most populous country, the seventh-largest country by land area, and the most populous democracy in the world. One of the oldest civilisations in the world, India is a mosaic of multicultural experiences. With a rich heritage and myriad attractions, the country is among the most popular tourist destinations in the world. Shri Ram Nath Kovind is the President of India and Shri Narendra Damodar Das Modi is the present Prime Minister of India.")
    print("Results : India, officially the Republic of India, is a country in South Asia. It is the second-most populous country, the seventh-largest country by land area, and the most populous democracy in the world. One of the oldest civilisations in the world, India is a mosaic of multicultural experiences. With a rich heritage and myriad attractions, the country is among the most popular tourist destinations in the world. Shri Ram Nath Kovind is the President of India and Shri Narendra Damodar Das Modi is the present Prime Minister of India.")

	
def points_of_attr():
    speak("Just tell me the name of Indian city,village,town,state or district in which you want to see points of attraction.")
    place = userquery().lower()
    wb.open_new("https://www.google.com/search?sclient=psy-ab&site=&source=hp&btnG=Search&q="+place+"+point+of+interest") #Search filtering technique using Google as example


def itenary():
    wb.open_new("https://www.makemytrip.com/")


if __name__ == '__main__':
    wishme()
    query = userquery().lower() #storing all commands in lower case for easy recognition
    if 'climate' in query or 'season' in query or 'weather' in query or 'forecast' in query:
        climate()
    elif 'why to visit india' in query or 'about india' in query or 'why should i visit india' in query or 'information on india' in query or 'what is india' in query:
        about_india()
    elif 'point of attraction' in query or 'points of attraction' in query or 'tourist attractions' in query or "tourist spots" in query or "monuments" in query or "attraction spots" in query or 'places of interests' in query:
        points_of_attr()
    elif 'itinerary' in query or 'booking' in query:
        itenary()
    else:
        speak("I don't have much information on this. Please try something else.")
