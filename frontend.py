from model import extract_text_from_pdf, bart
from grammarmodel import grammar_check_model
import streamlit as st
from model1 import model1
from translate import translate

st.set_page_config(layout="wide")

            
def summarize(uploaded_file,input_text):
    with st.spinner("In progress"):
        extracted_text=""
        if uploaded_file is not None :extracted_text=extract_text_from_pdf(uploaded_file)
        else : extracted_text=input_text

        slider_value = st.slider("Select a value:", min_value=1, max_value=len(extracted_text.split()), value=5, step=1)

        if uploaded_file:
            if st.button('summarize'):
                col1, col2 = st.columns(2)
                with col1:
                    st.info("Extracted Text")
                    st.write(extracted_text)
                with col2:
                    # summary=bart(extracted_text,slider_value)
                    summary=model1(extracted_text,slider_value)
                    st.info("Summarization Complete")
                    st.success(summary)
                
        else:
            if input_text:
                if st.button("Summarize"):
                    col1, col2 = st.columns(2)
                    if(input_text==""): return
                    with col1:
                        st.info("Input Text")
                        st.write(input_text)
                    with col2:
                        # summary=bart(extracted_text,slider_value)
                        summary=model1(extracted_text,slider_value)
                        st.info("Summarization Complete")
                        st.success(summary)
                        
                    

def grammar_check(uploaded_file,input_text):
    with st.spinner("In progress"):
        extracted_text=""
        if uploaded_file is not None: extracted_text=extract_text_from_pdf(uploaded_file)
        else : extracted_text=input_text
        col1,col2=st.columns(2)
        with col1:
            st.info("Original text")
            st.write(extracted_text)
        with col2:
            st.info("Corrected text")
            st.write(grammar_check_model(extracted_text))

def Translate(uploaded_file,input_text):
    with st.spinner("In progress"):
        extracted_text=""

        if uploaded_file is not None: extracted_text=extract_text_from_pdf(uploaded_file)
        else : extracted_text=input_text
        destination_language=st.text_area("Enter your language")
        if st.button("Translate"):
        
            col1,col2=st.columns(2)
            with col1:
                st.info("Original text")
                st.write(extracted_text)
            with col2:
                st.info("Translated text")
                st.write(translate(extracted_text,destination_language))
    
    
    
def main():
    selected_section=""
    section_options=[
        "Summarize",
        "Translate",
        "Grammar Check"
    ]
    with st.sidebar:
        st.subheader("select file")
        uploaded_file = st.file_uploader("Upload your PDF file", type=['pdf'])
        input_text=st.text_area("Enter your text")
        if(uploaded_file or input_text):
            # st.sidebar.title("Summarizar OR QA with PDF")
            select_box_placeholder = st.sidebar.empty()
            selected_section = select_box_placeholder.selectbox("Select Task", section_options)
    if selected_section == "Summarize":
        summarize(uploaded_file,input_text)
    elif selected_section=="Translate":
        Translate(uploaded_file,input_text)
    elif selected_section=="Grammar Check":
        grammar_check(uploaded_file,input_text)
    
    
if __name__ =="__main__":
    main()