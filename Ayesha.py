
import pyttsx3
import speech_recognition as sr
import instaloader
import smtplib
import cv2
import datetime
import pyautogui
import wolframalpha
import json
import webbrowser
import wikipedia
import os
import pyjokes
import time
import requests
import pywhatkit as kit
from requests import get
from PIL import Image
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from PIL import Image
import time
from instabot import Bot
import qrcode
import random

#engine voices
engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
test = [1,2]
engine.setProperty('voice',voices[random.choice(test)].id)

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
        print(f"Sir said :{query}")

    except Exception as e:
        speak("unable to recognise your voice . please say it again")
        print("Unable to recognise your voice.please say it again ")
        return  "None"
    return  query

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
        speak("Good Morning sir Did you eat breakfast?")
        print("Good Morning sir Did you eat breakfast?")

    elif hour>=12 and hour < 18:
        speak("Good Afternoon sir did you eat lunch?")
        print("Good Afternoon sir did you eat lunch?")
    else:
        speak("Good evening sir did you eat dinner ?")
        print("Good evening sir did you eat dinner? ")

    assname = ("I am ayesha , Yadav Assistant")
    speak(assname)
    print(assname)
    speak("what work do you want from me")
    print("what work do you want from me")

#other people intro
def usrname():
    speak("What is your name")
    print("what is your name")
    uname = takeCommand()
    if "Deepak Yadav" in uname:
        speak("you are my Boss")
        print("you are my Boss")
        speak("Welcome Deepak Yadav")
        print("Welcome Deepak Yadav")
    else:
        speak("Welcome Mister")
        print("Welcome Mister")
        speak(uname)
        speak("How can i help you sir")
        print("How can i  help you sir")

#Main Function
if __name__ == '__main__':
 wishMe()
 # usrname()
while True:
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
          speak("searching wikipedia")
          print("searching wikipedia")
          query = query.replace("wikipedia","")
          results =  wikipedia.summary(query,sentences = 3)
          speak("according to wikipedia")
          print(results)
          speak(results)

        elif 'open youtube' in query:
          speak("here you go to youtube ")
          webbrowser.open_new_tab("www.youtube.com")
          time.sleep(10)

        elif 'open google' in query:
          speak("here you go to google ")
          webbrowser.open_new_tab("www.google.com")
          time.sleep(10)

        elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"sir,the time is{strTime}")
           print(f"sir,the time is {strTime}")

        elif 'which day' in query:
            day = datetime.datetime.today().weekday()+1
            time.sleep(2)
            Day_dict = {1: 'Monday', 2: 'Tuesday',
                        3: 'Wednesday', 4: 'Thursday',
                        5: 'Friday', 6: 'Saturday',
                        7: 'Sunday'}

            if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
                speak("The day is " + day_of_the_week)

        elif 'email to sameer' in query:
           try:
            speak("what should i say?")
            print("what should i say")
            content = takeCommand()
            to = "sam5@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent")

           except Exception as e:
            print(e)
            speak("i am not able to send email")

        elif 'how are you' in query:
             speak("i am fine, Thank you!")
             print("i am fine thank you!")


        elif 'exit' in query or'no thanks'in query or 'quit ' in query:
             speak("thank for using me :) ")
             exit()

        elif 'send multimedia mail' in query:
            speak("What is the subject of mail?")
            print("What is the subject of mail?")
            io = takeCommand()
            print("what is the body of mail")
            speak("what is the body of mail")
            h=  takeCommand()
            from_address = "dhgh0@gmail.com"
            to_address = "onlijjjn4545@gmail.com"
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            msg['Subject'] = io
            body = h
            msg.attach(MIMEText(body, 'plain'))
            #filename here
            filename = "elwal/content1"
            attachment = open(
                #enter complete link
                r"C:\Useelwal\content1",
                "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment;filename = %s" % filename)
            msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(from_address, "pasword")
            text = msg.as_string()
            s.sendmail(from_address, to_address, text)
            s.quit()
            print("mail sent suceesfully!")
            speak("mail sent suceesfully!")

        elif'joke' in query:
             speak(pyjokes.get_joke())

        elif 'calculate' in query:
             speak("running....")
             print("running....")
             #enter your api id
             app_id = "take it for your from "
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
             kit.sendwhatmsg("+918854585411", " message ", 17, 30)
             time.sleep(10)
             speak("message sent successfully")
             print("messsgae sent succesfully")


        elif "play song on youtube" in query:
            speak("tell me song name")
            print("tell me song name")
            h = takeCommand()
            speak("playing..")
            kit.playonyt(h)

        elif 'is love' in query:
          speak(" probably yes hmmm ")
          print("probably yes hmm")

        elif 'do not listen' in query:
          speak("for how much time ")
          print("for how much ")
          a= int(takeCommand())
          time.sleep(a)
          print(a)

        elif 'where is ' in query:
          query = query.replace("where is "," ")
          location = query
          speak("You asked to locate")
          print("you asked to locate")
          speak(location)
          time.sleep(10)
