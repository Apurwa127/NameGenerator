import streamlit as st
from langchain_core.prompts import PromptTemplate
import os
from langchain_openai import ChatOpenAI
from secret_key import openai_key

st.title("Welcome to Bishal and Puja's baby name generator")
st.write("Hello! This is Apurwa Bhattarai and I would like to welome you to the baby's name generator website ")



def user_input():
    relation = st.text_input("please enter your relation with the couple: ")
    if relation:

        st.write("hello! ", relation)
        origin = st.selectbox('please select the language for the name that you wish',['Nepali', 'English', 'Chinese', 'Hindi'])
        os.environ['OPENAI_API_KEY'] = openai_key

        prompt = PromptTemplate(template="Generate atleast 5 unique and rare names of {origin} for both male and female and include the meaning of each names",
                                input_variables=['origin'])
        final_prompt = prompt.format(origin=origin)

        st.write(final_prompt)

        model = ChatOpenAI(model='gpt-5-mini',
                           temperature=0.9)

        chain = prompt | model

        if st.button("Generate Names"):
            try:
                response = chain.invoke({'origin': origin})
                st.write(response.content)
            except Exception as e:
                st.error(e)

user_input()