from tkinter import * # import all the tkinter modules
import tkinter as tk #GUI
from geopy.geocoders import Nominatim # module to convert an address into latitude and longitude values
from tkinter import ttk,messagebox # message box desing
from timezonefinder import TimezoneFinder   #find timezone from given coordinates
from datetime import datetime
import requests
import pytz # for timezone

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():

        try:
                city=textfield.get() # get the city name from textfield

                geolocator=Nominatim(user_agent="geoapiExercises") # create an object
                location= geolocator.geocode(city) # get the location of the city
                obj = TimezoneFinder() # create an object
                result = obj.timezone_at(lng=location.longitude,lat=location.latitude) # get the timezone of the city

                home=pytz.timezone(result) # get the timezone of the city
                local_time=datetime.now(home) # get the local time of the city
                current_time=local_time.strftime("%I:%M %p") # get the current time of the city
                clock.config(text=current_time) # set the current time of the city
                name.config(text="CURRENT WEATHER") # set the name of the city


                #weather
                api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f1d23cbb14220b547f615d1afd906e88" # get the weather of the city from API

                json_data = requests.get(api).json() # get the weather of the city from API
                condition = json_data['weather'][0]['main'] # get the weather condition of the city
                description = json_data['weather'][0]['description'] # get the weather description of the city
                temp = int(json_data['main']['temp']-273.15) # get the temperature of the city
                pressure = json_data['main']['pressure'] # get the pressure of the city
                humidity = json_data['main']['humidity'] # get the humidity of the city
                wind = json_data['wind']['speed'] # get the wind speed of the city


                t.config(text=(temp,"°")) # set the temperature of the city
                c.config(text=(condition,"|","FEELS","LIKE",temp,"°")) # set the weather condition of the city


                w.config(text=wind) # set the wind speed of the city
                h.config(text=humidity) # set the humidity of the city
                d.config(text=description) # set the weather description of the city
                p.config(text=pressure) # set the pressure of the city  



        except Exception as e: # if the city name is not found
                messagebox.showerror("Weather App","Invalid Entry!!")     


#template for weather app 
#search box
Search_image=PhotoImage(file=r"C:\weather\search.png") # search image
myimage=Label(image=Search_image) 
myimage.place(x=20,y=20) 

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white") # textfield
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file=r"C:\weather\search_icon.png") # search icon
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)
#logo
Logo_image=PhotoImage(file=r"C:\weather\logo.png") # logo image
logo=Label(image=Logo_image)
logo.place(x=150,y=100)


#Bottom box
Frame_image=PhotoImage(file=r"C:\weather\box.png") # bottom box image
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold")) # name of the city
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20)) # current time of the city
clock.place(x=30,y=130)



#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef") # wind label
label1.place(x=120,y=400)



label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef") # humidity label
label2.place(x=250,y=400)


label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef") # description label
label3.place(x=430,y=400)


label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef") # pressure label
label4.place(x=650,y=400)



t=Label(font=("arial",70,"bold"),fg="#ee666d") # temperature label
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef") # wind speed label
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef") # humidity label
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef") # description label
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")      # pressure label
p.place(x=670,y=430)


root.mainloop() # run the app