#not loading ERRROR
          webbrowser.open("https://www.google.nl / maps / place/"+location + " ")

        elif 'write a note' in query:
            speak("what should i write")
            note = takeCommand()
            file= open('ayesha.txt','w')
            speak("sir,Should i include date and time")
            snfm =  takeCommand()
            if 'yes' in snfm or 'sure'  in snfm:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
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
           speak("What i should convert?")
           print(("What is hould convert?"))
           h = takeCommand()
           print(h)
           kit.text_to_handwriting(h, rgb=[0, 0, 0])

        elif "open command promot" in query:
            speak("opening..")
            print("opening..")
            os.system("start cmd")

# ERROR : camera not taking picture
        elif "open camera" in query or 'launch camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                  break;
                  cap.release()
            cv2.destroyAllWindow()

        elif "my ip address" in query:
           ip = get('https://api.ipify.org').text
           speak(f"your IP address is{ip}")
           print(f"your IP address is{ip}")

        elif 'download instagram profile photo' in query:
            speak("honey, please give few second to download")
            print("honey, please give few second to download")
            mod = instaloader.Instaloader()

            f = mod.download_profile("userhandle", profile_pic_only=True)
            speak("Downloaded Sucessfully")
            print("downloaded Sucessfully")

  ##have to write something
        elif 'upload picture on instagram' in query:
            bot = Bot()
            speak("what caption i should write on picture")
            print("what caption i should write on picture")
            w = takeCommand()
            bot.login(username="enter your username",
                      password="enter your password")
            bot.upload_photo(
                #link to the file
                r"C:\User.pg",
                caption=w)
            speak("Photo uploaded successfully!")
            print("Photo uploaded successfully!")
            time.sleep(10)

        elif "open  movies" in query:
            speak("opening sir")
            print("opening sir")
            webbrowser.open_new_tab("www.movies.com")

        elif "ayesha" in query:
           wishMe()
           speak("I am ayesha , Deepak assistant")
           print("I am ayesha , Deepak assistant")

        elif 'revenge' in query or 'open blaster' in query:
            speak("who trouble you  ? ..give me chance i will  see  them")
            print("who trouble you  ? ..give me chance i will  see  them")
            num  ="enter your number"
            print("sir tell me your stress level in low and high terms ")
            speak("sir tell me your stress level in low and high terms")
            gh = takeCommand()
            if 'low' in gh:
                frequency  = 10
            elif 'high' in gh :
                frequency = 20
            else :
                 frequency  = 15
            #flipkart
            browser =webdriver.Chrome(ChromeDriverManager().install())
            mobile_number = num
            for i in range(frequency):
              browser.get('https://www.flipkart.com/account/login?ret =/')
              number = browser.find_element_by_class_name('_2IX_2-')
              number.send_keys(mobile_number)
              forgot = browser.find_element_by_link_text('Forgot?')
              forgot.click()
              time.sleep(10)
            browser.quit()
            print("still workin on...")
            speak("still working on...")
            for i in range(frequency):
                driver = webdriver.Chrome()
                driver.get(
                    "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Ffrom%3Dhz%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

                driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys(num)
                driver.find_element_by_xpath('//*[@id="continue"]').click()
                driver.find_element_by_xpath('//*[@id="auth-fpp-link-bottom"]').click()
                driver.find_element_by_xpath('//*[@id="continue"]').click()
                time.sleep(5)

            driver.close()
            print("Now i think revenge taken off. ..  please drink water Sir")
            speak("Now i think revenge taken off. ..  please drink water Sir")

        elif "weather" in query:
            api_key = "Enter Your api key"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("tell me city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"]!= "404":

              y = x["main"]
              current_temperature  = y["temp"]
              current_pressure = y["pressure"]
              current_humididty = y["humidity"]
              z = x["weather"]
              weather_description = z[0]["description"]

              print("Temperature (in kelvin unit) = " +str(current_temperature)+ "\n atmospheric pressure (in hPa unit) = "+str(current_pressure) +"\n humidity (in percentage) = "+str(current_humididty) +"\n description = " +str(weather_description))
              speak("Temperature (in kelvin unit) is "+str(current_temperature)+ "\n atmospheric pressure (in hPa unit) is "+str(current_pressure) +"\n humidity (in percentage) is "+str(current_humididty) +"\n description is " +str(weather_description))

            else:
              speak("City Not Found")
              print("City Not Found")



        elif"wikipedia" in query:
           speak("opening")
           webbrowser.open("www.wikipedia.com")

        elif  "what is" in query :
            speak("running ...")
            print("running...")
            client = wolframalpha.Client("PAss here app id ")
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)

            except StopIteration:
                print("No results")
                speak("no results")

        elif "volume up" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "volume mute" in query or "mute" in query:
            pyautogui.press("volumemute")

        elif "set alarm" in query:
            speak("Tell me time in this manner set alarm to 5:30 am")
            print ("Tell me time in this manner set alarm to 5:30 am")
            q  = takeCommand();
            q = q.replace("set alarm to","")
            time.sleep(10)
            q = q.replace(".","")
            time.sleep(10)
            q= q.upper()
            time.sleep(2)
            import Alarm
            Alarm.Alaram(q)



        elif "screenshot" in query or"take screenshot" in query:
            speak("capturing...")
            print("capturing...")
            screenshot = pyautogui.screenshot()
            screenshot.save("swh.png")
            try:
                image = Image.open("swh.png")
                image.show()
            except :
             time.sleep(5)

        elif "who is " in query:
            try:
               speak("running ...")
               print("running...")
               client = wolframalpha.Client(" enter your App id")
               res = client.query(query)
               print(next(res.results).text)
               speak(next(res.results).text)
            except :
              query = query.split(' ')
              query = " ".join(query[0:])
              speak("I am searching for " + query)
              print(wikipedia.summary(query, sentences=3))
              speak(wikipedia.summary(query,
                                          sentences=3))


        elif 'send a text message' in query:
            speak("to whom?")
            print("to whom?")
            loe = "enter recvier no"
            print(loe)
            speak("what should i say")
            print("what should i say")
            com = takeCommand()
            print(com)

            url = "https://www.fast2sms.com/dev/bulk"
            my_data = {
                # Your default Sender ID
                'sender_id': 'FSTSMS',

                # Put your message here!
                'message': com,

                'language': 'english',
                'route': 'p',

                # You can send sms to multiple numbers
                # separated by comma.
                'numbers': loe
            }
            headers = {
                'authorization': 'Enter Your own id getting from post registration',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
            response = requests.request("POST",
                                        url,
                                        data=my_data,
                                        headers=headers)

            # load json data from source
            returned_msg = json.loads(response.text)

            # print the send message
            print(returned_msg['message'])
            speak("Sms Sent Sucessfully")

        elif 'upload picture on instagram' in query:
            print("Since i had picture path.so, i am uploading this..")
            speak("Since i had picture path.so, i am uploading this..")
            print("What should i write the caption of this picture")
            speak("What should i write the caption of this picture")
            gi  = takeCommand()
            print(qi)
            bot = Bot()
            bot.login(username="ENter your usernmae",
                      password="enter password")
            bot.upload_photo(
                r"C:\Uprofile_pic.jpg",
                caption=qi)
            print("picture uploaded successfully sir")
            speak("picture uploaded successfully sir")

        elif 'open mobile camera' in query:
            import urllib.request
            import cv2
            import numpy as np
            import time
            Url= "here enter your own https link/shot.jpg"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(Url).read()),dtype=np.uint8)
                img=cv2.imdecode(img_arr,-1)
                cv2.imshow("IPWebcam",img)
                q =cv2.waitKey(1)
                if q==ord("q"):
                    break;

            cv2.destroyAllWindows()

        elif 'check network speed' in query:
            import speedtest
            st = speedtest.Speedtest()
            d1 =st.download()
            up=st.upload()
            print(f"sir upload speed is {up} bit per second and download speed is{d1} bit per second")
            speak(f"sir upload speed is {up} bit per second and download speed is{d1} bit per second")

        elif 'check battery' in query:
            import psutil
            battery = psutil.sensors_battery()
            per = battery.percent
            print(f"sir our system have {per} percent battery")
            speak(f"sir our system have {per}  percent battery")

        elif 'encrypt'in query or 'change to qr' in query:
            print("what message you want to convert in qr..please tell me Sir")
            speak("what message you want to convert in qr..please tell me sir")
            qe = takeCommand()
            data = qe
            qr = qrcode.QRCode(version=1,
                               box_size=10,
                               border=5,

                               )
            qr.add_data(data)
            # Encoding data using make() function
            qr.make(fit=True)
            img = qr.make_image(fill_color="black",
                                back_color="white"
                                )

            # Saving as an image file
            img.save('deep.png')
            im = Image.open("deep.png")
            im.show()

    speak("do you have any other work ?")
    print("do you have other work ?")