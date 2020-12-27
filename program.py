import tkinter as tk #FOR GUI Development
from tkinter import TOP,BOTTOM
import tkinter.messagebox
import pyttsx3 #text to speech library
import datetime #date and time library
import pyaudio #to enable microphone use
import speech_recognition as sr #user speech recognition library
import wikipedia #to get information about india and different states/heritage/culture
import webbrowser as wb #to open web browser of searches
import requests
import sys
import json #to handle json compatability
from amadeus import Client, ResponseError #AMADEUS DEVELOPER API
from  geopy.geocoders import Nominatim #GeoPy and Nominatim to retrieve lat & long of city
from playsound import playsound #to play audio
import os
from twilio.rest import Client as cl #making calls/messages API TWILIO

#API's USED IN THE PROJECT : TWILIO, IPSTACK, TEACHABLE MACHIENE, AMADEUS, DISTANCEMATRIX, OPENWEATHERMAP

engine = pyttsx3.init() #initiating the text to speech engine
rate = engine.getProperty('rate') #getting the speech word rate per minute

def speak(audio):
	engine.say(audio)
	engine.runAndWait()


def userquery():
	rec = sr.Recognizer()
	with sr.Microphone() as source: #Using microphone with help of PyAudio
		print("Listening...")
		rec.pause_threshold = 1
		audio = rec.listen(source)
	
	try:
		print("Recognizing...")
		recquery = rec.recognize_google(audio, language='en-US, en-IN, en-AU') #Recognizing using google speech recognizer
		print("You :"+ recquery)
	except Exception:
		print("Say that again please...")
		return "None"
	return recquery


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


def distance_calc():
	#DISTANCEMATRIX API
	speak("Tell me the name of your current city")
	
	geolocator = Nominatim(user_agent="jainayush362@gmail.com")
	cur_city_dist = userquery().lower()
	loc_cur_city_dist = geolocator.geocode(cur_city_dist)

	speak("Now tell me the name of destination city")
	des_city_dist = userquery().lower()
	loc_des_city_dist = geolocator.geocode(des_city_dist)

	api_key = "TG5q5VdV4PUNEO2fpfzw4uxHwhpc6"
	base_url = "https://api.distancematrix.ai/maps/api/distancematrix/json?"
	complete_url = base_url + "origins=" + str(loc_cur_city_dist.latitude) + "," + str(loc_cur_city_dist.longitude) + "&destinations=" + str(loc_des_city_dist.latitude) + "," + str(loc_des_city_dist.longitude) + "&departure_time=now" + "&key=" + api_key
	response = requests.get(complete_url)
	xdis = response.json()

	if xdis["status"]=="OK":
		ydis = xdis["rows"]
		edis = ydis[0]["elements"]
		ddis = edis[0]["distance"]
		dis_text = ddis["text"]
		speak("The distance for given journey is")
		speak(dis_text)
		print("Results : The distance for given journey is : "+dis_text)
	else:
		speak("Not have much information")
		print("Result : No data found")


def duration_calc():
	#DISTANCEMATRIX API
	speak("Tell me the name of your current city")
	
	geolocator = Nominatim(user_agent="jainayush362@gmail.com")
	cur_city = userquery().lower()
	loc_cur_city = geolocator.geocode(cur_city)

	speak("Now tell me the name of destination city")
	des_city = userquery().lower()
	loc_des_city = geolocator.geocode(des_city)

	api_key = "TG5q5VdV4PUNEO2fpfzw4uxHwhpc6"
	base_url = "https://api.distancematrix.ai/maps/api/distancematrix/json?"
	complete_url = base_url + "origins=" + str(loc_cur_city.latitude) + "," + str(loc_cur_city.longitude) + "&destinations=" + str(loc_des_city.latitude) + "," + str(loc_des_city.longitude) + "&departure_time=now" + "&key=" + api_key
	response = requests.get(complete_url)
	xd = response.json()

	if xd["status"]=="OK":
		yd = xd["rows"]
		ed = yd[0]["elements"]
		dd = ed[0]["duration"]
		dura_text = dd["text"]
		speak("The duration for given journey is")
		speak(dura_text)
		print("Results : The duration for given journey is : "+dura_text)
	else:
		speak("Not have much information")
		print("Result : No data found")


