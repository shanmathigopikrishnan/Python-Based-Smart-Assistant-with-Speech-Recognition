import os
import speech_recognition as sr
import pyttsx3
import datetime as dt
import webbrowser
import wikipedia
import pyjokes
import requests
import smtplib

# --- CONFIGURATION ---
ASSISTANT_NAME = "Nova"

# Optional: Read email credentials from environment variables
EMAIL_USER = os.getenv("NOVA_EMAIL")      # Set in your system
EMAIL_PASS = os.getenv("NOVA_EMAIL_PASS") # Set in your system

# --- INITIALIZATION ---
engine = pyttsx3.init()
recogniser = sr.Recognizer()
reminders = []

def speak(text: str) -> None:
    print(f"{ASSISTANT_NAME}: {text}")
    engine.say(text)
    engine.runAndWait()

def listen() -> str:
    with sr.Microphone() as source:
        recogniser.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = recogniser.listen(source)
    try:
        query = recogniser.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("I didn't catch that, please repeat.")
    except sr.RequestError:
        speak("Speech service is not available.")
    return ""

def greet() -> None:
    hour = dt.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak(f"I'm {ASSISTANT_NAME}. How can I help?")

def set_reminder(text: str) -> None:
    reminders.append(text)
    speak(f"Reminder set: {text}")

def show_reminders() -> None:
    if reminders:
        speak("Here are your reminders:")
        for r in reminders:
            speak(r)
    else:
        speak("You have no reminders.")

def send_email(to_addr: str, subject: str, body: str) -> None:
    if not EMAIL_USER or not EMAIL_PASS:
        speak("Email credentials are not set in environment variables.")
        return
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(EMAIL_USER, to_addr, message)
        speak("Email sent successfully.")
    except Exception as e:
        speak(f"Failed to send email. {e}")

def main():
    greet()
    while True:
        query = listen()
        if not query:
            continue

        if "time" in query:
            current_time = dt.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}.")
        elif "date" in query:
            today = dt.datetime.now().strftime("%A, %d %B %Y")
            speak(f"Today's date is {today}.")
        elif "wikipedia" in query:
            speak("What should I search on Wikipedia?")
            topic = listen()
            if not topic:
                continue
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak(summary)
            except wikipedia.DisambiguationError as e:
                speak("The topic is ambiguous. Did you mean: " + ", ".join(e.options[:5]))
            except Exception:
                speak("Sorry, I couldn't find that on Wikipedia.")
        elif query.startswith("open"):
            if "youtube" in query:
                webbrowser.open("https://youtube.com")
                speak("Opening YouTube.")
            elif "google" in query:
                webbrowser.open("https://google.com")
                speak("Opening Google.")
            else:
                site = query.replace("open ", "").strip()
                webbrowser.open(f"https://{site}")
                speak(f"Opening {site}.")
        elif "weather" in query:
            speak("Which city?")
            city = listen()
            if city:
                speak(get_weather(city))
        elif "remind me" in query or "set reminder" in query:
            speak("What should I remind you about?")
            reminder = listen()
            if reminder:
                set_reminder(reminder)
        elif "show reminders" in query or "my reminders" in query:
            show_reminders()
        elif "joke" in query:
            speak(pyjokes.get_joke())
        elif "send email" in query:
            speak("What's the recipient's email address?")
            recipient = listen()
            speak("What's the subject?")
            subject = listen()
            speak("What should I say?")
            message = listen()
            if recipient and subject and message:
                send_email(recipient, subject, message)
        elif any(word in query for word in ["exit", "quit", "stop", "bye"]):
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I can only do basic tasks at the moment.")

if __name__ == "__main__":
    main()