# from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Reasearch Tool")

user_input = st.text_input('Enter your prompt')

model = GoogleGenerativeAI(
    model="gemini-2.5-flash"
)

if st.button('summarize'):
    result = model.invoke(user_input)
    st.write(result)