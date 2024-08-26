import streamlit as st
from transformers import pipeline

# set config
st.set_page_config(
    page_title="Text Generation APP",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("Text Generation App")

# Load the model
with st.spinner("Loading Model..."):
    generator = pipeline("text-generation", model="gpt2")  # you can use any model from the model hub

# prompt
prompt = st.text_input("Enter your prompt here")

# Generate the text
if st.button("Generate"):
    with st.spinner("Generating..."):
        result = generator(prompt)
        st.write(result)
