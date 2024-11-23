import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
import os

# Your Oxford Dictionaries API credentials
app_id = "e656702f"  # Replace with your Oxford Dictionaries App ID
app_key = "d228a5e52ec2143cd206b75d8ad9d1fe"  # Replace with your Oxford Dictionaries App Key

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "2d61dc1bb95846569bf7b45917576852"
dictapi = "https://od-api-sandbox.oxforddictionaries.com/api/v2" 

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    # os.remove("temp.mp3")
    
def get_hindi_translation(word):
    # API endpoint for Oxford Dictionaries API (entries endpoint)
    url = f"https://od-api-sandbox.oxforddictionaries.com/api/v2/entries/en-us/{word.lower()}"
    
    # Set the headers with your app credentials
    headers = {
        "app_id": app_id,
        "app_key": app_key
    }

    # Make the API request
    response = requests.get(url, headers=headers)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        
        # Check if Hindi translations are available
        try:
            # Navigate through the JSON data structure to find translations (if available)
            translations = data.get('results', [])
            for result in translations:
                if 'lexicalEntries' in result:
                    for lexical_entry in result['lexicalEntries']:
                        if 'entries' in lexical_entry:
                            for entry in lexical_entry['entries']:
                                if 'senses' in entry:
                                    for sense in entry['senses']:
                                        if 'translations' in sense:
                                            for translation in sense['translations']:
                                                if translation['language'] == 'hi':  # Hindi language code
                                                    return translation['text']
        except KeyError:
            speak("Translation not found in Hindi.")
            return None
    else:
        speak(f"Error fetching translation: {response.status_code}")
        return None

def processCommand(c):
    if "translate" in c.lower():
        speak("Please tell me the English word youṇ want to translate into Hindi.")
        
        # Listen for the English word after the initial command
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for English word...")
            audio = recognizer.listen(source)
            word = recognizer.recognize_google(audio).lower()

            print(f"Received word: {word}")

            # Get Hindi translation from Oxford API
            hindi_word = get_hindi_translation(word)
            if hindi_word:
                speak(f"The Hindi translation of {word} is: {hindi_word}")
            else:
                speak(f"Sorry, I couldn't find the translation for {word}.")
                
    elif "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open wikipedia" in c.lower():
        webbrowser.open("https://www.wikipedia.org/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "tell me the news" in c.lower():
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code == 200:
                # Parse the JSON response
                data = r.json()

                # Extract the articles
                articles = data.get('articles', [])

                # Print the headlines
                if articles:
                    for article in articles:
                        speak(article['title'])
                else:
                    speak("Sorry, I couldn't find any news at the moment.")

            else:
                speak("Sorry, there was an issue fetching the news.")

        except requests.exceptions.RequestException as e:
            print(f"Error while fetching news: {e}")
            speak("Sorry, there was an error fetching the news.")

    else:
        speak("Sorry! Please tell me again.")
    

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                speak("Listening...")
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if word.lower() == "hello jarvis":
                speak("Yaa, how can I help?")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
