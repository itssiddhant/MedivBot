import speech_recognition as sr
import pyttsx3
from bs4 import BeautifulSoup
import requests
import datetime
import wikipedia
from RobotControl import *
from PatientDatabase import *

r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def voice_command(command):
    text = command.lower()
    global PID
    if "patient id" in text or "patient number" in text:
        words = text.split()
        index = words.index("ID")
        PID = words[index+1]
        return PID    
    
    elif "control robotic surgeon" in text:
        speak_text("Ok!" + (text))
        control_robotic_surgeon(text)
    elif "search for" in text:
        result = search(text)
        print(result)
    elif "schedule ct" in text or "ct scan" in text:
        print(PID)
        schedule_ct_scan(PID)
    elif "blood pressure" in text or "check blood pressure" in text:
        check_blood_pressure(PID)
    elif "write a note" in text or "record this for patient" in text:
        record_note_patient(PID)
    elif "latest lab" in text or "speak the latest lab result" in text:
        view_latest_lab_results(PID)
    elif "order medication" in text or "injection" in text or "test" in text:
        order_medication(PID)
    elif "what is the time" in text or "time" in text:
        asked_time = time()
        speak_text(asked_time)
    elif "all the patient" in text or "all the patients" in text:
        list_patients()
    else:
        return text


def search(search_term):
    st= search_term.split()
    if "article" in st or "artical" in st:
        w = st.index("article")
        stfinal = st[w + 1]
        url = f"https://pubmed.ncbi.nlm.nih.gov/?term={stfinal}"
        
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text

            # Use BeautifulSoup to parse the HTML
            soup = BeautifulSoup(html_content, 'html.parser')

            # Find the relevant information within the first article
            first_article = soup.find('article')

            if first_article:
                # Extract title and snippet (modify this based on actual HTML structure)
                title = first_article.find('a', class_='docsum-title')
                snippet = first_article.find('div', class_='docsum-content')

                if title and snippet:
                    title_text = title.get_text(strip=True)
                    snippet_text = snippet.get_text(strip=True)

                    # Speak out the top result
                    speak_text(f"The top result is titled: {title_text}. Here is a snippet: {snippet_text}")


        else:
            speak_text("No Article Found")
        # text = url.get_text()
        # return text
    elif 'for' in st:
        w1=st.index("for")
        stf= st[w1+1]
        try:
            result = wikipedia.summary(stf, sentences=2)
            speak_text(f"The Wikipedia summary for '{stf}' is: {result}")
        except wikipedia.exceptions.PageError:
            speak_text("No Wikipedia page found for the given term.")
    else:
        speak_text("Couldn't Find Anything Doc")
    
def time():
    now = datetime.datetime.now()
    time_string = now.strftime("%H:%M:%S")
    return time_string


def recognize_speech():
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Speak now...")
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        # Listen for audio input
        audio = r.listen(source)
        try:
            # Use Google Speech Recognition API to convert speech to text
            text = r.recognize_google(audio)
            print("You said:"+text)
            voice_command(text.lower())            

        except sr.UnknownValueError:
            print("Could not understand audio")
            while True:
                try:
                    # Listen for audio input again
                    print("Speak again...")
                    audio = r.listen(source)
                    textt = r.recognize_google(audio)
                    voice_command(textt)
                    break
                except sr.UnknownValueError:
                    pass
        return None

speak_text("Hello Doc! How can I help you?")
rtext = recognize_speech()