def airports():
	wb.open_new("https://www.aai.aero/en/content/how-many-international-airports-are-india-and-which-are-they")
	speak("The given are the official international airpotrs in india till date as per airports authority of india.")


def visa():
	speak("Official details related to registeration of Visa is available on the official website of Indian Govenrnment that is indianvisaonline.gov.in. You should not trust any other source or application.")
	wb.open_new("https://indianvisaonline.gov.in/")
	print("Results : Official details related to registeration of Visa is available on the official website of Indian Govenrnment that is indianvisaonline.gov.in. You should not trust any other source or application.")


def places_data():
	month = datetime.datetime.now().month
	if month in [12, 1]:
		speak("During winter season it is best to visit Kerala, Chennai, Jaipur, Udaipur, Jodhpur, Karnataka, Uttarakhand, Gujarat, Maharashtra, Lakshadweep, Goa, Delhi, Kashmir, Mussoorie, Agra, Varanasi, Lucknow")
		print("Results : During winter season it is best to visit Kerala, Chennai, Jaipur, Udaipur, Jodhpur, Karnataka, Uttarakhand, Gujarat, Maharashtra, Lakshadweep, Goa, Delhi, Kashmir, Mussoorie, Agra, Varanasi, Lucknow")
	elif month in [2, 3]:
		speak("During Spring season its best to visit Ooty, Kashmir, Nagaland, Andaman and Nicobar Islands, Kasol, Hampi, Kerela, Goa and Darjeeling.")
		print("Results : During Spring season its best to visit Ooty, Kashmir, Nagaland, Andaman and Nicobar Islands, Kasol, Hampi, Kerela, Goa and Darjeeling.")
	elif month in [4, 5, 6]:
		speak("During summer season it is best to visit Shimla, Manali, Andaman and Nicobar, Darjeeling, Rishikesh, Shilong, Laksdweep, Ooty, Gangtok, Ladakh, Dalhousie, Nanital, Uttrakhand")
		print("Results : During summer season it is best to visit Shimla, Manali, Andaman and Nicobar, Darjeeling, Rishikesh, Shilong, Laksdweep, Ooty, Gangtok, Ladakh, Dalhousie, Nanital, Uttrakhand")
	elif month in [7, 8, 9]:
		speak("During monsoon season it is best to visit Kashmir, Jaisalmer, Pondicherry, Kinnaur, Meghalaya, Jaipur, Gujrat, Mysore, Uttrakhand, Jodhpur, Ladakh, Agra, Varanasi, Lucknow, Delhi")
		print("Results : During mmonsoon season it is best to visit Kashmir, Jaisalmer, Pondicherry, Kinnaur, Meghalaya, Jaipur, Gujrat, Mysore, Uttrakhand, Jodhpur, Ladakh, Agra, Varanasi, Lucknow, Delhi")
	else:
		speak("During Autumn season you must visit to Kashmir, Kerala, Mysore, Gujarat, Uttarakhand , Kolkata, Darjeeling, Pushkar, Ladakh to see the dazzling fall colour.")
		print("Results : During Autumn season you must visit to Kashmir, Kerala, Mysore, Gujarat, Uttarakhand , Kolkata, Darjeeling, Pushkar, Ladakh to see the dazzling fall colour.")


def points_of_attr():
	speak("Just tell me the name of Indian city,village,town,state or district in which you want to see points of attraction.")
	place = userquery().lower()
	wb.open_new("https://www.google.com/search?sclient=psy-ab&site=&source=hp&btnG=Search&q="+place+"+point+of+interest") #Search filtering technique using Google as example


def identify():
	wb.open_new("C:\\Users\\Ayush\\Desktop\\devclub\\index.html") #External HTML page opening to detect images using webcam
	speak("Please face the camera towards the monument to start identifying.")


def itenary():
	wb.open_new("https://www.makemytrip.com/")


