import streamlit as st
import google.generativeai as genai
from api import api

genai.configure(api_key=api)

defaults =  {
    'model' : 'models/text-bison-001',
    'temperature' : 0.2,
    'candidate_count' : 1,
    'max_output_tokens' : 800,
}

st.title('Prompt Ai Asisstant')
st.write('Coba dulu ah')
response = None

# Buat side panel
with st.sidebar:
    st.write('## Prompt AI Asisstant')
    # Buat Dropdown
    paa = st.selectbox('Choose selector : ',
                       ["Caption Sosial Media","Script","Storytellings","Backstories"])
    
    prompt = st.text_input('Write what you want to search for')

    if st.button('Generate'):
        response_prompt = f"Write a {paa.lower()}, in which you are a professional in the field who will deliver the material clearly. Also, use a friendly language. So write {prompt}."
        final_response_prompt = genai.generate_text(
            **defaults,
            prompt=response_prompt
        )
        response = final_response_prompt

if response != None:
    st.write(response.result)