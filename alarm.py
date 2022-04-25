from dis import Instruction
import os
from distutils import command
import time
import winsound
import pyttsx3
from os import system, name
import speech_recognition as sr
from datetime import date
# import sleep to show output for some time period
from time import sleep
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



def listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        command = r.recognize_google(audio , language="en-in")
        print(f"you said : {command}")

    except:
        return ""

    command = str(command)
    return command.lower()

engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 160)     # setting up new voice rate
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) #1 for female and 0 for male

def talk(text):
    engine.say(text)
    engine.runAndWait()




talk("tell me the hour")
hour = int(listen())

talk("tell me the minute")
min = int(listen())

talk("tell me the second")
sec = int(listen())
print("log updated")

#this is for log file :-
# Month abbreviation, day and year	

today = date.today()
d = today.strftime("%b-%d-%Y")
# if you want to print today's date : print("d4 =", d4)
f = open("d:\\nikhil python\\alarm_log\\alarms.txt","w")
f.write(str(hour))
f.write(":")
f.write(str(min))
f.write(":")
f.write(str(sec))
f.write("\n")
f.write(d)
f.write("\n")

f.close()


while(True):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    #if (time.strftime("%H") == 20) :
        #print("hello")
    #p = time.strftime("%H")
    sleep(1)
    if int(time.strftime("%H")) == hour and  int(time.strftime("%M")) == min and int(time.strftime("%S")) == sec:
        winsound.Beep(2000 , 5000)
    clear()




'''while(1):
    if int(time.strftime("%H")) == hour and  int(time.strftime("%M")) == min and int(time.strftime("%S")) == sec:
        winsound.Beep(2000 , 5000)'''
      
