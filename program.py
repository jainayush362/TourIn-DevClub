import pyttsx3  # text to speech library
import speech_recognition as sr  # Convert speech to text
import pyaudio
import datetime
import requests
import sys
import json #to handle json compatability
from amadeus import Client, ResponseError #AMADEUS DEVELOPER API
from  geopy.geocoders import Nominatim #GeoPy and Nominatim to retrieve lat & long of city
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

def visit_india():
    send_url = "http://api.ipstack.com/check?access_key=0fbd1f7d2671232974fce0727cea581a" #IPStack API
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    origincity = geo_json['city']
    origincountry = geo_json['country_name']
    destinationcountry="india"
    wb.open_new("https://www.google.co.in/maps/dir/"+origincity+", +"+origincountry+"/"+destinationcountry+"/") #Search Filtering Technique using Google as example
    speak("Here on the map you can find out the time and preffered mode of commute for your journey.")


def about_india():
    speak("India, officially the Republic of India, is a country in South Asia. It is the second-most populous country, the seventh-largest country by land area, and the most populous democracy in the world. One of the oldest civilisations in the world, India is a mosaic of multicultural experiences. With a rich heritage and myriad attractions, the country is among the most popular tourist destinations in the world. Shri Ram Nath Kovind is the President of India and Shri Narendra Damodar Das Modi is the present Prime Minister of India.")
    print("Results : India, officially the Republic of India, is a country in South Asia. It is the second-most populous country, the seventh-largest country by land area, and the most populous democracy in the world. One of the oldest civilisations in the world, India is a mosaic of multicultural experiences. With a rich heritage and myriad attractions, the country is among the most popular tourist destinations in the world. Shri Ram Nath Kovind is the President of India and Shri Narendra Damodar Das Modi is the present Prime Minister of India.")


def points_of_attr():
    speak("Just tell me the name of Indian city,village,town,state or district in which you want to see points of attraction.")
    place = userquery().lower()
    wb.open_new("https://www.google.com/search?sclient=psy-ab&site=&source=hp&btnG=Search&q="+place+"+point+of+interest") #Search filtering technique using Google as example


def itenary():
    wb.open_new("https://www.makemytrip.com/")

def airports():
    wb.open_new("https://www.aai.aero/en/content/how-many-international-airports-are-india-and-which-are-they")
    speak("The given are the official international airpotrs in india till date as per airports authority of india.")


def visa():
    speak("Official details related to registeration of Visa is available on the official website of Indian Govenrnment that is indianvisaonline.gov.in. You should not trust any other source or application.")
    wb.open_new("https://indianvisaonline.gov.in/")
    print("Results : Official details related to registeration of Visa is available on the official website of Indian Govenrnment that is indianvisaonline.gov.in. You should not trust any other source or application.")

def activity():
    speak("Please tell the City for which you want to explore the activities?")
    placename = userquery().lower()
    geolocator = Nominatim(user_agent="jainayush362@gmail.com")
    city = placename
    country ="India"
    loca = geolocator.geocode(city+','+ country)

    amadeus = Client(client_id='Aq3qAwphK1SyDHjYnlABOc12OO2AHG82',client_secret='6h5fmOnNwCSSHfAd')
    try:
        response = amadeus.shopping.activities.get(latitude=loca.latitude, longitude=loca.longitude)
        speak("Following are the Activities for given location"+placename)
        tkinter.messagebox.showinfo('Result for Query',response.data)
        print(response.data)
    except ResponseError as error:
        print(error)

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
        

if __name__ == '__main__':
    wishme()
    query = userquery().lower() #storing all commands in lower case for easy recognition
    if 'climate' in query or 'season' in query or 'weather' in query or 'forecast' in query:
        climate()
    elif 'why to visit india' in query or 'about india' in query or 'why should i visit india' in query or 'information on india' in query or 'what is india' in query:
        about_india()
    elif 'visa' in query:
        visa()
    elif 'airport' in query or 'airports' in query:
        airports()
    elif 'point of attraction' in query or 'points of attraction' in query or 'tourist attractions' in query or "tourist spots" in query or "monuments" in query or "attraction spots" in query or 'places of interests' in query:
        points_of_attr()
    elif 'itinerary' in query or 'booking' in query:
        itenary()
    elif 'how far india' in query or 'distance to india' in query or "how to reach india" in query:
        visit_india()
    elif 'activities' in query or 'activity' in query:
        activity()
    elif 'states' in query or 'places to visit' in query or 'places i should' in query or 'places should i' in query or 'must visit places' in query or 'tourist destinations' in query or 'which places' in query:
        places_data()
    elif 'distance' in query:
        distance_calc()
    elif 'duration' in query:
        duration_calc()
    else:
        speak("I don't have much information on this. Please try something else.")
