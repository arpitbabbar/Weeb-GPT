import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

os.environ['OPENAI_API_KEY'] = apikey

st.title('WEEB GPT')
name = st.text_input('What is your name?')

llm = OpenAI(temperature=0.5)

if name:
    st.write('Konichiwa ' + name + ' Senpai')
    anime = st.text_input('What Anime would you like to talk about?')
    if anime:
        st.write('Okay! Gathering information about '+anime)
        ques = st.text_input('Ask Your Ques!?')
        ques_template = PromptTemplate(
            input_variables=['ques'],
            template='In anime '+anime+' {ques}'
        )
        if ques:
            resp = llm(ques)
            st.write(resp)







