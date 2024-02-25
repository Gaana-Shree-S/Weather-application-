from configparser import ConfigParser  
from tkinter import *
from tkinter import messagebox 

# extracting key from online apk to obtain weather updates
config_file = "config.ini"
config = ConfigParser() 
config.read(config_file) 
api_key = "3c91f2ad78ccc17451c13dd68f107148" 
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'



def getweather(city): 
	result = requests.get(url.format(city, api_key)) 
	
	if result: 
		sample = result.json() 
		city = sample['name'] 
		country = sample['sys'] 
		temp_kelvin = sample['main']['temp'] 
		temp_celsius = temp_kelvin-273.15
		weather_second = sample['weather'][0]['main'] 
		final = [city, country, temp_kelvin, 
				temp_celsius, weather_second] 
		return final 
	else: 
		print("NO Content Found") 


def search(): 
	city_name = city_text.get() 
	weather = getweather(city) 
	if weather: 
		location_label['text'] = '{} ,{}'.format(weather[0], weather[1]) 
		temperature_label['text'] = str(weather[3])+" Degree Celsius"
		weather_label['text'] = weather[4] 
	else: 
		messagebox.showerror('Error', "Cannot find {}".format(city)) 


#Outlook of application
app = Tk() 
app.title("Weather App") 
app.geometry("300x300") 

city_text = StringVar() 
entry = Entry(app, textvariable=city_text) 
entry.pack() 
Search_button = Button(app, text="Search Weather", width=12, command=search) 
Search_button.pack() 
location_label = Label(app, text="Location", font={'bold', 20}) 
location_label.pack() 
temperature_label = Label(app, text="") 
temperature_label.pack() 
weather_label = Label(app, text="") 
weather_label.pack() 
app.mainloop() 
