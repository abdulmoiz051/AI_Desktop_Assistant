from google import genai
import speech_recognition as speech
import pyttsx3, webbrowser, os, time
import gemini_conf

client = os.getenv("gemini_api")

import speech_recognition as sr

r = sr.Recognizer()

if __name__ == "__main__":
    while(True):
        with sr.Microphone() as source:
            pyttsx3.speak("Listening jarvis  properly.....")
            print("Listening... Say something!") 
            audio = r.listen(source)

            try:
                convert_audio_into_text = r.recognize_google(audio)
                if(convert_audio_into_text in "Jarvis"):
                    print(f"Jarvis : Yahh...")
                    pyttsx3.speak("Yahh...")
                    after_yah = r.listen(source)
                    again_listen = r.recognize_google(after_yah)
                    links_lists = [["youtube", "https://www.youtube.com/"], ["facebook", "https://www.facebook.com/"], ["ai", "https://chatgpt.com/"], ["ziauddin", "https://zu.edu.pk/"], ["reddit", "https://www.reddit.com/"], ["instagram", "https://www.instagram.com/?hl=en"]]

                    if "write" in again_listen.lower():
                        gemini_conf.generate_file(gemini_conf.pass_prompt(again_listen))
                        print(f"User : {again_listen}")
                        print("File generated")
                        pyttsx3.speak("I generated the file")
                        time.sleep(3)

                    elif "start vs code" in again_listen.lower():
                        print(f"User : {again_listen}")
                        print(f"Jarvis : Opeaning visual studio sir.....")
                        pyttsx3.speak("Opeaning visual studio sir.....")
                        os.startfile(r"C:\Users\Dell\AppData\Local\Programs\Microsoft VS Code\Code.exe")
                        time.sleep(4)

                    elif "open" in again_listen.lower():
                        for i in links_lists:
                            if f"open {i[0]}" in again_listen.lower():
                                print(f"Jarvis : Opening {i[0]} sir....")
                                pyttsx3.speak(f"Opening {i[0]} sir....")
                                webbrowser.open(i[1])

                    elif "jarvis exit" in again_listen.lower():
                        break
 
                    else:
                        prompt = gemini_conf.pass_prompt(again_listen)
                        print(f"User : {again_listen}") 
                        print(f"Jarvis : {prompt}") 
                        pyttsx3.speak(f"{prompt}")
                        time.sleep(3)

                # pyttsx3.speak(convert_audio_into_text)
            except:
                pyttsx3.speak("Someting wrong right now so be careful next time")
    

# config of object and the __exit__ method is generate the concept of context manager concept right now r.adjust_for_ambient_noise(source, duration=1)