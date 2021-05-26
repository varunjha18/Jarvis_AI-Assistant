import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
 

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<16:
        speak("good morning")
    else:
        speak("good evening")
    speak("This is Jarvis, How may I help you")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=800
        audio = r.listen(source)
        print(audio)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('varunjha1245@gmail.com', '*********')
    server.sendmail('varunjha1245@gmail.com', to, content)
    server.close()









if __name__ == "__main__":
    speak("teen guna lagan dena padega ")
    emails={'varun':'varunjha2000@gmail.com'}
    #wishMe()
    while 1:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            #music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            #songs = os.listdir(music_dir)
            #print(songs)    
            os.startfile("C:\\Users\\varun\\Desktop\\Python\\Jarvis\\song.mp3")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")    

        elif 'email to' in query:
            receiver=query[query.index('email to')+8:].split()[0]
            try:
                speak("What should I say?")
                content = takeCommand()
                to = emails[receiver]    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")    


