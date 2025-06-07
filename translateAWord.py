import pyaudio
import speech_recognition as sr
import sys
from PyDictionary import PyDictionary 
class WordTranslate:
    global r     
    global text  
    def translateWord():
        ###set up functions for translateWord
        def findLanguage():
            Language = input("Translate To: ").lower()
            langDict = {"english":"en", "hindi":"hi", "spanish":"en", "dutch":"de", "french": "fr", "russian":"ru", "polish":"pl", "chinese":"zh"}
            for x in langDict:
                if x == Language:
                    return langDict[Language]
        def commandManager(text):
            match text:
                case "Exit Program":
                    sys.exit()
                case _:
                    return 0
        ###Main function portion 
        ##with speech recognition using microphone we are gonna read the word then translate it with pyDictionary
        r = sr.Recognizer()    
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            try:    
                while True:
                    phrase = r.listen(source)    
                    print("Word To Translate: ", end="")                    
                    try:
                        text = r.recognize_sphinx(phrase) 
                        commandManager(text)
                        print(text)
                    except sr.UnknownValueError:
                        print("Input Not Received")
                    finally:
                        ##if theres a word recieved translate it in what ever language is picked when findLanguage is called
                        if bool(text) != None:
                            print("Word Translated:" ,PyDictionary().translate(text, findLanguage()))
                            return text
                        else:
                            print("No Input Received")
            except KeyboardInterrupt:
                    print("Interruption")
