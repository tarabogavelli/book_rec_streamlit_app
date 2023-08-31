import pandas as pd
import streamlit as st
import langchain
import os
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import config
os.environ["OPENAI_API_KEY"] = config.API_KEY


st.title("Book Recommendations")
st.subheader("Enter your top 3 favorite books and their corresponding authors")
col1, col2 = st.columns(2)

with col1:
    book1 = st.text_input("Book 1: ")
    book2 = st.text_input("Book 2: ")
    book3 = st.text_input("Book 3: ")
with col2:
    author1 = st.text_input("Author 1: ")
    author2 = st.text_input("Author 2: ")
    author3 = st.text_input("Author 3: ")

if st.button('Get recommendations'):
    with st.spinner("Just a moment..."):
        template1 = """My favorite books are {book1} by {author1}, {book2} by {author2}, and {book3} by {author3} please recommend me 5 books based on my favorite books. Explain how the recommended books are similar to my favorite books"""
        prompt = PromptTemplate(template=template1, input_variables=["book1", "author1", "book2", "author2", "book3", "author3"])

        llm = ChatOpenAI(model_name="gpt-4")
        llm_chain = LLMChain(prompt=prompt, llm=llm)
        output = llm_chain.run(book1=book1, author1=author1, book2=book2, author2=author2, book3=book3, author3=author3)


        template2 = """My favorite books are {book1} by {author1}, {book2} by {author2}, and {book3} by {author3} please describe my book taste"""

        prompt2 = PromptTemplate(template=template2, input_variables=["book1", "author1", "book2", "author2", "book3", "author3"])
        llm_chain2 = LLMChain(prompt=prompt2, llm=llm)
        taste = llm_chain2.run(book1=book1, author1=author1, book2=book2, author2=author2, book3=book3, author3=author3)

        st.write(taste)
        st.write(output.format())
        st.balloons()
