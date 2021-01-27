import pyttsx3
import speech_recognition as sr
import smtplib
import secure_smtplib
import datetime
import subprocess
import wolframalpha
import tkinter
import json
import cv2
import random
import operator
import webbrowser
import wikipedia
import os
import winshell
import pyjokes
import feedparser
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import pywhatkit as kit
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from ayeshaUI import Ui_MainWindow











#engine voices
engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#take command function
def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold =490
        audio  = r.listen(source)
    try:
        print("Recognizing...")
        query  = r.recognize_google(audio,language = 'en-in')
        print(f"baby said :{query}")

    except Exception as e:
        print(e)
        speak("unable to recognise your voice . please say it again")
        print("Unanable to recognise your voice.please say it again ")
        return  "None"
    return  query


# class MainThread(QThread):
#     def __init__(self):
#         super(MainThread,self).__init__()
#     def run(self):
#        #not completed

#mail send function
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email','password')
    server.sendmail('to',to,content)
    server.close()

#wishme function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning baby Did you eat breakfast")
        print("Good Morning baby Did you eat breakfast")

    elif hour>=12 and hour < 18:
        speak("Good Afternoon baby did you eat lunch")
        print("Good Afternoon baby did you eat lunch")


    else:
        speak("Good evening baby please take dinner")
        print("Good evening baby please take dinner")

    assname = ("I am ayesha ,Deepak girlfriend")
    speak(assname)
    print(assname)
    speak("what work do you want from me")
    print("what work do you want from me")
#other people intro
def usrname():
    speak("What is your name")
    print("what is your name")
    uname = takeCommand()
    if "deepak yadav" in uname:
        speak("you are my boyfriend")
        print("Welcome Deepak Yadav")
    else:
        speak("Welcome Mister")
        speak(uname)
        columns = shutil.get_terminal_size().columns
        print("###########".center(columns))
        print("Welcome Mr.",uname.center(columns))
        print("#############".center(columns))
        speak("How can i help you sir")
        print("How can i  help you sir")


#Main Function
if __name__ == '__main__':
 wishMe()
 #usrname()
