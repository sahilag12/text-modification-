import google.generativeai as genai

import os

def grammar_check_model(input_text):
    
    genai.configure(api_key="AIzaSyD8IUhM8QyB9e3aRqXrFm3bFTXPOqv4_qo")
    
    model=genai.GenerativeModel('gemini-pro')
    model=model.start_chat(history=[])
    command='''You should act like a experienced english teacher. Your work is to check the 
    grammatical mistakes and spelling mistakes in the given text and then give the corrected text as output. Your text is....'''
    response=model.send_message(command+input_text)
    
    return response.text

if __name__=='__main__':
    grammar_check_model()