def emergency():
	account_sid = 'ACae22c9ee3cb3e33f9f10182e29dd41a3'
	auth_token = '05fab44d42ec33b37585bab31b8ef581'
	send_url = "http://api.ipstack.com/check?access_key=0fbd1f7d2671232974fce0727cea581a" #IPStack API
	geo_req = requests.get(send_url)
	geo_json = json.loads(geo_req.text)
	tor_city = geo_json['city'].lower()
	tor_country = geo_json['country_name'].lower()
	tor_lat = geo_json['latitude']
	tor_long = geo_json['longitude'].lower()
	tor_zip = geo_json["zip"]
	tor_regname = geo_json["region_name"].lower()
	speak("What kind of emergency are you in? Accident, Medical, Fire or Police")
	emer = userquery().lower()
	if tor_country == 'india':
		if "fire" in emer:
			client = cl(account_sid, auth_token)
			call = client.calls.create(
								url='http://demo.twilio.com/docs/voice.xml',
								to='+917838379279',
								from_='+12058517339'
							)
			print(call.sid)
			mess = "Tourist in Fire Emergency. Location :"+str(tor_regname)+","+str(tor_city)+","+str(tor_country)+" Latitude:"+str(tor_lat)+" Longitude:"+str(tor_long)
			message = client.messages .create(body=mess,from_='+12058517339',to='+917838379279')
			print(message.sid)
			speak("These are the nearest Fire Stations in your location")
			wb.open_new("https://www.google.com/maps/search/Firestations/@"+tor_lat+","+tor_long)
			playsound('C:\\Users\\Ayush\\Desktop\\devclub\\images\\alarm.mp3')
		elif "accident" in emer or 'medical' in emer or 'ambulance' in emer:
			client = cl(account_sid, auth_token)
			call = client.calls.create(
								url='http://demo.twilio.com/docs/voice.xml',
								to='+917838379279',
								from_='+12058517339'
							)
			print(call.sid)
			mess = "Tourist in Medical Emergency. Location :"+str(tor_regname)+","+str(tor_city)+","+str(tor_country)+" Latitude:"+str(tor_lat)+" Longitude:"+str(tor_long)
			message = client.messages .create(body=mess,from_='+12058517339',to='+917838379279')
			print(message.sid)
			speak("These are the nearest Hospitals in your location")
			wb.open_new("https://www.google.com/maps/search/Hospitals/@"+tor_lat+","+tor_long)
			playsound('C:\\Users\\Ayush\\Desktop\\devclub\\images\\alarm.mp3')
		elif 'police' in emer or 'theft' in emer or 'robbery' in emer or 'kidnap' in emer or 'lost' in emer:
			client = cl(account_sid, auth_token)
			call = client.calls.create(
								url='http://demo.twilio.com/docs/voice.xml',
								to='+917838379279',
								from_='+12058517339'
							)
			print(call.sid)
			mess = "Tourist in Emergency. Location :"+str(tor_regname)+","+str(tor_city)+","+str(tor_country)+" Latitude:"+str(tor_lat)+" Longitude:"+str(tor_long)
			message = client.messages .create(body=mess,from_='+12058517339',to='+917838379279')
			print(message.sid)
			speak("These are the nearest Police Stations in your location")
			wb.open_new("https://www.google.com/maps/search/Policestations/@"+tor_lat+","+tor_long)
			playsound('C:\\Users\\Ayush\\Desktop\\devclub\\images\\alarm.mp3')
		else:
			speak("These are the nearest Police Stations in your location")
			wb.open_new("https://www.google.com/maps/search/Policestations/@"+tor_lat+","+tor_long)

	else:
		speak("Its seems that presently you are not in India. Dial these numbers in case of emergency while you are in India:")
		speak("For Police Dial : One Zero Zero")
		speak("For Ambulance Dial : One Zero Two")
		speak("For Fire Dial : One Zero One")


def activity():
	speak("Please tell the City for which you want to explore the activities?")
	t="Please tell the City for which you want to explore the activities?"
	placename = userquery().lower()
	geolocator = Nominatim(user_agent="jainayush362@gmail.com")
	city = placename
	country ="India"
	loca = geolocator.geocode(city+','+ country)
	#print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)

	amadeus = Client(client_id='Aq3qAwphK1SyDHjYnlABOc12OO2AHG82',client_secret='6h5fmOnNwCSSHfAd')
	try:
		response = amadeus.shopping.activities.get(latitude=loca.latitude, longitude=loca.longitude)
		speak("Following are the Activities for given location"+placename)
		tkinter.messagebox.showinfo('Result for Query',response.data)
		print(response.data)
	except ResponseError as error:
		print(error)