while True:
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
          speak("searching wikipedia")
          print("searching wikipedia")
          query = query.replace("wikipedia"," ")
          results =  wikipedia.summary(query,sentences=3)
          speak("according to wikipedia")
          print(results)
          speak(results)
        elif 'open youtube' in query:
          speak("here you go to youtube baby")
          webbrowser.open_new_tab("www.youtube.com")
        elif 'open google' in query:
          speak("here you go to google baby")
          webbrowser.open_new_tab("www.google.com")
        elif 'play music' or 'music' in query:
           speak("playing music baby")
           music = "C:\\Users\\USER\\Music"
           songs = os.listdir(music)
           print(songs)
           for song in songs:
               if song.endswith('.mp3'):
                  random=os.startfile(os.path.join(music,songs[2]))
        
                    
        elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("% H: % M:% S")
           speak(f"baby,the time is{strTime}")
           print(f"baby,the time is{strTime}")
        elif 'email to sameer' in query:
           try:
            speak("what should i say?")
            print("what should i say")
            content = takeCommand()
            to = "samirtiwari2308@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent")
           except Exception as e:
            print(e)
            speak("i am not able to send email")
        elif 'how are you' in query:
             speak("i am fine, Thank you!")
             print("i am fine thank you!")
             speak("how are you baby?")
             print("how are you baby?")

        elif 'fine ' in query or 'good ' in query:
             speak("It is  good to know that you are fine baby uuuhhhh")
        elif 'change name' in query:
             speak("what would you like to call me,baby")
             assname  = takeCommand()
             speak("thanks for giving me new name")
             print("thanks for giving me new name")
        elif 'exit' in query:
             speak("thank for using me baby ")
             exit()
        elif'joke' in query:
             speak(pyjokes.get_joke())
        elif 'calculate' in query:
             speak("running....")
             print("running....")
             app_id = " RA7R6J-Y575PX8KV7"
             client  = wolframalpha.Client(app_id)
             indx = query.lower().split().index('calculate')
             query = query.split()[indx + 1:]
             res = client.query(' '.join(query))
             answer= next(res.results).text
             print("The answer is "+answer)
             speak("The answer is "+answer)
        elif 'search for' in query or 'play ' in query:
             query = query.replace("search"," ")
             query = query.replace("play ", " ")
             webbrowser.open(query)

        elif "send whatsapp message" in query:
             kit.sendwhatmsg("+919306008049", "i am  ayesha deepak's girlfriend", 11, 40)
             print("messsgae sent succesfully")


        elif "play song on youtube" in query:
             speak("playing..")
             kit.playonyt("52 gaj ka dhaman")

        elif 'is love' in query:
          speak("that is i had for you")
          print("that is i had for you")
        elif 'do not listen' in query:
          speak("for how much time you want to stop ayesha from listening commands")
          print("for how much time you want to stop ayesha from listening commands")
          a= int(takeCommand())
          time.sleep(a)
          print(a)
        elif 'where is ' in query:
          query = query.replace("where is "," ")
          location = query
          speak("You asked to locate")
          print("you asked to locate")
          speak(location)
          webbrowser.open("https://www.google.nl / maps / place/"+location + " ")
        elif 'write a note' in query:
            speak("what should i write")
            note = takeCommand()
            file= open('ayesha.txt','w')
            speak("Baby,Should i include date and time")
            snfm =  takeCommand()
            if 'yes' in snfm or 'sure'  in snfm:
             strTime = datetime.datetime.now().strftime("% H: % M: % S")
             file.write(strTime)
             file.write(" :- ")
             file.write(note)
            else:
             file.write(note)
        elif "show note" in query:
          speak("showing notes")
          print("showing notes")
          file  = open("ayesha.txt","r")
          print(file.read())
          speak(file.read(6))
        elif "open notepad" in query:
          npath = "C:\\Windows\\system32\\notepad.exe"
          os.startfile(npath)
        elif "handwritten" in query:
           speak("running")
           kit.text_to_handwriting("hello i am ayesha ,deepak's girlfriend", rgb=[0, 0, 0])
        elif "open command promot" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                  break;
                  cap.release()
                  cv2.destroyAllWindow()

        # elif "my ip address" in query:
        #    ip = get('https://api.ipify.org').text
        #    speak(f"your IP address is{ip}")
        #    print(f"your IP address is{ip}")

        elif "ayesha" in query:
           wishMe()
           speak("I am ayesha Deepak's girlfriend")
           print("I am ayesha Deepak's girlfriend")
        elif "weather" in query:
           api_key = "db66791161b11fee77a038c0032175d1"
           base_url = "https://api.openweathermap.org/data/2.5/weather?"
           speak("what is city name ?")
           print("city name : ")
           city_name  = takeCommand()
           complete_url = base_url + "appid =" + api_key + "&q = " +city_name
           response = requests.get(complete_url)
           x= response.json()
           if x["cod"] != "404":
              y = x["main"]
              current_temperature  = y["temp"]
              current_pressure = y["pressure"]
              current_humididty = y["humidity"]
              z = x["weather"]
              weather_description = z[0]["description"]
              print("Temperature (in kelvin unit) = " +str(current_temperature)+ "\n atmospheric pressure (in hPa unit) = "+str(current_pressure) +"\n humidity (in percentage) = "+str(current_humididty) +"\n description = " +str(weather_description))
           else:
              speak("City Not Found")
              print("City Not Found")
        elif "send a message " in query:
            account_sid  = 'ACc5c41fab2e03ba29f36c6ab155adbe68'
            auth_token = '0497669be6a5159c8c6bffca9e1efa03'
            client = Client(account_sid,auth_token)
            message   = client.messages\
                          .create(
                              body= takeCommand(),
                              from_= '9306008049',
                              to = '9817551740',
                            )
            print(message.sid)
        elif"wikipedia" in query:
           speak("opening")
           webbrowser.open("www.wikipedia.com")
        elif  " will be my gf" in query:
           speak("Sorry i only committed for deepak")
           print("Sorry i only committed for deepak")
        elif  "what is" in query :
            speak("running ...")
            print("running...")
            client = wolframalpha.Client("RA7R6J-Y575PX8KV7")
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)

            except StopIteration:
                print("No results")
                speak("no results")
        elif "who is " in query:
          speak("running ...")
          print("running...")
          client = wolframalpha.Client("RA7R6J-Y575PX8KV7")
          res = client.query(query)

          try:
            print(next(res.results).text)
            speak(next(res.results).text)
          except StopIteration:
            print("No results")
            speak("no results")

speak("do you have any other work baby")
print("do you have other work baby")