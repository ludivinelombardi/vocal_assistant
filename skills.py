import datetime
import random
import webbrowser
from datetime import date
import requests
from apikey import api_key
import pyowm
import subprocess
import psutil
import os

class Skills:
        
    def __init__(self):
        pass
    
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = "Il est actuellement {} heure {}".format(now.hour, now.minute)
        return answer
    
    @staticmethod
    def greeting():
        answer = ["bonjour, je suis connor, ton assistant virtuel", "bonjour, comment puis-je t'aider ?"]
        greetings = random.choice(answer)
        return greetings
    
    @staticmethod
    def health():
        answer = ["ça va pas trop mal, merci", "je vais bien", "tout vas bien pour moi"]
        health = random.choice(answer)
        return health
       
    @staticmethod
    def leaving():
        answer = ["au revoir, bisous bisous", "à bientôt", "j'espère avoir pu t'aider !"]
        leaving = random.choice(answer)
        return leaving
    
    @staticmethod
    def open_browser():
        safari = webbrowser.get("safari")
        open = safari.open_new("google.fr")
        return open
    
    @staticmethod
    def open_youtube():
        safari = webbrowser.get("safari")
        open = safari.open_new("youtube.com")
        return open
    
    @staticmethod
    def get_weather():
        owm = pyowm.OWM(api_key)
        mgr = owm.weather_manager()
        weather = mgr.weather_at_place('Lyon,fr').weather
        observation = mgr.weather_at_place('Lyon,fr')
        w = observation.weather
        temp = weather.temperature('celsius')
        tempe = temp['feels_like']
        wind = w.wind()
        speed = wind['speed']
        pol = owm.airpollution_manager()
        air_status = pol.air_quality_at_coords(45.764043, 4.835659)
        pol_index = air_status.aqi
        weather = "La température ressentie est de {} degré celsius, la vitesse du vent est de {} mètre par seconde, et l'index de qualité de l'air est de {}".format(tempe, speed, pol_index)
        return weather
    
    @staticmethod
    def no_answer():
        e = ["Je suis désolé, je n'ai pas compris", "Pardon ?", "Peux-tu répéter ?"]
        error = random.choice(e)
        return error
    
    @staticmethod
    def open_mail():
        mail = subprocess.Popen(["/bin/bash","-c","open /System/Applications/Mail.app"])
        return mail
    
    @staticmethod
    def open_calendar():
        calendar = subprocess.Popen(["/bin/bash","-c","open /System/Applications/Calendar.app"])
        return calendar
    
    @staticmethod
    def open_message():
        msg = subprocess.Popen(["/bin/bash","-c","open /System/Applications/Messages.app"])
        return msg
    
    @staticmethod
    def open_github():
        hub = subprocess.Popen(["/bin/bash","-c","open /Applications/GitKraken.app"])
        return hub
    
    @staticmethod
    def open_shell():
        hub = subprocess.Popen(["/bin/bash","-c","open /Applications/iTerm.app"])
        return hub
    
    @staticmethod
    def battery_info():
        battery_data = psutil.sensors_battery()
        answer = "Ta batterie est chargée à {} pourcent".format(battery_data.percent)
        return answer

            
    
    
   