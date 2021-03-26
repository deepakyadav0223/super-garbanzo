#importing required modules
from tkinter import *
import requests
from geopy.geocoders import Nominatim
import json
from tkinter import messagebox

# this function take city name and api_key and get a request on
#free openweatherApi and collect data
def tellWeather():

    api_key = "db66791161b11fee77a038c0032175d1"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city_field.get()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city_name)
# if cod is not equal to 404 means city is present
 #   and then did data scrapping
    if x["cod"] != "404":
        y = x['main']
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity= y["humidity"]
        z= x["weather"]
        wdescription = z[0]["description"]

        temp_field.insert(15,str(current_temperature)+" kelvin")
        press_field.insert(25,str(current_pressure)+" hPa")
        humi_field.insert(35,str(current_humidity)+ " %")
        desc_field.insert(25,str(wdescription))
        coun_field.insert(25,str(location))
        # pop up message if city is not Present
    else:
        messagebox.showerror("ERROR","City Not Found \n"
                             "Please Enter a Valid City Name")
        # delete the invalid city name and set focus on the city name again
        city_field.delete(0,END)
        city_field.focus_set()
#clear all the  prevoius data
def ClearAll():
    city_field.delete(0,END)
    temp_field.delete(0,END)
    humi_field.delete(0,END)
    press_field.delete(0,END)
    desc_field.delete(0,END)
    coun_field.delete(0,END)
    city_field.focus_set()
#main function

if __name__ == '__main__':
    root = Tk()
    root.title("GUI APPLICATION")
    root.config(bg='coral')
    root.geometry('450x380')
    headlabel = Label(root,text="Weather Finding Application",fg='Black',bg='cyan',font="Arial")
    # creating label for each
    label1 = Label(root,text="City Name :",fg='Black',bg='blue')
    label2 = Label(root, text="Temparature :", fg='Black', bg='blue')
    label3 = Label(root, text="Pressure :", fg='Black', bg='blue')
    label4 = Label(root, text="Humidity :", fg='Black', bg='blue')
    label5 = Label(root, text="Description :", fg='Black', bg='blue')
    label6 = Label(root,text = "Country : " ,fg='Black',bg='blue')
#placing each label
    headlabel.grid(row=0,column=1)
    label1.grid(row=2,column=0,sticky="E")
    label2.grid(row=4, column=0, sticky="E")
    label3.grid(row=5, column=0, sticky="E")
    label4.grid(row=6, column=0, sticky="E")
    label5.grid(row=7, column=0, sticky="E")
    label6.grid(row=8, column=0, sticky="E")
#creating entry field to write data on it
    city_field = Entry(root)
    temp_field = Entry(root)
    press_field = Entry(root)
    humi_field = Entry(root)
    desc_field = Entry(root)
    coun_field = Entry(root)
# placing entry field
    city_field.grid(row=2,column=1,ipadx="100")
    temp_field.grid(row=4,column=1,ipadx="100")
    press_field.grid(row=5,column=1,ipadx="100")
    humi_field.grid(row=6,column=1,ipadx="100")
    desc_field.grid(row=7,column=1,ipadx="100")
    coun_field.grid(row=8,column=1,ipadx="100")
#makin button for submit,clear and exit
    button1 =Button(root,text="Submit-Now",bg="green", fg="black",command=tellWeather)
    button2 = Button(root,text="Clear-All",bg="black", fg="red",command=ClearAll,width=10,height=1)
    button3  = Button(root,text="Close",bg="yellow",fg="red",command=root.quit,width=7)
#placing the buttons
    button1.grid(row=3,column=1)
    button2.grid(row=9,column=1)
    button3.grid(row=10,column=1)

#run the till user wish
    root.mainloop()
