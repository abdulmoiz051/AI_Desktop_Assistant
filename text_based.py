from google import genai
import speech_recognition as speech
import pyttsx3, webbrowser, os, time
import gemini_conf

client = genai.Client(api_key="AIzaSyB1ENqmJ1uEJpsr56r94cDUJeNExLENvrg")

if __name__ == "__main__":
        while(True):
            pyttsx3.speak("Active jarvis properly.....")
            print("Say something!.....") 

            text = input("Prompt : ")
            if(text in "Jarvis"):
                print(f"Jarvis : Yahh...")
                pyttsx3.speak("Yahh...")
                again_listen = input("Prompt : ")
                links_lists = [["youtube", "https://www.youtube.com"], ["facebook", "https://www.facebook.com/"], ["ai","https://chatgpt.com/"], ["ziauddin", "https://zu.edupk/"], ["reddit", "https://www.reddit.com/"],["instagram", "https://www.instagram.com/?hl=en"]]

                if "write" in again_listen.lower():
                    gemini_conf.generate_file(gemini_conf.pass_prompt(again_listen))
                    print(f"User : {again_listen}")
                    print("File generated")
                    pyttsx3.speak("I generated the file")
                    time.sleep(3)

                elif "start vs code" in again_listen.lower():
                    print(f"User : {again_listen}")
                    print(f"Jarvis : Opening visual studio sir.....")
                    pyttsx3.speak("Opening visual studio sir.....")
                    os.startfile(r"C:\Users\Dell\AppData\Local\Programs\Microsoft VS Code\Code.exe")
                    time.sleep(4)

                elif "open" in again_listen.lower():
                    for i in links_lists:
                        if f"open {i[0]}" in again_listen.lower():
                            print(f"Jarvis : Opening {i[0]} sir....")
                            pyttsx3.speak(f"Opening {i[0]} sir....")
                            webbrowser.open(i[1])
 
                elif "jarvis exit" in again_listen.lower():
                    pyttsx3.speak("Take care....")
                    break

                else:
                    prompt = gemini_conf.pass_prompt(again_listen)
                    print(f"User :  {again_listen}") 
                    print(f"Jarvis : {prompt}") 
                    pyttsx3.speak(f"{prompt}")
                    time.sleep(3)

        # except:
        #     pyttsx3.speak("Someting wrong right now so be careful nexttime")
    

# config of object and the __exit__ method is generate the concept of context manager concept right now r.adjust_for_ambient_noise(source, duration=1)