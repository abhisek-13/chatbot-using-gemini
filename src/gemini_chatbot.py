# importing the dependencies
import os
import dotenv
from dotenv import load_dotenv
import google.generativeai as genai

# importing the Google Gemini-pro model by API KEY
def gemini_chatbot(prompt):
    load_dotenv()
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
    llm = genai.GenerativeModel("gemini-pro")
    response = llm.generate_content(prompt)  # giving input to the gemini model and storing the response
    return response.text
