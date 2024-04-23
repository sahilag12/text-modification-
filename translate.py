import google.generativeai as genai

import os

def translate(input_text,destination_language):
    
    genai.configure(api_key="AIzaSyD8IUhM8QyB9e3aRqXrFm3bFTXPOqv4_qo")
    
    model=genai.GenerativeModel('gemini-pro')
    model=model.start_chat(history=[])
    command='''You should act like a experienced and expert translater who is a master in translating languages texts. Your work is to the 
    translate the given text and then give the translated text as output. Your text is....'''
    response=model.send_message(command+input_text+" . translate to "+ str(destination_language))
    
    return response.text

if __name__=='__main__':
    translate()