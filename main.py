import pyttsx3
import speech_recognition as sr
from skills import Skills


class AI(): 
    
    def __init__(self):
        self.r = sr.Recognizer() #recognition 
        self.m = sr.Microphone() #micro
        self.engine = pyttsx3.init() #python text to speech v3 initialisation

    def listen(self):
        query = ""
    
        with self.m as source: 
            print("Dis quelque chose")
            self.r.pause_threshold = 1
            audio = self.r.listen(source,0,2)  
            self.r.adjust_for_ambient_noise(source) #ecouter au dessus du bruit ambient                  
                    
        try: 
            print("un instant .... ")
            query = self.r.recognize_google(audio, language="fr_FR")
            print(f"vous avez dit : {query}")
        
        except:
            pass
    
        query = str(query)  
        return query.lower()


    def say(self, text):
        print("     ")
        print(f"Connor: {text}")
        self.engine.say(text=text) 
        self.engine.runAndWait() 
        print("     ") 
    