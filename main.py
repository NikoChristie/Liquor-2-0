import pyaudio
import speech_recognition as sr
import pyttsx3
import os

os.system('cls')

print('Liquor 2.0')

engine = pyttsx3.init()

r = sr.Recognizer() 
mic = sr.Microphone(device_index=0) 

def main():
    audio = None
    with mic as source:
        print('listening...')
        try:
            audio = r.listen(source, 1, 2)
        except sr.WaitTimeoutError:
            pass
        if audio is not None:
            try:
                result = (r.recognize_google(audio)).split()
                print('running')

                for i in result:
                    if len(i) > 4:
                        s = i
                        
                        if(s == 'terminate'):
                            engine.say("late her? I barely even knew her!")
                            engine.runAndWait()
                            exit()

                        if i.endswith('s'):
                            s = str(s[:-1]) 
                        
                        if s.endswith(('er', 'or', 'ur')):
                            print("{0} her? I barely even knew her!".format(s[:-2]))
                            engine.say("{0} her? I barely even knew her!".format(s[:-2]))
                            engine.runAndWait()
                print('done')
            except sr.UnknownValueError:
                print('???')
    main()

main()
