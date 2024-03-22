import speech_recognition as sr
import pyttsx3
import pyfiglet
import webbrowser
from googlesearch import search

import re
import pywhatkit
import pyautogui
from PIL import Image
import sys
import time
import keyboard
import pyjokes


    

f = pyfiglet.figlet_format("JARVIS")

def speak(text, voice_id=None, rate=130):
    engine = pyttsx3.init()
    
    # Set the voice (you may need to experiment with different voice_ids)
    if voice_id:
        engine.setProperty('voice', voice_id)

    # Set the speech rate (words per minute)
    engine.setProperty('rate', rate)

    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your audio.")
        return ""
    except sr.RequestError as e:
        print(f"Speech recognition request failed: {e}")
        return ""
    
  
def process_command(command):
    

    if 'font art' in command:
        speak("Enter what do you want to transform in text art")
        ee= input("Enter what do you want to transform in text art: ")
        j = pyfiglet.figlet_format(ee)
        print("Working....")
        time.sleep(2)
        print(j)
        
    elif "play" in command:
            query = command.split("play")[1].strip()
            pywhatkit.playonyt({query})
            
            speak(f"Playing {query}.")
    if 'stop' in command:
        sys.exit()
    elif 'pause' in command:
        pyautogui.press('space')
        speak("Stopping the video.")
    
    if "type" in command:
        speak("Ok sir")
        query = command.split("type")[1].strip()
        keyboard.write(query, delay=0.1)
    if "your favourite sentence" in command:
       
        keyboard.write("I LOVE YOU (^///^)❤️")
    if "show picture of developer" in command:
        img = Image.open("Shubham 4.jpg")
        img.show()
    if "tell jokes" in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    elif "close tab" in command:
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'w')    
        
    elif "lock my laptop" in command:
                time.sleep(2)
                pyautogui.hotkey('win','l')
                
    elif "move mouse" in command:
        delay = 5

        # Duration of the drag (in seconds)
        drag_duration = 2

        # Sleep for the specified delay
        time.sleep(delay)

        # Get the starting position for the drag
        start_x, start_y = pyautogui.position()

        # Specify the distance to drag (you can adjust these values)
        drag_distance_x = 500
        drag_distance_y = 500

        # Calculate the ending position for the drag
        end_x = start_x + drag_distance_x
        end_y = start_y + drag_distance_y

        # Move the mouse to the starting position
        pyautogui.moveTo(start_x, start_y, duration=0.5)

        # Perform a mouse press (simulate clicking and holding)
        pyautogui.mouseDown()

        # Move the mouse to the ending position over the specified duration
        pyautogui.moveTo(end_x, end_y, duration=drag_duration)

        # Perform a mouse release (simulate releasing the mouse button)
        pyautogui.mouseUp()

           
    elif "click" in command:
            delay = 2
            time.sleep(delay)

            x, y = pyautogui.position()


            pyautogui.click(x, y)   
            print(f"Mouse clicked at position: ({x}, {y}) after {delay} seconds")
    
        
    elif "jarvis open youtube" in command:
        website = command.split("jarvis open youtube")[1].strip()
        
        url = f"youtube.com"
        webbrowser.open(url)
        speak(f"Opening youtube website.")
        

  
    elif "what is my name" in command:
        speak("Your Name is Shubham kumar")
        speak("You are a good boy and study in 9th class")
        
    elif "assistant" in command:
          query = command.split("assistant")[1].strip()
          url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
          webbrowser.open(url)
          speak(f"Searching Google for {query}.")
         
        
    elif "who made you" in command:
        speak("A frontend developer Shubham kumar developed me and i am here for serving humanity")   
    elif "what is my age" in command:
         speak("You are 15 year old")
         
       
       
         
    elif "what is my father name" in command:
        speak("Your father name is Sanjay kumar jha")
        print("Sanjay kumar jha")
        
        
    elif "gpt" in command:
        gpt = command.split("gpt")[1].strip()
        url=f"www.chat.openai.com"
        webbrowser.open(url)
    
            
        
    elif "what is my mother name" in command:
        speak("Your mother name is suleta kumari jha")       
 
    elif "what is my sister name" in command:
        speak("Your sister name is sakshi raj")
 
    elif "what can you do" in command:
        speak("I can search anything for google just by saying command.and i can also open websites╰(*°▽°*)╯")
    
    else:
       speak("Sorry sir")
       print("Sorry sir i am not prrogrammed for this command U_U")

if __name__ == "__main__":
    print(f)
    speak("Hello sir,I am your jarvis sir how can i assist you")
    print("Hello sir,I am your jarvis sir how can i assist you")
    

    while True:
        command = recognize_speech()
        


        if command:
            process_command(command)
            