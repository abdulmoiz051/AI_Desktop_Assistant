from google import genai
from random import randint
import os

client = genai.Client(api_key="AIzaSyB1ENqmJ1uEJpsr56r94cDUJeNExLENvrg")

def pass_prompt(prompt : str = "Nothing"):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents = prompt,   
    )
    return response.text

def generate_file(prompt_for_file : str):
    if not os.path.isdir("gemini_files"):
        os.mkdir("gemini_files")
    with open(f"gemini_files/gemini-{prompt_for_file[0:5]}-{randint(1, 100)}.txt", "w") as file:
        file.write(prompt_for_file)

# User say file then generate the file and prompt are different way means using pyttsx3