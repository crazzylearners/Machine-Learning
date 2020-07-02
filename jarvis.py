import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import os

#Reach to the local lappy voices
main = pyttsx3.init('sapi5')
#select voices
voices = main.getProperty('voices')
#print(voices[1].id)
main.setProperty('voices',voices[0].id)


def speak(audio):
         main.say(audio)
         main.runAndWait()

def wish():
         hr = int(datetime.datetime.now().hour)
         if hr>=0 and hr<12 :
                  speak('good morning!')
         elif hr>=12 and hr<=17:
                  speak('good afternoon!')
         else :
                  speak('good evening!')
         speak('I am Jarvis, how can I help you?')

def linput():

         r = sr.Recognizer()
         with sr.Microphone() as source:
                  print('Speak now...')
                  r.pause_threshold = 2
                  audio = r.listen(source)
         try :
                  print("Recognizing...")
                  query = r.recognize_google(audio)#, Language='en-in'
                  print('You said :',query)
         except Exception as e:
                  print('Sorry, speak it again...')
                  return 'none'
         return query

def sendEmail(to,content):
         server = smtplib.SMTP('smtp.gmail.com', port=587)
         server.ehlo()
         server.starttls()
         server.login('anmolvarshney91@gmail.com','Anmol@0909')
         server.sendmail('anmolvarshney91@gmail.com',to,content)
         server.close()

def pngtojpg():
    import tkinter as tk
    from tkinter import filedialog
    from PIL import Image

    root = tk.Tk()
    canvas1 = tk.Canvas(root,width=300,height=250,bg='azure3',relief='raised')
    canvas1.pack()

    label1 = tk.Label(root,text='File Conversion Tool',bg='azure3')
    label1.config(font=('georgia',20))
    canvas1.create_window(150,60,window=label1)

    def pngfile():
            global img1
            path=filedialog.askopenfilename()
            img1=Image.open(path)
            #path=filedialog.askopenfilename()
            #im1=Image(path)

    def convert():
            global img1
            exp_path = filedialog.asksaveasfilename(defaultextension='.jpg')
            img1.save(exp_path)

    saveasbutton=tk.Button(text='Convert PNG to JPG', command=convert,
                        bg='royalblue',fg='white',font=('georgia',12,'bold'))
    canvas1.create_window(150,180,window=saveasbutton)
    root.mainloop()



''' MAIN_PROGRAM'''


speak("Welcome to world of Artificial Intelligence")
wish()
while True:
        query = linput().lower()

        if 'wikipedia' in query:
                  speak('Searching Wikipedia...')
                  query = query.replace('Wikipedia','')
                  results = wikipedia.summary(query,sentences = 2)
                  speak('According to Wikipedia')
                  print(results)
                  speak(results)
        elif 'youtube' in query:
                  webbrowser.open('youtube.com')
        elif 'google' in query:
                  webbrowser.open('google.com')
        elif 'crazylearners' in query:
                  webbrowser.open('crazzylearners.com')
        elif 'time' in query :
                  time = datetime.datetime.now().strftime('%H:%M:%S')
                  print(time)
                  speak('currently time is')
                  speak(time)
        elif 'open idle' in query:
                  path = "C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\idlelib\\idle.pyw"
                  os.startfile(path)
        elif 'quit' in query:
                  exit()
        elif 'email' in query:
                  
                try:
                            speak('Tell me the domain id of receiver')
                            to = linput().lower()
                            to = to.replace(' ','')
                            print('Is this mail id is correct : ',(to+'@gmail.com'))
                            print('Yes/No')
                            user_reply = linput().lower()
                            if(user_reply=='yes'):
                                speak('What should I write in mail?')
                                content = linput()
                                to=to+'@gmail.com'
                                sendEmail(to,content)
                                speak('Email has been sent!')
                            else:
                                print('Sorry try to say email again.')
                except Exception as e:
                            print(e)
                            speak("Sorry email can't be sent!")    
        elif 'png to jpg' in query:
            pngtojpg()  

