import speech_recognition
import mysql.connector
import pyttsx3
import os
import flask


class mic (BaseException):
    recognizer = speech_recognition.Recognizer()

    mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="job_portal"
        )
    while True:
        try:
        
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()

                print(f"Recognized {text}")
    
#    except:
#        recognizer = speech_recognition.Recognizer()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            continue