#GUI Part of App
class Application(tk.Frame):
	
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def createCanvas(self, canvas_width, canvas_height):
		canvas = tk.Canvas(self.master, width=canvas_width, height=canvas_height)
		return canvas

	def addImage(self, canvas, filename, image_x, image_y, direction=tk.NW):
		self.img = tk.PhotoImage(file=filename) # Create PhotoImage object
		canvas.create_image(image_x, image_y, anchor=direction, image=self.img) # Create the image on our canvas
		return canvas

	def create_widgets(self):
		frame = tk.Frame(self)
		frame.grid()
		self.loadimage = tk.PhotoImage(file="images//acti.png")
		self.hi_there = tk.Button(frame, image=self.loadimage, bg="white", activebackground="yellow", command=activity)
		# self.hi_there["command"] = activity()
		self.hi_there["border"] = "2"
		self.hi_there.grid(row=0,column=0,padx=20,pady=20)
		self.lab = tk.Label(frame, text="Activities", font=("bold",13), anchor="s")
		self.lab.place(x=21,y=90)

		self.loadimage1 = tk.PhotoImage(file="images//climate.png")
		self.hi1_there = tk.Button(frame, image=self.loadimage1, bg="white", activebackground="yellow")
		self.hi1_there["command"] = climate
		self.hi1_there["border"] = "2"
		self.hi1_there.grid(row=0, column=1, padx=20,pady=20)
		self.lab1 = tk.Label(frame, text="Weather", font=("bold",13), anchor="s")
		self.lab1.place(x=130,y=90)

		self.loadimage2 = tk.PhotoImage(file="images//poa.png")
		self.hi2_there = tk.Button(frame, image=self.loadimage2, bg="white", activebackground="yellow")
		self.hi2_there["command"] = points_of_attr
		self.hi2_there["border"] = "2"
		self.hi2_there.grid(row=0, column=2, padx=20,pady=20)
		self.lab2 = tk.Label(frame, text="Attractions", font=("bold",13), anchor="s")
		self.lab2.place(x=236,y=90)

		self.loadimage3 = tk.PhotoImage(file="images//visa.png")
		self.hi3_there = tk.Button(frame, image=self.loadimage3, bg="white", activebackground="yellow")
		self.hi3_there["command"] = visa
		self.hi3_there["border"] = "2"
		self.hi3_there.grid(row=0, column=3, padx=20,pady=20)
		self.lab3 = tk.Label(frame, text="Visa", font=("bold",13), anchor="s")
		self.lab3.place(x=365,y=90)

		self.loadimage4 = tk.PhotoImage(file="images//india.png")
		self.hi4_there = tk.Button(frame, image=self.loadimage4, bg="white", activebackground="yellow")
		self.hi4_there["command"] = about_india
		self.hi4_there["border"] = "2"
		self.hi4_there.grid(row=0, column=4, padx=20,pady=20)
		self.lab4 = tk.Label(frame, text="About India", font=("bold",13), anchor="s")
		self.lab4.place(x=450,y=90)

		self.loadimage5 = tk.PhotoImage(file="images//itinerary.png")
		self.hi5_there = tk.Button(frame, image=self.loadimage5, bg="white", activebackground="yellow")
		self.hi5_there["command"] = itenary
		self.hi5_there["border"] = "2"
		self.hi5_there.grid(row=0, column=5, padx=20,pady=20)
		self.lab5 = tk.Label(frame, text="Booking", font=("bold",13), anchor="s")
		self.lab5.place(x=575,y=90)

		self.loadimage6 = tk.PhotoImage(file="images//identify.png")
		self.hi6_there = tk.Button(frame, image=self.loadimage6, bg="white", activebackground="yellow")
		self.hi6_there["command"] = identify
		self.hi6_there["border"] = "2"
		self.hi6_there.grid(row=1, column=0, padx=20,pady=20)
		self.lab6 = tk.Label(frame, text="Identify It", font=("bold",13), anchor="s")
		self.lab6.place(x=18,y=200)

		self.loadimage7 = tk.PhotoImage(file="images//duration.png")
		self.hi7_there = tk.Button(frame, image=self.loadimage7, bg="white", activebackground="yellow")
		self.hi7_there["command"] = duration_calc
		self.hi7_there["border"] = "2"
		self.hi7_there.grid(row=1, column=1, padx=20,pady=20)
		self.lab7 = tk.Label(frame, text="Duration", font=("bold",13), anchor="s")
		self.lab7.place(x=130,y=200)

		self.loadimage8 = tk.PhotoImage(file="images//distance.png")
		self.hi8_there = tk.Button(frame, image=self.loadimage8, bg="white", activebackground="yellow")
		self.hi8_there["command"] = distance_calc
		self.hi8_there["border"] = "2"
		self.hi8_there.grid(row=1, column=2, padx=20,pady=20)
		self.lab8 = tk.Label(frame, text="Distance", font=("bold",13), anchor="s")
		self.lab8.place(x=240,y=200)

		self.loadimage9 = tk.PhotoImage(file="images//emergency.png")
		self.hi9_there = tk.Button(frame, image=self.loadimage9, bg="white", activebackground="yellow")
		self.hi9_there["command"] = emergency
		self.hi9_there["border"] = "2"
		self.hi9_there.grid(row=1, column=3, padx=20,pady=20)
		self.lab9 = tk.Label(frame, text="Emergency", font=("bold",13), anchor="s")
		self.lab9.place(x=345,y=200)

		self.loadimage10 = tk.PhotoImage(file="images//airport.png")
		self.hi10_there = tk.Button(frame, image=self.loadimage10, bg="white", activebackground="yellow")
		self.hi10_there["command"] = airports
		self.hi10_there["border"] = "2"
		self.hi10_there.grid(row=1, column=4, padx=20,pady=20)
		self.lab10 = tk.Label(frame, text="Airports", font=("bold",13), anchor="s")
		self.lab10.place(x=465,y=200)

		self.loadimage11 = tk.PhotoImage(file="images//india1.png")
		self.hi11_there = tk.Button(frame, image=self.loadimage11, bg="white", activebackground="yellow")
		self.hi11_there["command"] = places_data
		self.hi11_there["border"] = "2"
		self.hi11_there.grid(row=1, column=5, padx=20,pady=20)
		# self.lab11 = tk.Label(frame, text="Places to Visit", font=("bold",13), anchor="s")
		# self.lab11.place(x=550,y=200)
		#
		# label_frame = tk.LabelFrame(self, text='This is Label Frame',bg="white",height=50,width=500,fg="black")
		# label_frame.grid(row=2,column=1)
		#
		# label1 = tk.Label(label_frame, text='1. This is a Label.')
		# label1.place(x=0, y=5)
		#
		# label2 = tk.Label(label_frame, text='2. This is another Label.')
		# label2.place(x=0, y=35)
		#
		# label3 = tk.Label(label_frame,
		# 			   text='3. We can add multiple\n    widgets in it.')
		#
		# label3.place(x=0, y=65)
		# self.labelBottom = tk.Label(self,height=100,width=150)
		# self.labelBottom.grid(row=2,column=0)

		# self.entryMsg = tk.Entry(self.labelBottom,
		# 					  bg="#2C3E50",
		# 					  fg="#EAECEE",
		# 					  font="Helvetica 13")
		#
		# # place the given widget
		# # into the gui window
		# self.entryMsg.place(relwidth=0.74,
		# 					relheight=0.06,
		# 					rely=0.008,
		# 					relx=0.011)

		# self.entryMsg.focus()


if __name__ == "__main__":

	root = tk.Tk()
	app = Application(master=root)
	canvas = app.createCanvas(700, 450)
	canvas = app.addImage(canvas,"images//backgroundimg.png", 0, 0)
	canvas.pack()
	app.mainloop()
