import pyaudio
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', pyttsx3.voices[0].id) 

r = sr.Recognizer() 
mic = sr.Microphone(device_index=0) 

def main():
    with mic as source:
        print('listening...')
        audio = r.listen(source)
    
    try:
        print('running')
        result = (r.recognize_google(audio)).split()

        for i in result:
            if len(i) > 4:
                s = i
                
                if i.endswith('s'):
                    s = str(s[:-1]) 
                
                print(s)
                if s.endswith(('er', 'or', 'ur')):
                    print("{0} her? I barely even knew her!".format(s[:-2]))
                    engine.say("{0} her? I barely even knew her!".format(s[:-2]))
                    engine.runAndWait()
    except sr.UnknownValueError:
        print('???')
    finally:
        print('done')
    main()

main()
