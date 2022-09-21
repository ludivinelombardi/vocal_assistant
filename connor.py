from main import AI
from skills import Skills
from nlu import classifier
from nlu.classifier import classify
import time
from tkinter import *
from PIL import Image, ImageTk 
from tkinter import ttk

def Commands():
    connor = AI()
    command = connor.listen()
    entity = classify(command)

    while True and entity != "partir/exit": 
        
        if entity in "salutation/greeting":
            connor.say(Skills.greeting())
            print(Skills.greeting())
            command = connor.listen()
            entity = classify(command)
            
        elif entity in "santé/health":
            connor.say(Skills.health())
            command = connor.listen()
            entity = classify(command)
                
        elif entity in "heure/getTime":
            connor.say(Skills.get_time())
            command = connor.listen()
            entity = classify(command)
                
        elif entity in "open/openGoogle":
            Skills.open_browser()
            connor.say("Voilà, j'ai ouvert Google sur ton navigateur")
            command = connor.listen()
            entity = classify(command)
                
        elif entity in "open/openYoutube":
            Skills.open_youtube()
            connor.say("Voilà, j'ai ouvert Youtube")
            command = connor.listen()
            entity = classify(command)
                
        elif entity in "temps/getWeather":
            connor.say(Skills.get_weather())
            command = connor.listen()
            entity = classify(command)
                
        elif entity in "confusion/noanswer":
            command = connor.listen()
            entity = classify(command)
                
        elif entity in "email/mail": 
            Skills.open_mail()
            connor.say("Voilà, j'ai ouvert l'application mail")
            command = connor.listen()
            entity = classify(command)
                
        elif entity in "calendrier/calendar": 
            Skills.open_calendar()
            connor.say("Voilà, j'ai ouvert ton calendrier")
            command = connor.listen()
            entity = classify(command)
                
        elif entity in "message/sms": 
            Skills.open_message()
            connor.say("Voilà, j'ai ouvert tes messages")
            command = connor.listen()
            entity = classify(command)
                
        elif entity in "git/openGit": 
            Skills.open_github()
            connor.say("Voilà, j'ai ouvert git kraken")
            command = connor.listen()
            entity = classify(command)
                
        elif entity in "batterie/système": 
            connor.say(Skills.battery_info())
            command = connor.listen()
            entity = classify(command)
                
        elif entity in "terminal/shell": 
            Skills.open_shell()
            connor.say("Voilà, j'ai ouvert le terminal")
            command = connor.listen()
            entity = classify(command)
            
    connor.say(Skills.leaving())
                
     
Commands()
     
# root = Tk()
# root.geometry("600x700+400+80")
# root.title("Connor, assistant virtuel")
# root.resizable(False,False)

# #icon 
# image_icon=PhotoImage(file="images/ai-icon.png")
# root.iconphoto(False, image_icon)

# #logo 
# photo=PhotoImage(file="images/v-a.png")
# mylogo=Label(image=photo, background=None)
# mylogo.pack(padx=5,pady=5)

# #titre 
# Label(text="Connor, assistant virtuel", font="Avenir 30 bold", background=None, fg="white").pack()

# #button 
# listen=Button(root,font="Avenir 20", text="Je vous écoute", fg="white", border=1, command=Commands()).pack(pady=30)
# root.mainloop()
 