import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from groq import Groq

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "7a517dd8b81547109073691923a4ec92"
def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiprocess(command):
        client = Groq(
           api_key="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",
         )

        chat_completion = client.chat.completions.create(
           messages=[
              {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud.(try to act like jarvis from the iron man movie and call me sir and also do not call me sir everytime you finish a sentence or line.)"},
              {"role": "user", "content": command }
              ],
             model="llama3-8b-8192",
         )

        return chat_completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
       speak("as you say")
       webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
       speak("as you say")
       webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
       speak("as you say")
       webbrowser.open("https://youtube.com") 
    elif "open linkedin" in c.lower():
       speak("as you say")
       webbrowser.open("https://linkedin.com")
    elif "open github" in c.lower():
       speak("as you say")
       webbrowser.open("https://github.com")
    elif "play" in c.lower():
       song=c.lower()
       if("like that" in song):
          link=musiclibrary.music["like that"]
          speak("good choice sir")
          webbrowser.open(link)  
       if("not like us" in song):
          link=musiclibrary.music["not like us"]
          speak("good choice sir")
          webbrowser.open(link)    
       if("like that guitar version" in song):
          link=musiclibrary.music["like that guitar version"]
          speak("good choice sir")
          webbrowser.open(link) 
       if("travis" in song or "fien" in song):
          link=musiclibrary.music["fien"]
          speak("good choice sir")
          webbrowser.open(link)  
    elif "news" in c.lower():
                  r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")           
                  if r.status_code == 200:
                      #parse the json reponse
                      data = r.json()

                      #extract the articles
                      articles = data.get('articles',[])

                      #speak the headlines
                      for article in articles:
                          speak(article['title'])
    else: 
        #let openAI handle the query
        output = aiprocess(c)
        speak(output)
                              

if(__name__=="__main__"):
    speak("Initialising Jarvis........")
    #listen for the activation word "jarvis"
    # obtain audio from the microphone
    
    while True:
        r = sr.Recognizer()
     # recognize speech using Sphinx
        print("recognizing....")
        try:
            with sr.Microphone() as source:
              print("Listening.....")
              audio = r.listen(source,timeout=3,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
               speak("Yes Sir..")
               #listen for a command to be given
               with sr.Microphone() as source:
                   print("Jarvis is listening.....")
                   speak("what can i do for you?")
                   audio = r.listen(source)
                   command = r.recognize_google(audio)
 
                   processCommand(command)

        except Exception as e:
         print("Error; {0}".format(e))