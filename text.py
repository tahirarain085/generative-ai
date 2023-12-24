from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st 
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text
st.set_page_config("Q&A DEMO APP")
st.header("QUESTION GEMINI APPLICATION")
input = st.text_input("input: ", key="input")
submit = st.button("Ask The Question ")

if submit:
    response = get_gemini_response(input)
    st.subheader("The response is ")
    st.write(response)



