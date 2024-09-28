import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
#os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

system_prompt = """
You are a helpful assistant.
You have to provide detailed answers to the user's queries.
When the conversion ends you should say "Have a nice day".
"""
prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt), ("human", "{input}")]
)
llm = ChatGroq(temperature=0, model="llama3-8b-8192")
chain = prompt | llm | StrOutputParser()


st.title("Chat Assistant")
st.write("Ask your question below:")


user_question = st.text_input("What do you want to ask?")


if st.button("Ask"):
    if user_question:
        
        response = chain.invoke({"input": user_question})
        st.success(response)
    else:
        st.warning("Please enter a question.")
