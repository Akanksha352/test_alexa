#!/usr/bin/env python
# coding: utf-8

# In[4]:


import speech_recognition as sr
import datatime as dt
import wikipedia as wk
import pywhatkit as pw
import pyttsk3 as ps
import pyjokes as pj
import sys
import webbrowser as wb


# In[21]:


engine = pw.init()
engine.setProperty("rate" , 150)
voices = engine.getPropety("voices")
engine.setProperty("voice" , voices [1].id)
recognizer = sr.Recognizer()

def engine_talk():
    engine.say(text)
    engine.runAndWait

def run_alexa():
    with sr.microphone as source:
        recognizer.adjust_for_ambient_noise(source,duration=1)
        print('/n')
        print('start speaking!')
        engine_talk('listening....')
        recordedaudio= recognizer.listen(source)
        try:
            command = recognizer.recognizer_google(recordedaudio, language ='en-in')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa' ,'')
                print('you said' + command)
            else:
                print('you said' + command)
            
            if 'hello' in command:
                print("Hi, how can I help you")
                engine_talk("Hi, how can I help you")
            elif 'who are u' in command:
                print("I am a mini alexa a k a a virtual assistant")
                engine_talk("I am a mini alexa a k a a virtual assistant, how can i help you")
                
            elif 'what can u do' in command:
                print("I can play song on youtube, tell u a joke,tell you date and time, find your location, locate area on map, search on wikipedia, open different websites like instagram, youtube,gmail, git hub, stack overflow and searches on google.How may i help you ??")
                engine_talk("I can play song on youtube, tell u a joke,tell you date and time, find your location, locate area on map, search on wikipedia, open different websites like instagram, youtube,gmail, git hub, stack overflow and searches on google.How may i help you ??")
            elif 'play' in command:
                song = command.replace('play', '')
                print("playing.."+ song)
                engine_talk('playing..' + song)
                pw.playonyt(song)
            elif 'date and time' in command:
                today = date.today()
                time = datetime.datetime.now().strftime('%I:%M %p')
                # texual date 
                d2 = today.strftime('%B %d %Y')
                print("Today's date is: ",  d2, 
                      "and time is:", time )
                engine_talk("Today is : " + d2) 
                engine_talk("and  current time is:" + time )
                            
            elif 'time and date' in command:
                
                today = date.today()
                time = datetime.datetime.now().strftime('%I:%M %p')
                # texual date 
              
                d2 = today.strftime('%B %d %Y')
                print("Time is:" ,time,
                      "and today's date is: " , d2  )
                engine_talk("current time is:" + time)
                engine_talk("and Today is : " + d2  )
                            
            elif 'date' in command:
                today = date.today()
                d2 = today.strftime('%B %d %Y')
                print("Today's date is: " , d2)
                engine_talk("Today is : " + d2  )
                            
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print("Time is:" , time)
                engine_talk("current time is:" + time)
                      
             
            elif 'tell me about' in command: 
                n= command.replace("tell me about", '')
                info = wikipedia.summary(n,1)
                print(info)
                engine_talk(info)
                      
            elif 'what is' in command:
                n= command.replace("what is", '')
                info = wikipedia.summary(n,1)
                print(info)
                engine_talk(info)
                      
            elif 'who is' in command:
                n= command.replace("who is", '')
                info = wikipedia.summary(n,1)
                print(info)
                engine_talk(info)
                
                      
            elif 'what is' in command:
                search = 'https://www.google.com/search?q='+ command
                print("Here's what i found on internet...")
                engine_talk("searching ...Here's what i found on internet  ")
                wb.open(search)
                      
            elif 'joke' in command: 
                j= pj.get_joke()
                print(j)
                engine_talk(j)
        
            elif 'search' in command:
                search = 'https://www.google.com/search?q='+ command
                engine_talk("searching")
                wb.open(search)
                      
            elif 'my location' in command:
                url = 'https://www.google.com/maps/search/where+I+am+?'+ command
                wb.get().open(url)
                engine_talk('as Per google maps u must be somewhere here')
                    
            elif 'locate' in command:
                l = command.replace('locate', '')
                if 'on map' in l:
                    u =l.replace('on map','')
                url = 'https://www.google.com/maps/place/'+ l[1] +'/&amp;'
                wb.get().open(url)
                print("Here's the location of"+ l[1])
                engine_talk("Here's the location of"+ l[1])
                
            elif 'on map' in command:
                engine_talk('locating ...')
                l = command.split(" ")
                print(l[1])
                url = 'https://www.google.com/maps/place/'+ l[1] +'/&amp;'
                wb.get().open(url)
                print("Here's the location of"+ l[1])
                engine_talk("Here's the location of"+ l[1])
                      
            elif 'where is' in command:
                engine_talk('locating ...')
                l = command.replace("where is ",'')
                url = 'https://www.google.com/maps/place/'+ l[1] +'/&amp;'
                wb.get().open(url)
                print("Here's the location of"+ l[1])
                engine_talk("Here's the location of"+ l[1])
                      
            elif 'location of' in command:
                engine_talk('locating ...')
                l = command.replace("find location of ",'')
                
                url = 'https://www.google.com/maps/place/'+ l[1] +'/&amp;'
                wb.get().open(url)
                print("Here's the location of"+ l[1])
                engine_talk("Here's the location of"+ l[1])
            elif 'open google' in command:
                print("Opening google...")
                engine_talk("Opening google...")
                wb.open_new('https://www.google.co.in/')
            
            elif 'open gmail' in command:
                print("Opening gmail...")
                engine_talk("Opening gmail...")
                wb.open_new('https://mail.google.com/')
                      
            elif 'open youtube' in command:
                print("Opening youtube...")
                engine_talk("Opening youtube...")
                wb.open_new('https://www.youtube.com/')
                      
            elif 'open github' in command:
                print("Opening github...")
                engine_talk("Opening github...")
                wb.open_new('https://www.github.com/') 
            elif 'open stackoverflow' in command:
                print("Opening stackoverflow...")
                engine_talk("Opening stackoverflow...")
                wb.open_new('https://www.stackoverflow.com/') 
            
            elif 'bye' in command:
                print("Goodbye.Have a nice day!!")
                engine_talk("Goodbye.Have a nice day!!")
                sys.exit()
                    
            elif 'tata' in command:
                print("Goodbye.Have a nice day!!")
                engine_talk("Goodbye.Have a nice day!!")
                sys.exit()
            elif 'stop' in command:
                print("Goodbye.Have a nice day!!")
                engine_talk("Goodbye.Have a nice day!!")
                sys.exit()
            elif 'thank you' in command:
                print("your welcome!!")
                engine_talk("your welcome!!")
                sys.exit()
            
            else:
                print("Here's what I found on internet")
                engine_talk("Here's what I found on internet")
                search = 'https://www.google.com/search?q='+ command
                wb.open(search)
        except Exception as ex:
            print(ex)
                      
print('Clearing background noise...Please wait')
engine_talk('Clearing background noise...Please wait')
print('\n')
print("hello, i am mini alexa how can i help you ??")
engine_talk ("hello i am mini alexa how can i help you ")
while True:
    run_alexa()


# In[ ]:




