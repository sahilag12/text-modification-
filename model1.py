import google.generativeai as genai

import os

def model1(input_text,no_of_words):
    
    genai.configure(api_key="AIzaSyD8IUhM8QyB9e3aRqXrFm3bFTXPOqv4_qo")
    
    model=genai.GenerativeModel('gemini-pro')
    model=model.start_chat(history=[])
    command='''You should act like a experienced and expert professor who is a master in summarizing texts. Your work is to check the 
    summarize the given text and then give the summarizied text as output. Your text is....'''
    response=model.send_message(command+input_text+" . summarize in "+ str(no_of_words))
    
    return response.text

if __name__=='__main__':
    model1()