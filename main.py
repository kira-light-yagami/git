import PyPDF2
import os
import sys
from AppOpener import open, close, mklist, give_appnames
from AppOpener import close as close1
import webbrowser
import pywhatkit

#************************************
from AppOpener import open as open1
from AppOpener import open as open2
from AppOpener import open as open3
from AppOpener import open as open4
from AppOpener import open as open5
from AppOpener import open as open6
from AppOpener import open as open7
from AppOpener import open as open8
from AppOpener import open as open9
from AppOpener import open as open10
from AppOpener import open as open11
from AppOpener import open as open12
from AppOpener import open as open13
#import os
#import wikipedia
import pyttsx3
import speech_recognition as sr
import datetime
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voices', voices [0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=3)

    try:
        print('recognizing....')
        query = r.recognize_google(audio,language='en-in')
        print(f'user said [{query}]')

    except Exception as e:
        speak("can you please say that again")
        return 'none'
    return query

def pdf_reader():
    book = open ('py3.pdf','rb')
    pdfreader=PyPDF2.PdfReader(book)
    pages = pdfreader.numPages
    speak(f"total no of pages in this pdf {pages}")
    speak("please enter the page no you want to read")
    pg=int(input("please enter the page no"))
    page = pdfreader.getPage(pg)
    text = page.extractText()
    speak(text)
def wish () :
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        print("good morning sir how are you feeling")
        speak("good morning sir how are you feeling")
    elif hour > 12 and hour < 18:
        speak("good afternoon master ji")
        speak("how may i help you master saksham ")
        print("how may i help you master saksham ")
        print("good afternoon master ji")
    else:
        speak("good evening master Saksham ")
        speak("sir how may i help you ")
        print("good evening master Saksham ")
        print("sir how may i help you ")



if __name__ == "__main__":
    #speak("hello master ji")
        wish()
        #while True:
        if 1:
            query = takecommand().lower()

            if 'open tips ' in  query:
                open("Tips")  # Opens whatsapp
                #path = "C:\\Users\\ARTI KATARIA\\Desktop\\jarvis.txt"
                #os.startfile(path)

            elif "open notepad" in query:
                open1("Notepad")
                print("as you commended sir ")


            elif "check my network speed" in query:
                webbrowser.open("https://www.speedtest.net/")
                speak("yes sir just press go")
                speak("opening okla speed test ")
                speak("checking your network it mite take few seconds sir                     ")
                speak("checking")
                speak("checking....")
                speak("checking....")
                speak("calculating speed")
                speak("calculating speed")
                speak("almost there")
                speak("gathering information for you sir ")
                speak("checking your networks  download speed")
                speak("checking..")
                speak("checking")

                speak("calculating")

                speak("gathering information for you sir ")
                speak("Checking your networks upload speed")
                speak("checking..")

                speak("almost their sir")
                speak("gathering information for you sir ")
                speak("network speed calculated sir ")
                speak("network speed as usual as on other day ")
                speak("result on your screen sir ")

                print("Yes sir just press go")
                print("Checking your network it mite take few seconds sir)                    ")
                print("Checking your networks upload and download speed")

            elif "open mail" in query:
                open2("Mail")
                speak("done sir")


            elif "read pdf" in query:
                pdf_reader()



            elif "open setting" in query:
                open3("Settings")

            elif "open calculator" in query:
                open4("Calculator")
                speak("look like some tough question master Saksham")
                print("look like some tough question master Saksham")

            #elif "check for massages " or "massages" or "show me massages "in query:
             #   open8("discord")
              #  open6("whatsapp")
               # speak("checking for massage sir please wait ")
                ##rint("checking for massage sir please wait ")
                #print("there you go sir your chatting applications are open ")

            elif "close discord" in query:
                close1("Discord", match_closest=True)

            elif "open discord" in query:
                open5("Discord")
                speak("sure sir but your friends might not be online sir if you insist i weill surly check it for you" )
                print("sure sir but your friends might not be online sir if you insist i weill surly check it for you" or "sure sir but your friends might not be online sir but master saksham to make sure i will check it ")

            elif "i want to play some game" in query:
                open13("riot clint" or "tlauncher")
                speak("sure sir. but please dont play too long ")

            elif "open valorant" in query:
                open7("riot clint")
                speak("sure sir. but please dont play too long ")

            elif "open netflix" in query:
                open9("netflix")
                speak("ready to chill with netflix sir")

            elif "open whatsapp" in query:
                open10("whatsapp")
                speak("as you wish sir ")
                print("As you wish sir ")

            elif "spotify " in query:
                open11("spotify", match_closest=True)
                speak("ok sir opening spotify for music")
                print("Ok sir ")

            elif "minecraft" in query:
                open6("Tlauncher")

            elif "i want to see system files" in query:
                open12("File explorer")
                speak("here are system files master saksham")
                print("Here are system files master saksham")

            elif "open youtube" in query:
                webbrowser.open("youtube.com")
                speak("here is youtube sir as you commanded")
                print("Here is youtube sir as you commanded")

            #elif "close youtube" in query:
               # webbrowser.open("youtube.com")
              #  speak("here is youtube sir as you commanded")
              #  print("Here is youtube sir as you commanded")

            elif "cartoon " in query:
                webbrowser.open("https://sanji.to/")
                speak("there you go master saksham now please enjoy")
                print("There you go master saksham now please enjoy")

            else:
                speak("sorry sir but i am not sure if i understand that please say that again  ")
                print("sorry sir but i am not sure if i understand that")


speak("Is there anything else to help you with sir ill be happy to know ")
print("Is there anything else to help you with sir ill be happy to know ")





